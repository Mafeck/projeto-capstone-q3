from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify
from osirisvalidator.exceptions import ValidationException

from app.configs.database import db
from app.models.lawyer_model import LawyerModel
from app.models.lawyers_address_model import LawyersAddressModel
from app.models.lawyers_phone_number_model import LawyersPhoneNumber
from app.exc import lawyer_exception

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
        phone_number_to_create = data.pop("phone_number")
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

        for address in list_address:
            if address == address_to_create:
                return jsonify({"error": "Address already exists!"}), HTTPStatus.CONFLICT

        address = LawyersAddressModel(**address_to_create)

        db.session.add(address)
        db.session.commit()

        data["address_id"] = address.id

        lawyer = LawyerModel(**data)

        lawyer.password = password_to_hash

        db.session.add(lawyer)
        db.session.commit()

        all_phone_number = LawyersPhoneNumber.query.all()

        phone_number_list = [phone_number.phone for phone_number in all_phone_number]

        for phone in phone_number_to_create:
            print(phone in phone_number_list)
            if phone not in phone_number_list:
                phone_number = LawyersPhoneNumber(phone=phone, lawyer_oab=oab)

                db.session.add(phone_number)

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
                } for phone_number in phone_number_to_create
            ]
        }), HTTPStatus.CREATED

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST
    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST
    except lawyer_exception.CpfFormatException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST
    # except oab_name_last_name_exception.OabNameLastNameException as e:
    #     return {"error": str(e)}, HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST


def login_user():
    data = request.get_json()

    try:
        email = data['email']
        password = data['password']

        lawyer: LawyerModel = LawyerModel.query.filter_by(email=email).first()

        if not lawyer or not lawyer.verify_password_hash(password):
            return {"error": "email or password not found"}, HTTPStatus.NOT_FOUND

        token = create_access_token(lawyer)

        return jsonify({"access_token": token}), HTTPStatus.OK
    except KeyError as e:
        return {"error": f"Key {e} is missing"}, HTTPStatus.BAD_REQUEST
    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST
