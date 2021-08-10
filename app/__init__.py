from flask import Flask
from config import Config
from flask_login import LoginManager #for loging users in and maintaing a session
from flask_sqlalchemy import SQLAlchemy #this talks to our database for us 
from flask_migrate import Migrate #makes changing database a lot easier 
from flask_moment import Moment 

#---init Login Manager
login = LoginManager()
login.login_view = 'auth.login'
#---init the database from_object
login.login_message = "You must be logged in to view this page"
login.login_message_category = "warning"
db = SQLAlchemy()
#---init migrate
migrate = Migrate()
moment = Moment()

def create_app(config_class=Config):
    #---Instantiation
    app = Flask(__name__)
    #---name space of file. this passes the file into the flask application
    app.config.from_object(config_class)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    from.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from.blueprints.social_media import bp as social_bp
    app.register_blueprint(social_bp)

    return app

   
