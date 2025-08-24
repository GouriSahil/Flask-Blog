"""
Users Blueprint - User Authentication and Account Management
==========================================================

This blueprint handles all user-related functionality including:
- User registration and login/logout
- Account management and profile updates
- Password reset functionality
- User profile pages showing their posts

Authentication Flow:
1. User registers → account created with hashed password
2. User logs in → session created, redirected to home
3. User can update profile → change username, email, profile picture
4. User can reset password → email sent with secure token
5. User can view their posts → paginated list of user's blog posts

Security Features:
- Password hashing with bcrypt
- CSRF protection via Flask-WTF forms
- Secure password reset tokens
- Session management with Flask-Login
"""

from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.user.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from flaskblog.user.utils import save_picture, send_reset_email

# Create users blueprint instance
users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    """
    User registration route
    
    Flow:
    1. GET request → Show registration form
    2. POST request → Validate form data
    3. If valid → Create user account with hashed password
    4. Redirect to login page with success message
    
    Security:
    - Password is hashed using bcrypt before storage
    - Form validation prevents duplicate usernames/emails
    - CSRF protection via Flask-WTF
    """
    # If user is already logged in, redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    # Create registration form instance
    form = RegistrationForm()
    
    # Handle form submission
    if form.validate_on_submit():
        # Hash the password for secure storage
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        # Create new user object
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        # Save user to database
        db.session.add(user)
        db.session.commit()
        
        # Show success message and redirect to login
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    
    # Render registration form (GET request or validation failed)
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    """
    User login route
    
    Flow:
    1. GET request → Show login form
    2. POST request → Validate credentials
    3. If valid → Log user in and redirect
    4. If invalid → Show error message
    
    Features:
    - Remember me functionality
    - Redirect to originally requested page after login
    - Secure password verification
    """
    # If user is already logged in, redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    # Create login form instance
    form = LoginForm()
    
    # Handle form submission
    if form.validate_on_submit():
        # Find user by email
        user = User.query.filter_by(email=form.email.data).first()
        
        # Check if user exists and password is correct
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Log user in (creates session)
            login_user(user, remember=form.remember.data)
            
            # Get the page user was trying to access before login
            next_page = request.args.get('next')
            
            # Redirect to next page if it exists, otherwise go to home
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            # Show error message for invalid credentials
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    # Render login form (GET request or validation failed)
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    """
    User logout route
    
    Flow:
    1. End user session
    2. Redirect to home page
    
    Security:
    - Clears all session data
    - User must log in again to access protected routes
    """
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """
    User account management route
    
    Flow:
    1. GET request → Show account form with current data
    2. POST request → Update account information
    3. Handle profile picture upload if provided
    
    Features:
    - Profile picture upload and storage
    - Username and email updates
    - Form pre-populated with current data
    
    Security:
    - @login_required decorator ensures only logged-in users can access
    - Only the user can update their own account
    """
    # Create account update form
    form = UpdateAccountForm()
    
    # Handle form submission
    if form.validate_on_submit():
        # Handle profile picture upload
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        
        # Update user information
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        # Save changes to database
        db.session.commit()
        
        # Show success message
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    
    # Handle GET request - populate form with current user data
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    # Get profile picture URL for display
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    
    # Render account page
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    """
    User profile page showing all posts by a specific user
    
    Flow:
    1. Find user by username
    2. Get all posts by that user with pagination
    3. Display posts in chronological order
    
    URL Parameters:
    - username: The username whose posts to display
    
    Features:
    - Pagination (5 posts per page)
    - Posts ordered by date (newest first)
    - 404 error if user doesn't exist
    """
    # Get page number for pagination
    page = request.args.get('page', 1, type=int)
    
    # Find user by username, return 404 if not found
    user = User.query.filter_by(username=username).first_or_404()
    
    # Get user's posts with pagination
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    
    # Render user posts page
    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    """
    Password reset request route
    
    Flow:
    1. GET request → Show password reset form
    2. POST request → Send reset email if user exists
    3. Always show success message (security best practice)
    
    Security:
    - Doesn't reveal if email exists in database
    - Sends reset email with secure token
    - Token expires after 30 minutes
    """
    # If user is already logged in, redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    # Create password reset form
    form = RequestResetForm()
    
    # Handle form submission
    if form.validate_on_submit():
        # Find user by email
        user = User.query.filter_by(email=form.email.data).first()
        
        # Send reset email (even if user doesn't exist for security)
        send_reset_email(user)
        
        # Show success message
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    
    # Render password reset form
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    """
    Password reset token verification and password update
    
    Flow:
    1. Verify reset token
    2. GET request → Show new password form
    3. POST request → Update password if token is valid
    
    Security:
    - Token verification prevents unauthorized password changes
    - Token expiration ensures security
    - New password is hashed before storage
    """
    # If user is already logged in, redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    # Verify the reset token
    user = User.verify_reset_token(token)
    
    # If token is invalid or expired
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    
    # Create new password form
    form = ResetPasswordForm()
    
    # Handle form submission
    if form.validate_on_submit():
        # Hash the new password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        # Update user's password
        user.password = hashed_password
        
        # Save to database
        db.session.commit()
        
        # Show success message and redirect to login
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    
    # Render password reset form
    return render_template('reset_token.html', title='Reset Password', form=form)

# Route Summary:
# =============
# /register → User registration with password hashing
# /login → User authentication with session management
# /logout → End user session
# /account → Account management and profile updates
# /user/<username> → Display user's blog posts
# /reset_password → Request password reset via email
# /reset_password/<token> → Complete password reset with token verification
# 
# Security Features:
# - Password hashing with bcrypt
# - CSRF protection via Flask-WTF
# - Secure password reset tokens
# - Session management with Flask-Login
# - @login_required decorator for protected routes

