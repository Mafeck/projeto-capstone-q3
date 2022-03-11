from flask import Blueprint

from app.routes.comments_blueprint import bp_comments
from app.routes.processes_blueprint import bp_processes
from app.controllers import clients_controller


bp_clients = Blueprint("clients", __name__, url_prefix="/clients")

bp_clients.register_blueprint(bp_comments)
bp_clients.register_blueprint(bp_processes)

bp_clients.get("/<cpf>")(clients_controller.get_client)
bp_clients.get("")(clients_controller.get_all_clients)
bp_clients.post("/register")(clients_controller.create_client)
bp_clients.patch("/<cpf>")(clients_controller.update_client)
# bp_clients.delete("/<int:client_id>")()