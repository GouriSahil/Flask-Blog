import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()

# Flask-WTF reads WTF_CSRF_SECRET_KEY first; if that key exists with value None, CSRF breaks.
# Normalize env (empty / whitespace-only counts as unset). Use a dev default only when unset.
_dev_secret = "dev-only-insecure-key"


def _env_nonempty(name: str) -> str | None:
    v = os.getenv(name)
    if v is None:
        return None
    v = v.strip()
    return v if v else None


app = Flask(__name__)

# Always reload templates from disk (avoids “no changes” when the server runs with debug off).
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Bust browser/CDN caches for main.css after UI changes (override with env ASSET_VERSION).
app.config["ASSET_VERSION"] = _env_nonempty("ASSET_VERSION") or "3"


_secret = _env_nonempty('SECRET_KEY') or _dev_secret
app.config['SECRET_KEY'] = _secret
app.config['WTF_CSRF_SECRET_KEY'] = _env_nonempty('WTF_CSRF_SECRET_KEY') or _secret
database_url = os.getenv('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///site.db'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)               
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Email configuration (optional for deployment)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog.user.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)