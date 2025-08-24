"""
Flask Blog Application - Main Application Factory
================================================

This file initializes the Flask application and configures all extensions.
It serves as the entry point for the entire application.

Application Flow:
1. Flask app creation and configuration
2. Database setup (SQLAlchemy)
3. Authentication setup (Flask-Login, Bcrypt)
4. Email configuration (Flask-Mail)
5. Blueprint registration for modular routing

Blueprints Used:
- main: Core pages (home, about)
- users: User authentication and account management
- posts: Blog post CRUD operations
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# Create Flask application instance
app = Flask(__name__)

# Application Configuration
# ========================
app.config['SECRET_KEY'] = b'14aa8f03f34ea5c388abe7eee5b21d92'  # Required for session management and CSRF protection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database file location

# Initialize Flask Extensions
# ==========================
db = SQLAlchemy(app)  # Database ORM for easy database operations
bcrypt = Bcrypt(app)  # Password hashing for security
login_manager = LoginManager(app)  # User session management
login_manager.login_view = 'users.login'  # Redirect to login page if user not authenticated
login_manager.login_message_category = 'info'  # Bootstrap alert category for login messages

# Email Configuration for Password Reset
# =====================================
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 587  # TLS port for Gmail
app.config['MAIL_USE_TLS'] = True  # Enable TLS encryption
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  # Email username from environment variable
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  # Email password from environment variable
mail = Mail(app)  # Initialize email functionality

# Blueprint Registration
# =====================
# Import all blueprint modules
from flaskblog.user.routes import users      # User authentication routes
from flaskblog.posts.routes import posts     # Blog post management routes
from flaskblog.main.routes import main       # Core application routes

# Register blueprints with the main application
# This makes all routes defined in blueprints available in the main app
app.register_blueprint(users)   # Handles: /register, /login, /logout, /account, /user/<username>, /reset_password
app.register_blueprint(posts)   # Handles: /post/new, /post/<id>, /post/<id>/update, /post/<id>/delete
app.register_blueprint(main)    # Handles: /, /home, /about

# Note: The order of registration doesn't matter for functionality,
# but it's good practice to register them in a logical order