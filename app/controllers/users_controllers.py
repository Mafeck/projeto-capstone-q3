from flask import request, jsonify
from http import HTTPStatus
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from osirisvalidator.exceptions import ValidationException

from app.configs.database import db
from app.models.lawyer_model import LawyerModel
from app.models.lawyers_address_model import LawyersAddressModel
from app.models.lawyers_phone_number_model import LawyersPhoneNumber
from app.exc import lawyer_exception, oab_name_last_name_exception

def create_user():
    data = request.get_json()

    try:
        oab = data['oab']
        name = data['name']
        last_name = data['last_name']
        cpf = data['cpf']
        email = data['email']
        password = data['password']
        address = data['address']
        
        address_to_create = data.pop('address')
        password_to_hash = data.pop('password')
       #print(address_to_create.items())

        #address = LawyersAddressModel(address_to_create)
        #session.add(address)

        lawyer = LawyerModel(**data)
        
        lawyer.password = password_to_hash
        

        db.session.add(lawyer)
        db.session.commit()

        return jsonify(lawyer), HTTPStatus.OK

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST
    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST
    except lawyer_exception.CpfFormatException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST
    except oab_name_last_name_exception.OabNameLastNameException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return {"error": "E-mail already exists"}, HTTPStatus.CONFLICT


def login_user():
    data = request.get_json()

    try:
        email = data['email']
        password = data['password']

        lawyer: LawyerModel = LawyerModel.query.filter_by(email=email).first()

        if not lawyer:
            return {"error": "email not found"}, HTTPStatus.NOT_FOUND
        
        if not lawyer.verify_password_hash(password):
            return {"error": "email and password missmatch"}, HTTPStatus.UNAUTHORIZED
        
        token = create_access_token(lawyer)

        return {"access_token": token}, HTTPStatus.OK
    except KeyError as e:
        return {"error": f"Key {e} is missing"}, HTTPStatus.BAD_REQUEST
    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST