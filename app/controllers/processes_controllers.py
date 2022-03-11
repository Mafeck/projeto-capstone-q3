from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

from app.configs.database import db
from app.models.client_model import ClientModel
from app.models.client_processes_model import ClientProcessesModel
from app.models.clients_process_table import clients_processes_table
from app.models.lawyer_model import LawyerModel

from http import HTTPStatus


@jwt_required()
def create_process(client_cpf):
    data = request.get_json()
    keys = ['number', 'description']
    missing_keys = []

    try:
        process_number = data['number']

        process = ClientProcessesModel(**data)

        db.session.add(process)

        for key in keys:
            if key not in data.keys():
                missing_keys.append(key)

        if len(missing_keys) > 0:
            return {'error': f'missing keys: {missing_keys}'}, HTTPStatus.BAD_REQUEST

        client = ClientModel.query.filter_by(cpf=client_cpf).first()

        if not client:
            return {"message": "Client not found"}, HTTPStatus.NOT_FOUND

        client.processes.append(process)

        db.session.commit()

        return jsonify(process), HTTPStatus.CREATED

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return {'error': f'{e}'}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_all_process_by_cpf(client_cpf):
    process = db.session.query(ClientProcessesModel)\
        .select_from(ClientProcessesModel).join(clients_processes_table).filter(client_cpf == client_cpf).all()

    if not process:
        return {"error": "Process not found"}, HTTPStatus.NOT_FOUND

    return jsonify({"processes": process}), HTTPStatus.OK


@jwt_required()
def update_process(number_process): 
    data = request.get_json()

    try:
        description = data['description']

        process_to_update = ClientProcessesModel.query.get(number_process)

        if not process_to_update:
            return jsonify({"message": "Process not found"}), HTTPStatus.NOT_FOUND

        for key, value in data.items():
            setattr(process_to_update, key, value)
            db.session.add(process_to_update)

        db.session.commit()

        return "", HTTPStatus.OK

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return {'error': f'{e}'}, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        return {"error": "You can't change the process number"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_process_by_number():
    args = request.args
    client_cpf = args["client_cpf"]
    number_process = args["number_process"]

    client = ClientModel.query.filter_by(cpf=client_cpf).first()

    if not client:
        return {"error": "Client not found"}, HTTPStatus.NOT_FOUND

    for process in client.processes:
        if process.number == number_process:
            return jsonify(process), HTTPStatus.OK

    return {"error": "Process not found"}, HTTPStatus.NOT_FOUND


@jwt_required()
def delete_process():
    args = request.args

    processes_number = args["processes_number"]
    client_cpf = args["client_cpf"]

    db.session.query(clients_processes_table).filter_by(number=processes_number, client_cpf=client_cpf).delete()

    db.session.commit()

    return "", HTTPStatus.NO_CONTENT


@jwt_required()
def get_all_processes():
    logged_user = get_jwt_identity()

    lawyer = LawyerModel.query.filter_by(oab=logged_user["oab"]).first()

    processes = [client.process for client in lawyer.clients]

    return {"processes": processes}, HTTPStatus.OK
