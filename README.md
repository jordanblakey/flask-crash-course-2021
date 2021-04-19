# Flask Crash Course

## Project Set Up

```sh
virtualenv -p python3 <env_name>
. ./<env_name>/bin/activate.fish
pip install flask
pip freeze > requirements.txt
pip install -r requirements.txt

# RUNNING THE DEV SERVER
# Code changes require restart. Debug mode enables hot reloading.
export FLASK_APP=<app_name>.py
export FLASK_DEBUG=1
flask run

# ALTERNATIVELY, YOU CAN RUN DIRECTLY USING PYTHON
python <app_name>.py

# See file structure
tree -I 'venv|*.pyc|__pycache__'
```

### Working with SQL Alchemy

```sh
# Create SQLite 3 Database
python # enter the Python interpreter
from flaskblog import db
db.create_all() # Creates the site.db SQLite db on disk, with models defining tables.
from flaskblog import User, Post
user_1 = User(username='John', email='john@mail.com', password='password')
db.session.add(user_1)
db.session.commit()
User.query.all() # return all rows from the user table (based on user model)
User.query.first() # return only the first row
User.query.filter_by(username='jordan').all()
User.query.filter_by(username='jordan').first()
user = User.query.get(1)
post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()
user.posts
post = Post.query.first()
post
Post('Blog 1', '2021-04-18 17:48:48.610192')
post.author
User('jordan', 'jordan.t.blakey@gmail.com', 'default.jpg')
db.drop_all() # Drop all tables
db.create_all() # Create all tables based on models
User.query.all() # []
Post.query.all() # []
```

### Hashing Passwords with Bcrypt

```python
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing').decode('utf-8') # '$2b$12$eqKyxBnVh7EGd5bBDJoytuADn.Iui.NBSgZ3SivHclb0VD7zF.YG6'
hashed_password = bcrypt.generate_password_hash('testing')
bcrypt.check_password_hash(hashed_password, 'password') # False
bcrypt.check_password_hash(hashed_password, 'testing') # True
```
