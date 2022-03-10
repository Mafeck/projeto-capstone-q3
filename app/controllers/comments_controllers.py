from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify
from osirisvalidator.exceptions import ValidationException

from app.configs.database import db
from app.models.lawyers_address_model import LawyersAddressModel
from app.exc import exceptions
from app.models.lawyer_model import LawyerModel
from app.models.lawyers_phone_number_model import LawyersPhoneNumber
from app.models.client_comments_model import ClientCommentsModel


from http import HTTPStatus

#@jwt_required
def create_comments():
    data = request.get_json()

    try:
        comment = data['comment']
        
        comment_to_create = ClientCommentsModel(**data)
      
        db.session.add(comment_to_create)
        db.session.commit()

        return jsonify({"message": comment_to_create}), HTTPStatus.CREATED

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST

"""
#@jwt_required()
def update_comments():
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


#@jwt_required()
def get_comments():
    client = ClientModel.query.filter_by(cpf=cpf).first()

    if not client:
        return {"error": "Client not found"}, HTTPStatus.NOT_FOUND

    return jsonify(client), HTTPStatus.OK



#@jwt_required()
def remove_comments():
    logged_user = get_jwt_identity()

    user_to_delete = LawyerModel.query.filter_by(email=logged_user["email"]).first()
    phone_to_delete = LawyersPhoneNumber.query.filter_by(lawyer_oab=logged_user['oab']).all()
    address_to_delete = LawyersAddressModel.query.filter_by(id=user_to_delete.address_id).first()
   
    for phone in phone_to_delete:
        db.session.delete(phone)    
        db.session.commit()

    db.session.delete(user_to_delete)
    db.session.commit()

    db.session.delete(address_to_delete)
    db.session.commit()

    return {"message": f"User {logged_user['name']} has been deleted"}, HTTPStatus.OK

"""