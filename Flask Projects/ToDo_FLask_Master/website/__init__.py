# Read README.md to run project
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating database object
sql_db = SQLAlchemy()
DB_NAME = 'todo.db'

# To check if database has been already created or not
def create_database(main_app):
    if not path.exists('website/' + DB_NAME):
        sql_db.create_all(app=main_app) # Creates a database in directory
        print('Database Created!')


def initialize_app():
    # Creating main app object
    app = Flask(__name__) # Default app name

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Because there were some warnings
    sql_db.init_app(app)

    # Import and initialize views(blueprints) here
    from .views import views # Importing here because of circular dependency issue

    app.register_blueprint(views, url_prefix='/')  
    # app.register_blueprint(home, url_prefix='/flask-todo/') Example: Sets prefix as flask-todo but does not set automatically

    create_database(app)
    return app