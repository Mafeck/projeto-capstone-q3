from flask import Blueprint

from app.controllers import processes_controllers


bp_processes = Blueprint("process", __name__, url_prefix="/processes")

# bp_processes.post("")()
# bp_processes.patch("/<int:process_id>")()
# bp_processes.get("/<int:process_id>")()
# bp_processes.get("")()
# bp_processes.delete("/<int:process_id>")()
bp_processes.post("")(processes_controllers.create_process)
