from flask import Blueprint

from app.controllers import processes_controllers


bp_processes = Blueprint("process", __name__, url_prefix="/processes")

bp_processes.post("/<client_cpf>")(processes_controllers.create_process)
bp_processes.get("/<client_cpf>")(processes_controllers.get_all_process_by_cpf)
bp_processes.get("")(processes_controllers.get_process_by_number)
bp_processes.get("/")(processes_controllers.get_all_processes)
bp_processes.patch("/<number_process>")(processes_controllers.update_process)
bp_processes.delete("")(processes_controllers.delete_process)
