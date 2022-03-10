from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

from app.configs.database import db
from app.models.lawyers_address_model import LawyersAddressModel
from app.models.proccesses_model import ProcessesModel

from http import HTTPStatus


def create_proccess():
    data = request.get_json()

    try:
        proccess_number = data['number']

        all_proccess = ProcessesModel.query.all()


        if proccess_number not in all_proccess:
            proccess = ProcessesModel(**proccess_number)

            db.session.add(proccess)
            db.session.commit()

            data["id"] = proccess.id

        else:
            proccess = LawyersAddressModel.query.filter_by(
                number=proccess["number"]
            ).first()

            data["id"] = proccess.id


        db.session.add(data)

        db.session.commit()

        return jsonify({
            data
        }), HTTPStatus.CREATED

    # except KeyError as e:
    #     return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST

    # except ValidationException:
    #     return jsonify({"error": "email key must be an email type like 'person@client.com'"}), HTTPStatus.BAD_REQUEST

    # except lawyer_exception.CpfFormatException as e:
    #     return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    # except lawyer_exception.OabNameLastNameException as e:
    #     return {"error": str(e)}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "Something went wrong"}, HTTPStatus.BAD_REQUEST
