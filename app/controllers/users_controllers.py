from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify
from osirisvalidator.exceptions import ValidationException

from app.configs.database import db
from app.models.lawyers_address_model import LawyersAddressModel
from app.exc import exceptions
from app.models.lawyer_model import LawyerModel
from app.models.lawyers_phone_number_model import LawyersPhoneNumber

from http import HTTPStatus


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
        street = address['street']
        number = address['number']
        state = address['state']
        district = address['district']
        country = address['country']
        cep = address['cep']

        phone_number = data["phone_number"]

        address_to_create = data.pop("address")
        phone_numbers_to_create = data.pop("phone_number")
        password_to_hash = data.pop("password")

        all_address = LawyersAddressModel.query.all()

        list_address = [
            {
                "street": address.street,
                "number": address.number,
                "district": address.district,
                "state": address.state,
                "country": address.country,
                "cep": address.cep
            } for address in all_address
        ]

        if address_to_create not in list_address:
            address = LawyersAddressModel(**address_to_create)

            db.session.add(address)
            db.session.commit()

            data["address_id"] = address.id

        else:
            address = LawyersAddressModel.query.filter_by(
                street=address["street"],
                number=address["number"],
                state=address["state"],
                district=address["district"],
                country=address["country"],
                cep=address["cep"]
            ).first()

            data["address_id"] = address.id

        lawyer = LawyerModel(**data)

        lawyer.password = password_to_hash

        db.session.add(lawyer)

        all_phone_number = LawyersPhoneNumber.query.all()

        phone_number_list = [phone_number.phone for phone_number in all_phone_number]

        for phone in phone_numbers_to_create:
            if phone not in phone_number_list:
                phone_number = LawyersPhoneNumber(phone=phone, lawyer_oab=oab)

                db.session.add(phone_number)

            else:
                return jsonify({"message": "Phone number already exists"}), HTTPStatus.CONFLICT

        db.session.commit()

        return jsonify({
            "oab": lawyer.oab,
            "name": lawyer.name,
            "last_name": lawyer.last_name,
            "email": lawyer.email,
            "address": address,
            "phone_number": [
                {
                    "phone": phone_number
                } for phone_number in phone_numbers_to_create
            ]
        }), HTTPStatus.CREATED

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST

    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST

    except exceptions.CpfFormatException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    except exceptions.OabNameLastNameException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return {'Error': f'{e}'}, HTTPStatus.BAD_REQUEST


def login_user():
    data = request.get_json()

    try:
        email = data['email']
        password = data['password']

        lawyer: LawyerModel = LawyerModel.query.filter_by(email=email).first()

        if not lawyer or not lawyer.verify_password_hash(password):
            return {"error": "email or password not match"}, HTTPStatus.BAD_REQUEST

        token = create_access_token(identity=lawyer)

        return jsonify({"access_token": token}), HTTPStatus.OK

    except KeyError as e:
        return {"error": f"Key {e} is missing"}, HTTPStatus.BAD_REQUEST

    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST


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

    except TypeError as e:
        return {'Error': f'{e}'}, HTTPStatus.BAD_REQUEST


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
    phone_to_delete = LawyersPhoneNumber.query.filter_by(lawyer_oab=logged_user['oab']).all()
   
    for phone in phone_to_delete:
        db.session.delete(phone)    
        db.session.commit()

    db.session.delete(user_to_delete)
    db.session.commit()

    return {"message": f"User {logged_user['name']} has been deleted"}, HTTPStatus.OK
