from flask import Blueprint

from app.controllers import processes_controllers


bp_processes = Blueprint("process", __name__, url_prefix="/processes")

bp_processes.post("")(processes_controllers.create_process)
bp_processes.get("")(processes_controllers.get_all_process)
bp_processes.get("/<number_process>")(processes_controllers.get_process_by_number)
bp_processes.patch("/<number_process>")(processes_controllers.update_process)
bp_processes.delete("/<number_process>")(processes_controllers.delete_process)
