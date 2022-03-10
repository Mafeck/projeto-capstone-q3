from flask import Blueprint
from app.controllers.comments_controllers import create_comments, update_comments, get_all_comments, get_comment_by_cpf, remove_comment

from app.controllers import processes_controllers, user_clients_controller


bp_clients = Blueprint("clients", __name__, url_prefix="/clients")

bp_clients.get("/<cpf>")(user_clients_controller.get_client)
bp_clients.get("")(user_clients_controller.get_all_clients)
# bp_clients.get("/<int:client_id>/comments")()
# bp_clients.post("/register")()
# bp_clients.post("/login")()
bp_clients.post("/comments")(create_comments)
bp_clients.get("/comments")(get_all_comments)
bp_clients.get("/comments/<cpf>")(get_comment_by_cpf)
# bp_clients.patch("/<int:client_id>")()
bp_clients.post("/register")(user_clients_controller.create_client)
# bp_clients.post("/<int:client_id>/comments")()
bp_clients.patch("/<cpf>")(user_clients_controller.update_client)
bp_clients.patch("/comments/<comment_id>")(update_comments)
# bp_clients.delete("/<int:client_id>")()
bp_clients.delete("/comments/<comment_id>")(remove_comment)

# bp_processes.post("/process")()
# bp_processes.patch("/<int:process_id>")()
# bp_processes.get("/<int:process_id>")()
# bp_processes.get("/process")()
# bp_processes.delete("/<int:process_id>")()
bp_clients.post("/processes")(processes_controllers.create_process)