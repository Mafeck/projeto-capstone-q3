from flask_jwt_extended import jwt_required
from flask import request, jsonify

from app.models.client_comments_model import ClientCommentsModel
from app.models.client_model import ClientModel
from app.models.clients_comments_table import clients_comments_table
from app.configs.database import db

from http import HTTPStatus
from datetime import datetime


@jwt_required()
def create_comments():
    data = request.get_json()

    try:
        comment = data["comment"]
        clients_cpf = data["clients_cpf"]

        clients_cpf_to_append = data.pop("clients_cpf")

        comment_to_create = ClientCommentsModel(**data)

        for cpf in clients_cpf_to_append:
            found_client = ClientModel.query.filter_by(cpf=cpf).first()

            if not found_client:
                return jsonify({"message": f"Client {cpf} not found"}), HTTPStatus.NOT_FOUND

            found_client.comments.append(comment_to_create)

            print(comment_to_create.clients)
            print(found_client.comments)

        db.session.add(comment_to_create)
        db.session.commit()

        return jsonify({"message": {
            "title": comment_to_create.title,
            "comment": comment_to_create.comment,
            "created_at": comment_to_create.create_date,
            "update_at": comment_to_create.update_at
        }})

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST


@jwt_required()
def update_comments(comment_id):
    comment_data = request.get_json()

    try:
        comment = comment_data["comment"]
        
        comments_to_update = ClientCommentsModel.query.filter_by(id=comment_id).all()

        if len(comments_to_update) < 1:
            return jsonify({"message": "Comment not found"}), HTTPStatus.NOT_FOUND

        for comment in comments_to_update:
            for key, value in comment_data.items():
                setattr(comment, key, value)

                comment.update_at = datetime.now()

                db.session.add(comment)

        db.session.commit()
        
        return "", HTTPStatus.OK

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_comments_by_cpf(cpf):
    client = ClientModel.query.filter_by(cpf=cpf).first()

    if not client:
        return {"error": "Client not found"}, HTTPStatus.NOT_FOUND

    return jsonify({"comments": client.comments}), HTTPStatus.OK


@jwt_required()
def get_comment_by_id():
    query_params = request.args

    client_cpf = query_params["client_cpf"]
    comment_id = query_params["comment_id"]

    client = ClientModel.query.filter_by(cpf=client_cpf).first()

    if not client:
        return {"error": "Client not found"}, HTTPStatus.NOT_FOUND

    for comment in client.comments:
        if comment.id == int(comment_id):
            return jsonify(comment), HTTPStatus.OK

    return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND


@jwt_required()
def remove_comment(comment_id):
    client_cpf = request.get_json()["client_cpf"]

    db.session.query(clients_comments_table).filter_by(client_cpf=client_cpf, comment_id=comment_id).delete()

    db.session.commit()

    return "", HTTPStatus.NO_CONTENT
