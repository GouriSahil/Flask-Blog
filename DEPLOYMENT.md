# Flask Blog Deployment Guide

## Fixing 502 Bad Gateway Error

### 1. Environment Variables Required

Set these environment variables in your deployment platform:

```bash
SECRET_KEY=your-secure-secret-key-here
FLASK_ENV=production
DATABASE_URL=your-database-url
PORT=5000
```

### 2. Database Setup

For production, you'll need a PostgreSQL database. The app will automatically handle the URL conversion.

### 3. Dependencies

All required dependencies are now in `requirment.txt`:
- flask>=3.1.1
- Flask-WTF>=1.2.2
- gunicorn>=23.0.0
- flask-sqlalchemy>=3.1.1
- flask-bcrypt>=1.0.1
- flask-login>=0.6.3
- flask-mail>=0.10.0
- flask-migrate>=4.1.0
- email-validator>=2.2.0
- pillow>=11.3.0
- python-dotenv>=1.1.1

### 4. Deployment Platforms

#### Render.com
- Use `wsgi.py` as the entry point
- Set environment variables in the dashboard
- Build command: `pip install -r requirment.txt`
- Start command: `gunicorn wsgi:app`

#### Heroku
- Use the `Procfile` provided
- Set environment variables in Heroku dashboard
- Deploy with: `git push heroku main`

#### Railway
- Use `wsgi.py` as the entry point
- Set environment variables in Railway dashboard

### 5. Common 502 Error Causes Fixed

✅ **Missing dependencies** - Now included in requirements.txt
✅ **Wrong WSGI configuration** - Created proper wsgi.py
✅ **Development settings** - Updated for production
✅ **Missing environment variables** - Added proper fallbacks
✅ **Port binding** - Fixed to use environment PORT

### 6. Testing Locally

```bash
# Install dependencies
pip install -r requirment.txt

# Set environment variables
export SECRET_KEY="your-secret-key"
export FLASK_ENV="production"

# Run with Gunicorn
gunicorn wsgi:app

# Or run with Flask
python run.py
```

### 7. Database Migration

If using PostgreSQL, you may need to run migrations:

```bash
flask db upgrade
```

## Troubleshooting

If you still get 502 errors:

1. Check deployment logs for specific error messages
2. Verify all environment variables are set
3. Ensure database is accessible
4. Check if the port is correctly configured
5. Verify all dependencies are installed

The main fixes applied:
- ✅ Updated `run.py` for production
- ✅ Complete `requirment.txt` with all dependencies
- ✅ Created `wsgi.py` for WSGI servers
- ✅ Created `Procfile` for Heroku
- ✅ Updated Flask config for environment variables
- ✅ Added database URL handling for PostgreSQL
