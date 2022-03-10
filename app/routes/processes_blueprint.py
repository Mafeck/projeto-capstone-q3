from flask import Blueprint
from app.controllers import processes_controllers 


bp_processes = Blueprint("processes", __name__, url_prefix="/processes")

# bp_processes.post("/process")()
# bp_processes.patch("/<int:process_id>")()
# bp_processes.get("/<int:process_id>")()
# bp_processes.get("/process")()
# bp_processes.delete("/<int:process_id>")()
bp_processes.post("/processes")(processes_controllers.create_proccess)
