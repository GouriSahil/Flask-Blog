"""
Posts Blueprint - Blog Post Management (CRUD Operations)
======================================================

This blueprint handles all blog post-related functionality including:
- Creating new blog posts
- Reading/viewing individual posts
- Updating existing posts
- Deleting posts

CRUD Operations:
- CREATE: /post/new - Create new blog post
- READ: /post/<id> - View specific blog post
- UPDATE: /post/<id>/update - Edit existing blog post
- DELETE: /post/<id>/delete - Remove blog post

Security Features:
- @login_required decorator for create/update/delete operations
- Authorization checks ensure users can only modify their own posts
- CSRF protection via Flask-WTF forms
- Proper error handling with 404 and 403 responses

User Flow:
1. Logged-in user creates new post → /post/new
2. Anyone can view posts → /post/<id>
3. Author can edit their posts → /post/<id>/update
4. Author can delete their posts → /post/<id>/delete
"""

from flask import Blueprint
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

# Create posts blueprint instance
posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    """
    Create new blog post route
    
    Flow:
    1. GET request → Show post creation form
    2. POST request → Validate form and save post
    3. Redirect to home page with success message
    
    Security:
    - @login_required ensures only logged-in users can create posts
    - Form validation prevents empty or invalid posts
    - CSRF protection via Flask-WTF
    
    Database Operations:
    - Creates new Post object with current user as author
    - Saves to database with automatic timestamp
    """
    # Create post form instance
    form = PostForm()
    
    # Handle form submission
    if form.validate_on_submit():
        # Create new post with current user as author
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        
        # Save post to database
        db.session.add(post)
        db.session.commit()
        
        # Show success message and redirect to home
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    
    # Render post creation form (GET request or validation failed)
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    """
    View individual blog post route
    
    Flow:
    1. Find post by ID
    2. Return 404 if post doesn't exist
    3. Display post with full content
    
    Features:
    - Public access (no login required)
    - 404 error handling for non-existent posts
    - Displays post title, content, author, and date
    
    URL Parameters:
    - post_id: The ID of the post to display
    """
    # Find post by ID, return 404 if not found
    post = Post.query.get_or_404(post_id)
    
    # Render post view template
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """
    Update existing blog post route
    
    Flow:
    1. Find post by ID
    2. Check if current user is the author
    3. GET request → Show form with current post data
    4. POST request → Update post if user is authorized
    
    Security:
    - @login_required ensures only logged-in users can access
    - Authorization check prevents users from editing others' posts
    - 403 Forbidden error if user is not the author
    
    Authorization:
    - Only the post author can update their posts
    - Returns 403 Forbidden if unauthorized access attempted
    """
    # Find post by ID, return 404 if not found
    post = Post.query.get_or_404(post_id)
    
    # Check if current user is the author of the post
    if post.author != current_user:
        # Return 403 Forbidden if user is not the author
        abort(403)
    
    # Create post form instance
    form = PostForm()
    
    # Handle form submission
    if form.validate_on_submit():
        # Update post content
        post.title = form.title.data
        post.content = form.content.data
        
        # Save changes to database
        db.session.commit()
        
        # Show success message and redirect to post view
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    
    # Handle GET request - populate form with current post data
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    
    # Render post update form
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    """
    Delete blog post route
    
    Flow:
    1. Find post by ID
    2. Check if current user is the author
    3. Delete post from database
    4. Redirect to home with success message
    
    Security:
    - @login_required ensures only logged-in users can access
    - Authorization check prevents users from deleting others' posts
    - 403 Forbidden error if user is not the author
    - Only POST method allowed (prevents accidental deletion via GET)
    
    Authorization:
    - Only the post author can delete their posts
    - Returns 403 Forbidden if unauthorized access attempted
    
    Database Operations:
    - Permanently removes post from database
    - No soft delete - post is completely removed
    """
    # Find post by ID, return 404 if not found
    post = Post.query.get_or_404(post_id)
    
    # Check if current user is the author of the post
    if post.author != current_user:
        # Return 403 Forbidden if user is not the author
        abort(403)
    
    # Delete post from database
    db.session.delete(post)
    db.session.commit()
    
    # Show success message and redirect to home
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

# Route Summary:
# =============
# /post/new → Create new blog post (POST only, login required)
# /post/<id> → View specific blog post (public access)
# /post/<id>/update → Edit existing blog post (login + authorization required)
# /post/<id>/delete → Delete blog post (POST only, login + authorization required)
# 
# Security Features:
# - @login_required decorator for create/update/delete operations
# - Authorization checks ensure users can only modify their own posts
# - CSRF protection via Flask-WTF forms
# - Proper error handling (404 for missing posts, 403 for unauthorized access)
# 
# Database Operations:
# - CREATE: db.session.add(post) + db.session.commit()
# - READ: Post.query.get_or_404(post_id)
# - UPDATE: Modify post attributes + db.session.commit()
# - DELETE: db.session.delete(post) + db.session.commit()
# 
# Template Files Used:
# - create_post.html: Form for creating and updating posts
# - post.html: Display individual post with full content







