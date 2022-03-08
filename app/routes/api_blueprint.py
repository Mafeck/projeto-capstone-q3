from flask import Blueprint
<<<<<<< HEAD


bp_api = Blueprint("api", __name__, url_prefix="/api")
=======
from app.routes.route_clients_blueprint import bp_clients
from app.routes.route_users_blueprint import bp_users


bp_api = Blueprint("api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_clients)
bp_api.register_blueprint(bp_users)

>>>>>>> 08faa96d28cbbca3507f3751011bc931e1d12300
