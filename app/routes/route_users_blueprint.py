from flask import Blueprint


bp_users = Blueprint("users", __name__, url_prefix="/users")

bp_users.post("/register")()
bp_users.post("/login")()
bp_users.patch("/<int:users_id>")()
bp_users.get("/<int:users_id>")()
bp_users.delete("/<int:user_id>")()