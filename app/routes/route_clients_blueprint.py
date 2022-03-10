from flask import Blueprint
from app.controllers import proccess_controllers 


bp_clients = Blueprint("clients", __name__, url_prefix="/clients")

# bp_clients.get("")()
# bp_clients.get("/<int:client_id>")()
# bp_clients.get("/<int:client_id>/comments")()
# bp_clients.post("/register")()
# bp_clients.post("/login")()
# bp_clients.post("/<int:client_id>/comments")()
# bp_clients.patch("/<int:client_id>")()
# bp_clients.patch("/<int:client_id>/comments")()
# bp_clients.delete("/<int:client_id>")()
# bp_clients.delete("/<int:client_id>/comments")()
bp_clients.post("/proccess")(proccess_controllers.create_proccess)
# bp_clients.patch("/<int:proccess_id>")()
# bp_clients.get("/<int:proccess_id>")()
# bp_clients.get("/proccess")()
# bp_clients.delete("/<int:proccess_id>")()
