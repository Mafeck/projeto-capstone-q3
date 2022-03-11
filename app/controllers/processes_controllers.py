from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

from app.configs.database import db
from app.models.lawyers_address_model import LawyersAddressModel
from app.models.processes_model import ProcessesModel

from http import HTTPStatus


def create_process():
    data = request.get_json()

    try:
        process_number = data['number']

        all_proccess = ProcessesModel.query.all()

        proccess = ProcessesModel(**data)
        
        keys = ['number', 'description']

        missing_keys = []

        for key in keys:
            if key not in data.keys():
                missing_keys.append(key)

        if len(missing_keys) > 0:
            return {'error': f'missing keys: {missing_keys}'},HTTPStatus.BAD_REQUEST

        db.session.add(proccess)

        db.session.commit()

        
        
        return jsonify({"msg":
            proccess
            }), HTTPStatus.CREATED

        # db.session.add(proccess)
        # db.session.commit()

        # data["id"] = proccess.id


    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST    

    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST

    except TypeError as e:
        return {'Error': f'{e}'}, HTTPStatus.BAD_REQUEST

# @jwt_required()
def get_all_process():
    process = ProcessesModel.query.all()

    if not process:
        return {"error": "Process not found"}, HTTPStatus.NOT_FOUND

    return jsonify(process), HTTPStatus.OK

#@jwt_required()
def update_process(number_process): 
    data = request.get_json()

    try:
        description = data['description']
        
        process_to_update = ProcessesModel.query.get(number_process)

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
        return {'Error': f'{e}'}, HTTPStatus.BAD_REQUEST   

#@jwt_required()
def get_process_by_number(number_process):
    process = ProcessesModel.query.get(number_process)

    if not process:
        return {"error": "Process not found"}, HTTPStatus.NOT_FOUND

    return jsonify(process), HTTPStatus.OK

#@jwt_required()
def delete_process(number_process):
    process_to_delete = ProcessesModel.query.get(number_process)
    if not process_to_delete:
        return {"error": "Process not found"}, HTTPStatus.NOT_FOUND
    db.session.delete(process_to_delete)
    db.session.commit()

    return {"message": f"Process has been deleted"}, HTTPStatus.OK