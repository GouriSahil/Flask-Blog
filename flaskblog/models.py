"""
Database Models for Flask Blog Application
==========================================

This file defines the database schema using SQLAlchemy ORM.
It contains two main models: User and Post, with a one-to-many relationship.

Database Schema:
- User: Stores user account information and authentication data
- Post: Stores blog posts with reference to their authors

Authentication Flow:
1. User registers with username, email, and password
2. Password is hashed using bcrypt before storage
3. User logs in with email/password combination
4. Flask-Login manages user sessions
5. Password reset functionality using secure tokens
"""

from datetime import datetime
from flaskblog import db, login_manager, app
from flask_login import login_user, UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

# User Loader Function for Flask-Login
# ===================================
# This function tells Flask-Login how to find a user by their ID
# It's called automatically when Flask-Login needs to load a user from the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    User Model - Handles user authentication and account management
    
    This model inherits from UserMixin which provides the required methods
    for Flask-Login to work properly (is_authenticated, is_active, etc.)
    
    Database Fields:
    - id: Primary key for user identification
    - username: Unique username for display
    - email: Unique email for login and communication
    - image_file: Profile picture filename (stored in static/profile_pics/)
    - password: Hashed password (never store plain text passwords!)
    - posts: Relationship to user's blog posts (one-to-many)
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    
    # Relationship: One user can have many posts
    # backref='author' creates an 'author' attribute on Post objects
    # lazy=True means posts are loaded only when accessed
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        """
        Generate a secure password reset token
        
        Args:
            expires_sec (int): Token expiration time in seconds (default: 30 minutes)
        
        Returns:
            str: URL-safe token that can be sent via email
        """
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """
        Verify and decode a password reset token
        
        Args:
            token (str): The token received via email
        
        Returns:
            User or None: User object if token is valid, None if invalid/expired
        """
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        """String representation of User object for debugging"""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    """
    Post Model - Handles blog post storage and management
    
    Database Fields:
    - id: Primary key for post identification
    - title: Post title (max 100 characters)
    - date_posted: Timestamp when post was created
    - content: Post content (unlimited text)
    - user_id: Foreign key linking to User table (author of the post)
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    # Foreign Key: Links to User table
    # This creates the relationship between Post and User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """String representation of Post object for debugging"""
        return f"Post('{self.title}', '{self.date_posted}')"

# Database Relationships Summary:
# =============================
# User (1) ←→ (Many) Post
# - One user can create many posts
# - Each post belongs to exactly one user (author)
# - Access user's posts: user.posts
# - Access post's author: post.author