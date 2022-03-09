from flask import Blueprint
from app.routes.route_clients_blueprint import bp_clients
from app.routes.route_users_blueprint import bp_users


bp_api = Blueprint("api", __name__, url_prefix="/api")


bp_api.register_blueprint(bp_clients)
bp_api.register_blueprint(bp_users)
