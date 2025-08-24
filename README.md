# Flask Blog Application

A complete blog application built with Flask, featuring user authentication, blog post management, and a modern responsive UI.

## 🏗️ Project Architecture

This project uses **Flask Blueprints** for modular organization. Think of blueprints as separate modules that handle different parts of the application.

### 📁 Project Structure

```
Flask-Blog/
├── flaskblog/
│   ├── __init__.py          # Main application factory & configuration
│   ├── models.py            # Database models (User, Post)
│   ├── main/                # Main blueprint - public pages
│   │   ├── __init__.py
│   │   └── routes.py        # Home & About routes
│   ├── user/                # Users blueprint - authentication
│   │   ├── __init__.py
│   │   ├── routes.py        # Login, register, account routes
│   │   ├── forms.py         # User-related forms
│   │   └── utils.py         # Helper functions
│   ├── posts/               # Posts blueprint - blog management
│   │   ├── __init__.py
│   │   ├── routes.py        # CRUD operations for posts
│   │   └── forms.py         # Post-related forms
│   ├── templates/           # HTML templates
│   └── static/              # CSS, JS, images
├── instance/                # Database files
├── main.py                  # Application entry point
└── run.py                   # Development server runner
```

## 🔄 Application Flow

### 1. **Application Initialization** (`flaskblog/__init__.py`)
- Creates Flask app instance
- Configures database, authentication, email
- Registers all blueprints

### 2. **Blueprint Organization**

#### **Main Blueprint** (`flaskblog/main/routes.py`)
- **Purpose**: Public pages accessible to everyone
- **Routes**:
  - `/` and `/home` → Display all blog posts with pagination
  - `/about` → Static about page

#### **Users Blueprint** (`flaskblog/user/routes.py`)
- **Purpose**: User authentication and account management
- **Routes**:
  - `/register` → Create new user account
  - `/login` → User authentication
  - `/logout` → End user session
  - `/account` → Update profile information
  - `/user/<username>` → View user's posts
  - `/reset_password` → Password reset request
  - `/reset_password/<token>` → Complete password reset

#### **Posts Blueprint** (`flaskblog/posts/routes.py`)
- **Purpose**: Blog post CRUD operations
- **Routes**:
  - `/post/new` → Create new blog post
  - `/post/<id>` → View specific post
  - `/post/<id>/update` → Edit existing post
  - `/post/<id>/delete` → Delete post

### 3. **Database Models** (`flaskblog/models.py`)

#### **User Model**
```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
```

#### **Post Model**
```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

**Relationship**: One User can have many Posts (one-to-many)

## 🔐 Security Features

### Authentication & Authorization
- **Password Hashing**: bcrypt for secure password storage
- **Session Management**: Flask-Login for user sessions
- **CSRF Protection**: Flask-WTF forms prevent cross-site request forgery
- **Authorization**: Users can only modify their own posts

### Password Reset
- **Secure Tokens**: Time-limited tokens for password reset
- **Email Integration**: SMTP email sending for reset links
- **Token Verification**: Validates tokens before allowing password changes

## 🎨 Frontend Structure

### Template Inheritance
- **Base Template**: `layout.html` provides common structure
- **Page Templates**: Extend base template for specific pages
- **Responsive Design**: Bootstrap 4 for mobile-friendly UI

### Navigation
- **Public Navigation**: Home, About (accessible to everyone)
- **User Navigation**: Login/Register (guests) vs New Post/Account/Logout (authenticated users)

## 🚀 User Journey Examples

### New User Registration
1. User visits `/register`
2. Fills out registration form
3. Password is hashed and stored
4. User is redirected to login page
5. User logs in and can create posts

### Creating a Blog Post
1. Logged-in user clicks "New Post"
2. User fills out post form
3. Post is saved to database with user as author
4. User is redirected to home page
5. New post appears in post list

### Reading and Managing Posts
1. Anyone can view posts at `/post/<id>`
2. Post author sees edit/delete buttons
3. Author can update or delete their posts
4. Non-authors get 403 error if trying to modify others' posts

## 🔧 Key Technologies

- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and CSRF protection
- **Bcrypt**: Password hashing
- **Bootstrap**: Frontend framework
- **SQLite**: Database (can be changed to PostgreSQL/MySQL)

## 📝 Development Notes

### Blueprint Benefits
- **Modularity**: Each blueprint handles specific functionality
- **Maintainability**: Easy to find and modify features
- **Scalability**: Can add new blueprints without affecting existing ones
- **Testing**: Can test each blueprint independently

### Database Operations
- **CREATE**: `db.session.add(object)` + `db.session.commit()`
- **READ**: `Model.query.get(id)` or `Model.query.filter_by().first()`
- **UPDATE**: Modify object attributes + `db.session.commit()`
- **DELETE**: `db.session.delete(object)` + `db.session.commit()`

### URL Generation
- **Blueprint Routes**: `url_for('blueprint_name.route_function')`
- **Examples**:
  - `url_for('main.home')` → `/home`
  - `url_for('users.login')` → `/login`
  - `url_for('posts.new_post')` → `/post/new`

## 🛠️ Running the Application

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables** (for email functionality):
   ```bash
   export EMAIL_USER="your-email@gmail.com"
   export EMAIL_PASS="your-app-password"
   ```

3. **Initialize Database**:
   ```bash
   python create_db.py
   ```

4. **Run Development Server**:
   ```bash
   python run.py
   ```

5. **Access Application**: http://localhost:5000

## 🔍 Understanding the Code

### For New Contributors

1. **Start with `__init__.py`**: Understand how the app is configured
2. **Review `models.py`**: See the data structure
3. **Examine blueprints**: Each handles specific functionality
4. **Check templates**: See how the UI is structured
5. **Follow user flows**: Trace through registration → login → posting

### Key Concepts to Understand

- **Blueprint Pattern**: Modular organization of routes
- **Template Inheritance**: Base template with page-specific content
- **Database Relationships**: One-to-many between User and Post
- **Authentication Flow**: Registration → Login → Session Management
- **Authorization**: Users can only modify their own content

This application demonstrates best practices for Flask development with proper separation of concerns, security measures, and scalable architecture.


