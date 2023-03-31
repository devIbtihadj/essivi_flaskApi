import json
import os

from flask import request

from src.application.Utils.responses import Response
from src.application.essivi import type_vente_bp as type_venteCtrl
from src.application import db
from src.application.authentification.routes.auth import token_required
from src.application.essivi.models.type_Vente import Type_vente
from src.application.essivi.services.type_vente import formatType_Vente
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@type_venteCtrl.route('/creer/<int:idM>', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur, idM):
    global filename
    try:
        print(request)
        print(request.form['prix_unit'])
        # prix_unit = request.form['prix_unit']
        # data = request.get_json()
        # print(data)

        if 'image' in request.files:
            print('----')
            file = request.files['image']
            print(file)
            print('------')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print('filename ' + filename)
                file.save(os.path.join(os.getenv('UPLOAD_FOLDER_FOR_PRODUCTS'), filename))
            print("////////////")
            type_vente = Type_vente(libelle_type_vente=request.form['libelle_type_vente'],
                                    prix_unit=request.form['prix_unit'],
                                    qte_contenu_unitaire=request.form['qte_contenu_unitaire'],
                                    qte_composition=request.form['qte_composition'], marque_id=idM,
                                    image=(os.path.join(os.getenv('PRODUCTS_FILES_FOLDER'), filename)))

        else:
            type_vente = Type_vente(libelle_type_vente=request.form['libelle_type_vente'],
                                    prix_unit=request.form['prix_unit'],
                                    qte_contenu_unitaire=request.form['qte_contenu_unitaire'],
                                    qte_composition=request.form['qte_composition'], marque_id=idM, image=None)
        type_vente.insert()
        return Response.success_response(200, "OK", "Type de vente enrégistré avec succès",
                                         formatType_Vente(type_vente.id)), 200

    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Veuillez remplir tous les champs"), 400


@type_venteCtrl.route('/get/all/<int:idM>', methods=['GET'])
@token_required
def get_allForMarque(current_user, current_utilisateur, idM):
    try:
        type_ventes = Type_vente.query.filter_by(marque_id=idM).order_by(Type_vente.id.desc()).all()
        type_vente_formatted = [formatType_Vente(type_vente.id) for type_vente in type_ventes]
        return Response.success_response(200, "OK", "Liste des types de vente récupérée avec succès", type_vente_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Problème du serveur"), 500



@type_venteCtrl.route('/get/all', methods=['GET'])
@token_required
def get_all(current_user, current_utilisateur):
    try:
        type_ventes = Type_vente.query.order_by(Type_vente.id.desc()).all()
        type_vente_formatted = [formatType_Vente(type_vente.id) for type_vente in type_ventes]
        return Response.success_response(200, "OK", "Liste des types de vente récupérée avec succès", type_vente_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Problème du serveur"), 500



@type_venteCtrl.route('/get/<int:id>', methods=['GET'])
@token_required
def get_one(current_user, current_utilisateur, id):
    try:
        return Response.success_response(200, "OK", "Type de vente récupérée avec succès", formatType_Vente(id))
    except:
        return Response.error_response(500, "Internal server error", "Problème du serveur"), 500

