from flask import request, jsonify
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.configs.database import db
from osirisvalidator.exceptions import ValidationException
from app.models.client_model import ClientModel

@jwt_required()
def update_client():
    client_data = request.get_json()
    logged_client = get_jwt_identity()
    try:
        client_to_update = ClientModel.query.filter_by(email=logged_client["email"]).first()
        for key, value in client_data.items():
            setattr(client_to_update, key, value)
        db.session.add(client_to_update)
        db.session.commit()
        return jsonify(client_to_update), HTTPStatus.OK
    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST

@jwt_required()
def get_client():
    client = get_jwt_identity()
    if not client:
        return {"error": "Client not found"}, HTTPStatus.NOT_FOUND
    return jsonify(client), HTTPStatus.OK

@jwt_required()
def remove_client():
    logged_client = get_jwt_identity()
    client_to_delete = ClientModel.query.filter_by(email=logged_client["email"]).first()
    name = client_to_delete.name
    db.session.delete(client_to_delete)
    db.session.commit()
    return {"message": f"Client {name} has been deleted"}, HTTPStatus.OK

@jwt_required()
def get_all_clients():
    clients = ClientModel.query.all()
    return jsonify({"clients": [*clients]}), HTTPStatus.OK

def create_client():
    pass