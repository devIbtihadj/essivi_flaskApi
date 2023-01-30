from flask import request

from src.application.Utils.responses import Response
from src.application.essivi import marque_bp as marque
from src.application import db
from src.application.authentification.routes.auth import token_required
from src.application.essivi.models.marque import Marque


@marque.route('/creer', methods=['POST'])
@token_required
def create(current_user, current_utilisateur):
    data = request.get_json()
    print(data)
    try:
        marque = Marque(libelle_marque=data['libelle_marque'])
        marque.insert()
        return Response.success_response(200, "OK", "Marque enregistrée avec succès", marque.format()), 200
    except:
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400


@marque.route('/update/<int:id>', methods=['PUT'])
@token_required
def update(current_user, current_utilisateur, id):
    data = request.get_json()
    try:
        marque = Marque.query.filter_by(id=id).first()
        marque.libelle_marque = data['libelle_marque']
        marque.update()
        return Response.success_response(200, "OK", "Marque enregistré avec succès", marque.format())
    except:
        return Response.error_response(400, "Bad request", "Veuillez remplir les champ requis"), 400


@marque.route('/get/all', methods=['GET'])
@token_required
def get_all(current_user, current_utilisateur):
    try:
        marques = Marque.query.order_by(Marque.id).all()
        marques_formatted = [marque.format() for marque in marques]
        return Response.success_response(200, "OK", "Liste des types de vehicules récupérée avec succès", marques_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@marque.route('/delete/<int:id>', methods=['DELETE'])
@token_required
def delete(current_user, current_utilisateur, id):
    marque = Marque.query.get(id)
    if id is not None:
        try:
            marque.delete()
            return Response.success_response(200, "OK", "Marque supprimée avec succès", None)
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500
    else:
        return Response.error_response(400, "Bad request", "Type non existant"), 400
