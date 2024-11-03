from flaskblog import app, db
from flaskblog.models import User, Post
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt(app)

with app.app_context():
    # Create the database and tables
    db.create_all()

    # Create initial users
    hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
    user1 = User(username='Gouri Sahil', email='gouri@gmail.com', password=hashed_password)
    user2 = User(username='Asrar', email='asrar@demo.com', password=hashed_password)

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Create initial posts
    post1 = Post(title='Blog post 1', content='First post content', author=user1, date_posted=datetime(2021, 4, 20))
    post2 = Post(title='Blog post 2', content='Second post content', author=user2, date_posted=datetime(2021, 4, 21))

    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()

    print("Database created and initial data added.")
