from flask import Blueprint
from app.controllers.comments_controllers import create_comments, update_comments

from app.controllers import user_clients_controller
from app.routes.processes_blueprint import bp_processes


bp_clients = Blueprint("clients", __name__, url_prefix="/clients")
bp_clients.register_blueprint(bp_processes)


bp_clients.get("/<cpf>")(user_clients_controller.get_client)
bp_clients.get("")(user_clients_controller.get_all_clients)
# bp_clients.get("/<int:client_id>/comments")()
# bp_clients.post("/register")()
# bp_clients.post("/login")()
bp_clients.post("/comments")(create_comments)
# bp_clients.patch("/<int:client_id>")()
bp_clients.post("/register")(user_clients_controller.create_client)
# bp_clients.post("/<int:client_id>/comments")()
bp_clients.patch("/<cpf>")(user_clients_controller.update_client)
bp_clients.patch("/comments/<id>")(update_comments)
# bp_clients.delete("/<int:client_id>")()
# bp_clients.delete("/<int:client_id>/comments")()
