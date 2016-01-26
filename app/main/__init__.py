from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..model import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
