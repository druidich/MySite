from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.script import Manager
from config import config
from flask.ext.login import LoginManager

# app = Flask(__name__)
db = SQLAlchemy()

manager = Manager()
bootstrap = Bootstrap()
moment = Moment()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth/login'
# login_manager.init_app(app)


def create_app(configname):
    app = Flask(__name__)
    app.config.from_object(config[configname])
    config[configname].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    login_manager.init_app(app)
    return app
