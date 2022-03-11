from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

from app.configs.database import db
from app.models.lawyers_address_model import LawyersAddressModel
from app.models.client_processes_model import ClientProcessesModel

from http import HTTPStatus


def create_process():
    data = request.get_json()

    try:
        process_number = data['number']

        all_proccess = ClientProcessesModel.query.all()


        # if process_number not in all_proccess:
        #     proccess = ProcessesModel(process_number)

        # db.session.add(proccess)
        # db.session.commit()

        # data["id"] = proccess.id

        # db.session.add(data)

        # db.session.commit()

        return jsonify({"msg":
            data
        }), HTTPStatus.CREATED

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST

# @jwt_required()
# def get_process():
#     process = ProcessesModel.query.filter_by().first()

#     if not process:
#         return {"error": "Process not found"}, HTTPStatus.NOT_FOUND

#     return jsonify(process), HTTPStatus.OK