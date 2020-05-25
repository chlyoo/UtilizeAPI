from flask import Blueprint
mailing = Blueprint('/mailing', __name__)
from . import views
