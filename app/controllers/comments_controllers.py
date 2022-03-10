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
from app.models.client_model import ClientModel
from app.models.clients_comments_table import clients_comments_table


from http import HTTPStatus

#@jwt_required
def create_comments():
    data = request.get_json()
    #formato da req no insomnia:
    """
    {
	    "comment": "First comment",
		"clients_cpf": [
		    "000.000.000-29",
		    "000.000.000-28"	
	    ]
    }
    """
    try:
        comment = data['comment']
        clients_cpf = data['clients_cpf'] #lista com cpf de todos os clientes que vão ter o mesmo comentário
        
        clients = data.pop("clients_cpf")
        
        comment_to_create = ClientCommentsModel(**data)

        found_client = ()
        for client in clients: #itero por cada cpf da lista passada na requisição, procuro no banco e adiciono o comentário
            found_client = ClientModel.query.filter_by(cpf=client).first()
            found_client.comments.append(comment_to_create)

        #descomente as linhas abaixo para ver que ta tud funcionando bonitinho    
        #print(comment_to_create.clients)
        #print(found_client.comments)
      
        db.session.add(comment_to_create)
        db.session.commit()
        return jsonify({"message": {
            "comment": comment_to_create.comment,
            "created_at": comment_to_create.create_date,
            "clients": comment_to_create.clients
        }})
        #return jsonify({"message": comment_to_create}), HTTPStatus.CREATED

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST




#@jwt_required()
def update_comments(id): #não dá pra atualizar pelo cpf porque o cliente pode ter vários comentários. Vai ter que ser pelo id do comentário mesmo
    comment_data = request.get_json()

    try:
        comment = comment_data['comment']
        #comment = ClientModel.query.filter_by(cpf=cpf).first()
        #found = clients_comments_table.query.filter_by(client_cpf=cpf)
        comment_to_update = ClientCommentsModel.query.filter_by(id=id).first()
        if not comment_to_update:
            return jsonify({"message": "Comment not found"}), HTTPStatus.NOT_FOUND

        for key, value in comment_data.items():
            setattr(comment_to_update, key, value)
        
        #seria legal colocar o updated_at mesmo pra sinalizar a data da última atualização 
        db.session.add(comment_to_update)
        db.session.commit()
        
        return "", HTTPStatus.OK #segundo o canvas, quando a atualização é feita, não precisa de body na resposta

    except KeyError as e:
        return {"error": f"Key {e} is missing."}, HTTPStatus.BAD_REQUEST

        
"""
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