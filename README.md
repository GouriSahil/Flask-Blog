# 📝 Flask Blog

A full-featured blogging platform built with Flask that demonstrates modern web development practices including user authentication, CRUD operations, and responsive design.

## 🚀 Live Demo

Visit the application at `http://localhost:5000` after running the setup instructions below.

## ✨ Features

### 🔐 User Authentication & Management
- **User Registration & Login**: Secure user registration with email validation
- **Password Reset**: Email-based password reset functionality
- **Session Management**: Persistent login sessions with "Remember Me" option
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
- **Blueprint Architecture**: Modular code organization

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Flask 2.x |
| **Database** | SQLite with SQLAlchemy ORM |
| **Authentication** | Flask-Login, Flask-Bcrypt |
| **Forms** | Flask-WTF, WTForms |
| **Email** | Flask-Mail |
| **Frontend** | HTML5, CSS3, Bootstrap 4.5 |
| **Templating** | Jinja2 |
| **Development** | Python 3.x |

## 📁 Project Structure

```
flaskblog/
├── flaskblog/
│   ├── __init__.py          # Flask app configuration
│   ├── models.py            # Database models (User, Post)
│   ├── main/               # Main routes (home, about)
│   ├── user/               # User authentication routes
│   ├── posts/              # Blog post management routes
│   ├── templates/          # Jinja2 HTML templates
│   └── static/             # CSS, images, and static files
├── run.py                  # Application entry point
├── create_db.py           # Database initialization script
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flaskblog
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-bcrypt flask-wtf flask-mail
   ```

4. **Set up environment variables** (optional)
   ```bash
   export EMAIL_USER=your-email@gmail.com
   export EMAIL_PASS=your-app-password
   ```

5. **Initialize the database**
   ```bash
   python create_db.py
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Default Credentials
The database initialization script creates two test users:
- **User 1**: `gouri@gmail.com` / `password`
- **User 2**: `asrar@demo.com` / `password`

## 🔧 Configuration

### Environment Variables
- `EMAIL_USER`: Gmail address for password reset emails
- `EMAIL_PASS`: Gmail app password for SMTP authentication

### Database Configuration
- **Database**: SQLite (`site.db`)
- **Location**: `instance/site.db` (created automatically)

## 📚 API Endpoints

### Public Routes
- `GET /` - Home page with blog posts
- `GET /about` - About page
- `GET /register` - User registration
- `GET /login` - User login
- `GET /reset_password` - Password reset request

### Protected Routes
- `GET /account` - User account management
- `GET /post/new` - Create new post
- `GET /post/<int:post_id>` - View specific post
- `GET /post/<int:post_id>/update` - Edit post
- `GET /post/<int:post_id>/delete` - Delete post
- `GET /user/<string:username>` - User profile page

## 🗄️ Database Schema

### User Model
- `id` (Primary Key)
- `username` (Unique, 20 chars)
- `email` (Unique, 120 chars)
- `image_file` (Profile picture filename)
- `password` (Hashed with bcrypt)

### Post Model
- `id` (Primary Key)
- `title` (100 chars)
- `date_posted` (DateTime)
- `content` (Text)
- `user_id` (Foreign Key to User)

## 🔒 Security Features

- **Password Hashing**: Bcrypt for secure password storage
- **CSRF Protection**: Flask-WTF CSRF tokens
- **Session Security**: Secure session management
- **Input Validation**: Form validation with WTForms
- **Authorization**: User-specific post access control

## 🧪 Testing

To test the application functionality:

1. **Register a new account** or use the default credentials
2. **Create a new post** using the "New Post" button
3. **Edit your posts** by clicking the edit button
4. **Test password reset** functionality
5. **Upload a profile picture** in the account section

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production Deployment
For production deployment, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up a proper database (PostgreSQL, MySQL)
- Configuring environment variables
- Setting up HTTPS
- Using a reverse proxy (Nginx)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Flask community for the excellent framework
- Bootstrap for the responsive UI components
- SQLAlchemy for the ORM functionality

---

**Built with ❤️ using Flask**


