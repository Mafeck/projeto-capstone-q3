from flask import Blueprint
from app.controllers.comments_controllers import create_comments


bp_clients = Blueprint("clients", __name__, url_prefix="/clients")

# bp_clients.get("")()
# bp_clients.get("/<int:client_id>")()
# bp_clients.get("/<int:client_id>/comments")()
# bp_clients.post("/register")()
# bp_clients.post("/login")()
bp_clients.post("/comments")(create_comments)
# bp_clients.patch("/<int:client_id>")()
# bp_clients.patch("/<int:client_id>/comments")()
# bp_clients.delete("/<int:client_id>")()
# bp_clients.delete("/<int:client_id>/comments")()
# bp_clients.post("/process")()
# bp_clients.patch("/<int:process_id>")()
# bp_clients.get("/<int:process_id>")()
# bp_clients.get("/process")()
# bp_clients.delete("/<int:process_id>")()
