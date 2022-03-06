from flask import request, jsonify
from http import HTTPStatus
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.configs.database import db
from sqlalchemy.exc import IntegrityError
from osirisvalidator.exceptions import ValidationException
from app.models.lawyer_model import LawyerModel
from app.models.lawyers_address_model import LawyersAddressModel
from app.models.lawyers_phone_number_model import LawyersPhoneNumber

@jwt_required()
def update_user():
    user_data = request.get_json()
    logged_user = get_jwt_identity()
    try:
        user_to_update = LawyerModel.query.filter_by(email=logged_user["email"]).first()
        for key, value in user_data.items():
            setattr(user_to_update, key, value)
        db.session.add(user_to_update)
        db.session.commit()
        return jsonify(user_to_update), HTTPStatus.OK
    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST

@jwt_required()
def get_user():
    user = get_jwt_identity()
    if not user:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND
    return jsonify(user), HTTPStatus.OK

@jwt_required()
def remove_user():
    logged_user = get_jwt_identity()
    user_to_delete = LawyerModel.query.filter_by(email=logged_user["email"]).first()
    name = user_to_delete.name
    db.session.delete(user_to_delete)
    db.session.commit()
    return {"message": f"User {name} has been deleted"}, HTTPStatus.OK