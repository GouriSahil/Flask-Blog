"""
Main Blueprint - Core Application Routes
=======================================

This blueprint handles the main pages of the blog that are accessible to all users.
These routes don't require authentication and serve as the public face of the application.

Routes:
- / (root) and /home: Display all blog posts with pagination
- /about: Static about page with information about the blog

Flow:
1. User visits home page → sees all published posts
2. User can browse posts with pagination (5 posts per page)
3. User can click on individual posts to read them
4. User can visit about page for blog information
"""

from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post

# Create main blueprint instance
# The first parameter 'main' is the blueprint name used in url_for()
# The second parameter __name__ is the module name for blueprint discovery
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    Home page route - displays all blog posts with pagination
    
    This route handles both the root URL (/) and /home URL.
    It shows the most recent posts first, with 5 posts per page.
    
    URL Parameters:
    - page: Page number for pagination (default: 1)
    
    Returns:
        Rendered home.html template with paginated posts
    """
    # Get page number from URL parameters, default to page 1
    page = request.args.get('page', 1, type=int)
    
    # Query all posts, ordered by date (newest first)
    # paginate() handles pagination automatically
    # per_page=5 means 5 posts per page
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    
    # Render the home template with the paginated posts
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    """
    About page route - displays static information about the blog
    
    This is a simple static page that doesn't require any database queries.
    It's used to provide information about the blog, its purpose, or the author.
    
    Returns:
        Rendered about.html template with title
    """
    return render_template('about.html', title='About')

# Route Summary:
# =============
# / or /home → Shows all blog posts with pagination
# /about → Shows static about page
# 
# Template Files Used:
# - home.html: Displays posts in a list format
# - about.html: Static content about the blog
# 
# Database Queries:
# - Post.query.order_by(Post.date_posted.desc()).paginate(): Gets paginated posts
