# 📝 Flask Blog

A full-featured blogging platform built with Flask that demonstrates modern web development practices including user authentication, CRUD operations, and responsive design.

## 🚀 Live Demo

This project is deployed and live at [blogs.sahilgouri.me](https://blogs.sahilgouri.me)

> **Note**: The blog currently uses **dummy data and test posts** to demonstrate functionality.  
> **Note 2**: The app is deployed on a **free-tier hosting provider**, so initial loading may be slow when the server spins up.  

## ✨ Features

### 🔐 User Authentication & Management
- **User Registration & Login**: Secure user registration with email validation
- **Password Reset**: Email-based password reset functionality using secure tokens
- **Session Management**: Persistent login sessions with Flask-Login
- **Profile Management**: Update account details and profile pictures
- **Authorization**: Role-based access control for post management

### 📝 Blog Post Management
- **Create Posts**: Rich text editor for creating new blog posts
- **Edit & Delete**: Authors can edit and delete their own posts
- **Post Pagination**: Efficient pagination for large numbers of posts
- **Post History**: Chronological display of posts with timestamps
- **Author Attribution**: Posts are linked to their authors

### 🎨 User Interface
- **Responsive Design**: Bootstrap-based responsive layout
- **Modern UI**: Clean, professional interface with navigation
- **User Profiles**: Individual user post pages
- **Flash Messages**: User-friendly notifications for actions
- **Image Upload**: Profile picture upload functionality

### 🔧 Technical Features
- **Database Management**: SQLite database with SQLAlchemy ORM
- **Form Validation**: WTForms integration with custom validators
- **Security**: Password hashing with bcrypt
- **Email Integration**: SMTP email functionality for password resets
- **Blueprint Architecture**: Modular code organization with Flask blueprints

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Flask 3.x |
| **Database** | SQLite with SQLAlchemy ORM |
| **Authentication** | Flask-Login, Flask-Bcrypt |
| **Forms** | Flask-WTF, WTForms |
| **Email** | Flask-Mail |
| **Frontend** | HTML5, CSS3, Bootstrap |
| **Templating** | Jinja2 |
| **Development** | Python 3.12+ |

## 🧑‍💻 My Role & Contributions

- Designed and developed the entire application from scratch using **Flask**  
- Deployed the project live on a custom domain: [blogs.sahilgouri.me](https://blogs.sahilgouri.me)  
- Extended the base tutorial with **advanced features**:  
  - Email-based password reset with secure tokens  
  - Role-based access control for posts  
  - Profile image upload with image processing  
- Implemented **security best practices**: bcrypt password hashing, CSRF protection, and secure session management  
- Structured the project using **Flask Blueprints** for clean, modular architecture  
- Documented installation, setup, and usage for easy reproducibility  


## 📁 Project Structure

```
Flask-Blog/
├── flaskblog/
│   ├── __init__.py          # Flask app configuration
│   ├── models.py            # Database models (User, Post)
│   ├── main/               # Main routes (home, about)
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── user/               # User authentication routes
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── utils.py
│   ├── posts/              # Blog post management routes
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── templates/          # Jinja2 HTML templates
│   └── static/             # CSS, images, and static files
├── run.py                  # Application entry point
├── create_db.py           # Database initialization script
├── pyproject.toml         # Project dependencies and metadata
├── uv.lock               # Lock file for uv package manager
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- uv package manager (recommended) or pip

### Installation Options

#### Option 1: Using uv Package Manager (Recommended)

1. **Install uv** (if not already installed)
   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/GouriSahil/Flask-Blog.git
   cd Flask-Blog
   ```

3. **Initialize the project with uv**
   ```bash
   uv init
   ```


4. **Install dependencies**
   ```bash
   uv add flask flask-sqlalchemy flask-login flask-bcrypt flask-wtf flask-mail email-validator pillow python-dotenv
   ```

5. **Initialize the database**
   ```bash
   uv run python create_db.py
   ```

6. **Run the application**
   ```bash
   uv run python run.py
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

#### Option 2: Using Traditional pip

1. **Clone the repository**
   ```bash
   git clone https://github.com/GouriSahil/Flask-Blog.git
   cd Flask-Blog
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-bcrypt flask-wtf flask-mail email-validator pillow python-dotenv
   ```

4. **Initialize the database**
   ```bash
   python create_db.py
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`


## 🔧 Configuration

### Environment Variables (Optional)
For email functionality (password reset), set these environment variables:
- `EMAIL_USER`: Gmail address for password reset emails
- `EMAIL_PASS`: Gmail app password for SMTP authentication

### Database Configuration
- **Database**: SQLite (`site.db`)
- **Location**: `instance/site.db` (created automatically)

## 📚 Application Routes

### Public Routes
- `GET /` or `GET /home` - Home page with blog posts
- `GET /about` - About page
- `GET /register` - User registration
- `GET /login` - User login


### Protected Routes
- `GET /account` - User account management
- `POST /account` - Update account information
- `GET /post/new` - Create new post form
- `POST /post/new` - Create new post
- `GET /post/<int:post_id>` - View specific post
- `GET /post/<int:post_id>/update` - Edit post form
- `POST /post/<int:post_id>/update` - Update post
- `POST /post/<int:post_id>/delete` - Delete post
- `GET /user/<string:username>` - User profile page
- `GET /logout` - User logout



## 🔒 Security Features

- **Password Hashing**: Bcrypt for secure password storage
- **CSRF Protection**: Flask-WTF CSRF tokens on all forms
- **Session Security**: Secure session management with Flask-Login
- **Input Validation**: Form validation with WTForms
- **Authorization**: User-specific post access control

## 🧪 Testing

To test the application functionality:

1. **Register a new account** or use the default credentials
2. **Create a new post** using the "New Post" button
3. **Edit your posts** by clicking the edit button
4. **Test password reset** functionality (requires email configuration)
5. **Upload a profile picture** in the account section
6. **View user profiles** by clicking on usernames

## 🚀 Deployment

### Local Development
```bash
# Using uv
uv run python run.py

# Using traditional pip
python run.py
```

### Production Deployment
For production deployment, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up a proper database (PostgreSQL, MySQL)
- Configuring environment variables
- Setting up HTTPS
- Using a reverse proxy (Nginx)
- Using Docker for containerization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- Flask community for the excellent framework
- Bootstrap for the responsive UI components
- SQLAlchemy for the ORM functionality
- uv team for the fast Python package manager

---

**Built with ❤️ using Flask**


