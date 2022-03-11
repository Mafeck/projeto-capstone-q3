from flask import Blueprint
from app.controllers import users_controllers


bp_users = Blueprint("users", __name__, url_prefix="/users")

bp_users.post("/register")(users_controllers.create_user)
bp_users.post("/login")(users_controllers.login_user)
bp_users.patch("")(users_controllers.update_user)
bp_users.get("")(users_controllers.get_user)
bp_users.delete("")(users_controllers.remove_user)