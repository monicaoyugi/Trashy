from . import auth
from ..models import User
from .. import db
from flask_login import login_user, login_required, logout_user,current_user