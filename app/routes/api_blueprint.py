from flask import Blueprint
from app.routes.route_clients_blueprint import bp_clients


bp_api = Blueprint("api", __name__, url_prefix="/api")

bp_api.register(bp_clients)