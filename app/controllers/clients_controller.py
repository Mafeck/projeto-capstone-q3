from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from osirisvalidator.exceptions import ValidationException

from app.models.client_address_model import ClientAddressModel
from app.models.client_model import ClientModel
from app.models.clients_phone_number_model import ClientsPhoneModel
from app.models.clients_comments_table import clients_comments_table
from app.models.clients_process_table import clients_processes_table
from app.configs.database import db
from app.exc import exceptions
from app.models.lawyer_model import LawyerModel
from app.models.lawyers_clients_table import lawyers_clients_table

from http import HTTPStatus


@jwt_required()
def update_client(cpf):
    client_data = request.get_json()

    try:
        client_to_update = ClientModel.query.filter_by(cpf=cpf).first()

        if not client_to_update:
            return jsonify({"message": "Client not found"}), HTTPStatus.NOT_FOUND

        for key, value in client_data.items():
            setattr(client_to_update, key, value)

        db.session.add(client_to_update)
        db.session.commit()

        return jsonify(client_to_update), HTTPStatus.OK

    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST

    except exceptions.CpfFormatException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    except exceptions.TypeException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return {'Error': f'{e}'}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_client(cpf):
    client = ClientModel.query.filter_by(cpf=cpf).first()

    if not client:
        return {"error": "Client not found"}, HTTPStatus.NOT_FOUND

    return jsonify(client), HTTPStatus.OK


@jwt_required()
def get_all_clients():
    logged_user = get_jwt_identity()

    lawyer = LawyerModel.query.filter_by(oab=logged_user["oab"]).first()

    return jsonify({"clients": [*lawyer.clients]}), HTTPStatus.OK


@jwt_required()
def remove_client(client_cpf):
    client = ClientModel.query.filter_by(cpf=client_cpf).first()
    phone_numbers = ClientsPhoneModel.query.filter_by(client_cpf=client_cpf).all()

    # for phone in phone_numbers:
    #     db.session.delete(phone)
    #     db.session.commit()

    comments = client.comments
    processes = client.processes
    print(processes)

    # for comment in comments:
    #     db.query(clients_comments_table).filter_by(comment_id=comment.id, client_cpf=client_cpf).delete()
    #
    # for process in processes:
    #     db.query(clients_processes_table).filter_by(process_number=process.number, client_cpf=client_cpf).delete()

    # db.session.delete(client)
    # db.session.commit()

    return "", HTTPStatus.NO_CONTENT


@jwt_required()
def create_client():
    data = request.get_json()
    logged_user = get_jwt_identity()

    try:
        cpf = data["cpf"]
        name = data["name"]
        last_name = data["last_name"]
        email = data["email"]
        marital_status = data["marital_status"]
        password = data["password"]

        address = data["address"]
        street = address["street"]
        number = address["number"]
        district = address["district"]
        state = address["state"]
        country = address["country"]
        cep = address["cep"]

        phone_number = data["phone_number"]
        phone = data["phone_number"]

        password_to_hash = data.pop("password")
        address_to_create = data.pop("address")
        phone_numbers_to_create = data.pop("phone_number")

        all_address = ClientAddressModel.query.all()

        all_address = [
            {
                "street": address.street,
                "number": address.number,
                "state": address.state,
                "district": address.district,
                "country": address.country,
                "cep": address.cep,
            } for address in all_address
        ]

        if address_to_create not in all_address:
            address = ClientAddressModel(**address_to_create)

            db.session.add(address)
            db.session.commit()

            data["address_id"] = address.id

        else:
            address = ClientAddressModel.query.filter_by(
                street=address["street"],
                number=address["number"],
                state=address["state"],
                district=address["district"],
                country=address["country"],
                cep=address["cep"]
            ).first()

            data["address_id"] = address.id

        lawyer = LawyerModel.query.filter_by(email=logged_user["email"]).first()

        client = ClientModel(**data)

        client.password = password_to_hash

        client.lawyers.append(lawyer)
        db.session.add(client)

        all_phone_number = ClientsPhoneModel.query.all()

        phone_number_list = [phone_number.phone for phone_number in all_phone_number]

        for phone in phone_numbers_to_create:
            if phone not in phone_number_list:
                phone = ClientsPhoneModel(phone=phone, client_cpf=cpf)

                db.session.add(phone)
            else:
                return jsonify({"message": "Phone number already exists."}), HTTPStatus.CONFLICT

        db.session.commit()

        return jsonify({
            "cpf": client.cpf,
            "name": client.name,
            "last_name": client.last_name,
            "email": client.email,
            "marital_status": client.marital_status,
            "address": address
        }), HTTPStatus.CREATED

    except KeyError as e:
        return jsonify({"error": f"Key {e} is missing."}), HTTPStatus.BAD_REQUEST

    except ValidationException:
        return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST

    except exceptions.CpfFormatException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    except exceptions.TypeException as e:
        return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return {'Error': f'{e}'}, HTTPStatus.BAD_REQUEST
