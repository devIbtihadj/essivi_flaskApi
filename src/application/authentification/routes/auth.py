from src.application.Utils.responses import Response
from src.application.authentification import auth_bp as auth
from flask import request, abort, make_response
from src.application.authentification.models.user import User
from src.application.essivi.models.commercial import Commercial


@auth.route('/test', methods=['GET'])
def test():
    print("ok........")


@auth.route('/register', methods=['POST'])
def user_register():
    try:
        data = request.get_json()
        print(data)
        user = User(email=data['email'], password=data['password'])
        user_saved = user.insert()
        commercial = Commercial(nom=data['nom'], prenom=data['prenom'], numTel=data['numTel'],
                                numIdentification=data['numIdentification'], quartier=data['quartier'],
                                nomPersonnePrevenir=data['nomPersonnePrevenir'],
                                prenomPersonnePrevenir=data['prenomPersonnePrevenir'],
                                contactPersonnePrevenir=data['contactPersonnePrevenir'],
                                user_id=user_saved.id
                                )
        commercial.insert()
        return Response.success_response(http_code=201, http_message="Created",
                                         message="Utilisateur enregistré avec succès", data=commercial)
    # TODO SEND THE token
    except Exception as e:
        print(e)
        return Response.error_response(http_code=400, http_message="Bad request",
                                       message="Veuillez préciser tous les champs")
