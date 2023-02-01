import os

from flask import request

from src.application.Utils.responses import Response
from src.application.essivi import type_vehicule_bp as type_v
from src.application import db
from src.application.authentification.routes.auth import token_required
from src.application.essivi.models.type_Vehicule import Type_Vehicule
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@type_v.route('/creer', methods=['POST'])
@token_required
def create(current_user, current_utilisateur):
    print(request)
    print(request.files['image'])
    print(request.form['libelle_type'])

    try:
        file = request.files['image']
        print(file)
        print('------')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('filename '+filename)
            file.save(os.path.join(os.getenv('UPLOAD_FOLDER'), filename))
            type = Type_Vehicule(libelle_type=request.form['libelle_type'], image=(os.path.join(os.getenv('UPLOAD_FOLDER'), filename)))
            type.insert()
            return Response.success_response(200, "OK", "Type de vehicule enregistré avec succès", type.format())
        else:
            return Response.error_response(400, "Bad request", "EAssurez-vous du type de fichier"), 400
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400


@type_v.route('/update/<int:id>', methods=['PUT'])
@token_required
def update(current_user, current_utilisateur, id):
    print(request)
    print(request.files['image'])
    print(request.form['libelle_type'])
    type = Type_Vehicule.query.filter_by(id=id).first()
    try:
        file = request.files['image']
        print(file)
        print('------')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('filename ' + filename)
            type.libelle_type = request.form['libelle_type']
            file.save(os.path.join(os.getenv('UPLOAD_FOLDER'), filename))
            type.image = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            type.update()
            return Response.success_response(200, "OK", "Type de vehicule mis à jour avec succès", type.format())
        else:
            return Response.error_response(400, "Bad request", "Assurez-vous du type de fichier"), 400
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400

@type_v.route('/get/all', methods=['GET'])
@token_required
def get_all(current_user, current_utilisateur):
    try:
        types = Type_Vehicule.query.order_by(Type_Vehicule.id).all()
        types_formatted = [type.format() for type in types]
        return Response.success_response(200, "OK", "Liste des types de vehicules récupérée avec succès",
                                         types_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@type_v.route('/delete/<int:id>', methods=['DELETE'])
@token_required
def delete(current_user, current_utilisateur, id):
    type = Type_Vehicule.query.get(id)
    if type is not None:
        try:
            type.delete()
            return Response.success_response(200, "OK", "Type de véhicule supprimé avec succès", None)
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500
    else:
        return Response.error_response(400, "Bad request", "Type non existant"), 400
