from flask import Blueprint
from app.controllers.users_controllers import create_user, login_user


bp_users = Blueprint("users", __name__, url_prefix="/users")
bp_users.post("/register")(create_user)
bp_users.post("/login")(login_user)

# bp_users.patch("/<int:users_id>")()
# bp_users.get("/<int:users_id>")()
# bp_users.delete("/<int:user_id>")()
