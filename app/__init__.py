from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.script import Manager
from flask import Blueprint


import config

main = Blueprint('main', __name__)
db = SQLAlchemy()
manager = Manager()
bootstrap = Bootstrap()
moment = Moment()


def create_app(configname):
    app = Flask(__name__)
    app.config.from_object(config[configname])
    config[configname].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
