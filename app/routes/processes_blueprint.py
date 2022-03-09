from flask import Blueprint


bp_processes = Blueprint("processes", __name__, url_prefix="/processes")

# bp_clients.post("/process")()
# bp_clients.patch("/<int:process_id>")()
# bp_clients.get("/<int:process_id>")()
# bp_clients.get("/process")()
# bp_clients.delete("/<int:process_id>")()
