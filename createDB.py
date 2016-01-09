# from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
# from config import SQLALCHEMY_TRACK_MODIFICATIONS
from app import db

from app import model

SQLALCHEMY_TRACK_MODIFICATIONS = True
db.create_all()