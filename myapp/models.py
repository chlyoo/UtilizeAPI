from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# 20191108
from flask import current_app, request, url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer 
# 20191112
from flask_login import AnonymousUserMixin

# 20191122
from datetime import datetime


