import datetime
import os
from functools import wraps

from dotenv import load_dotenv
from sqlalchemy.exc import PendingRollbackError

from src.application.Utils.responses import Response
from src.application.authentification import auth_bp as auth
from flask import request, abort, make_response, jsonify
from src.application.authentification.models.user import User
from src.application.essivi.models.admin import Admin
#from src.application.essivi.models.commercial import Commercial
from src.application import db, bcrypt
import jwt


from src.application.essivi.models.utilisateur import Utilisateur
from src.application.essivi.models.commercial import Commercial
from src.application.essivi.services.commercial import formatCommercial

load_dotenv()

@auth.route('test', methods=['GET'])
def test():
    return 'OK'

@auth.route('/register', methods=['POST'])
def user_register():
    try:
        data = request.get_json()
        print(data)
        user = User(email=data['email'], password=data['password'])
        inserted_id = user.insert()
        if data['typeUser'] == 'Commercial': 
            commercial = Commercial(nom=data['nom'], prenom=data['prenom'], numTel=data['numTel'],
                                    numIdentification=data['numIdentification'], quartier=data['quartier'],
                                    nomPersonnePrevenir=data['nomPersonnePrevenir'],
                                    prenomPersonnePrevenir=data['prenomPersonnePrevenir'],
                                    contactPersonnePrevenir=data['contactPersonnePrevenir'],
                                    user_id=inserted_id
                                    )
            print(commercial.nom)
            print(commercial.prenom)
            print(commercial.numIdentification)
            print(commercial.quartier)
            print(commercial.nomPersonnePrevenir)
            print(commercial.prenomPersonnePrevenir)
            print(commercial.user_id)

            commercial.insert()
            db.session.commit()
            return Response.success_response(http_code=201, http_message="Created",
                                             message="Commercial enregistré avec succès",
                                             data=formatCommercial(commercial.id)), 201
        else:
            if data['typeUser'] == 'Admin':
                admin = Admin(nom=data['nom'], prenom=data['prenom'], numTel=data['numTel'], user_id=inserted_id)
                admin.insert()
                db.session.commit()
                return Response.success_response(http_code=201, http_message="Created",
                                                 message="Admin enregistré avec succès",
                                                 data=admin.format()), 201
    # TODO SEND THE token
    except PendingRollbackError:
        return Response.error_response(http_code=400, http_message="Bad request",
                                       message="Cette adresse email a déjà été utilisée"), 400

    except Exception as e:
        print(type(e))
        print(e)
        db.session.rollback()
        return Response.error_response(http_code=400, http_message="Bad request",
                                       message="Veuillez préciser tous les champs"), 400


@auth.route('/login', methods=['POST'])
def login():
    try:
        print(request.headers)
        data = request.get_json()
        print(data)
        if not data['email'] or not data['password']:
            return Response.error_response(400, "Bad request", "Veuillez renseigner tous les champs"), 400
        user = User.query.filter_by(email=data['email']).first()
        print(user)
        if not user:
            return Response.error_response(400, "Bad request",
                                           "Aucun utilisateur n'existe avec cette adresse email"), 400
        if bcrypt.check_password_hash(user.password, data['password']):
            utilisateur = Utilisateur.query.filter_by(user_id=user.id).first()
            print(utilisateur)
            token = jwt.encode(
                {
                    'user_id': user.id,
                    'utilisateur_id': utilisateur.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                },
                os.getenv('MY_APP_SECRET_KEY')
            )
            data = {
                'token': token,
                'utilisateur': utilisateur.formatOfIdSimple(utilisateur.id)
            }
            return Response.success_response(200, "OK", "Connexion effectuée avec succès", data), 200
        else:
            return Response.error_response(400, "Bad request", "Mot de passe incorrect"), 400
    except Exception as e :
        print(e)
        return Response.error_response(400, "Bad request", "Mot de passe incorrect"), 400

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            print(token)
        if not token:
            return Response.error_response(401, "Unauthorized", "Veuillez d'abord vous connecter"), 401
        try:
            # PAR DEFAULT ICI, C'est l'algo HS256 qui est utilisé... La vérification a été faite en lisant la
            # fonction encode.
            data = jwt.decode(token, os.getenv('MY_APP_SECRET_KEY'), algorithms="HS256")

            current_user = User.query.filter_by(id=data['user_id']).first()
            current_utilisateur = Utilisateur.query.filter_by(id=data['utilisateur_id']).first()
        except Exception as e:
            print(e)
            return Response.error_response(401, "Unauthorized", "Token invalid!"), 401
        return f(current_user, current_utilisateur, *args, **kwargs)

    return decorated


@auth.route('/update', methods=['PUT'])
@token_required
def change_password(current_user, current_utilisateur):
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        return Response.error_response(400, "Bad request", "Email non valide"), 400
    else:
        user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        utilisateur = Utilisateur.query.filter_by(user_id=user.id).first()
        db.session.commit()
        return Response.success_response(200, "OK", "Mot de passe mis à jour avec succès", utilisateur.format()), 200


# TODO DISABLE ACCOUNT

@auth.route('/me/<int:id>', methods=['POST'])
@token_required
def me(current_user, current_utilisateur, id):
    utilisateur = Utilisateur.query.filter_by(id=id).first()
    print(utilisateur)
    return Response.success_response(200, "OK", "Informations de l'utilisateur", utilisateur.format()), 200