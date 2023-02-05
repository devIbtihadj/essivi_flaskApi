from flask import request

from src.application.Utils.responses import Response
from src.application.essivi import vehicule_bp as vehicule
from src.application import db
from src.application.authentification.routes.auth import token_required
from src.application.essivi.models.vehicule import Vehicule
from src.application.essivi.services.vehicule import formatVehicule


@vehicule.route('/creer', methods=['POST'])
@token_required
def create(current_user, current_utilisateur):
    data = request.get_json()
    print(data)
    try:
        vehicule = Vehicule(immatriculation=data['immatriculation'], type_vehicule_id=data['type_vehicule_id'])
        vehicule.insert()
        return Response.success_response(200, "OK", "vehicule enregistré avec succès", formatVehicule(vehicule.id))
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400


@vehicule.route('/update/<int:id>', methods=['PUT'])
@token_required
def update(current_user, current_utilisateur, id):
    data = request.get_json()
    try:
        vehicule = Vehicule.query.filter_by(id=id).first()
        vehicule.immatriculation = data['immatriculation']
        vehicule.type_vehicule_id = data['type_vehicule_id']
        vehicule.update()
        return Response.success_response(200, "OK", "vehicule enregistré avec succès", formatVehicule(vehicule.id))
    except:
        return Response.error_response(400, "Bad request", "Veuillez remplir les champ requis"), 400


@vehicule.route('/get/all', methods=['GET'])
@token_required
def all(current_user, current_utilisateur):
    try:
        vehicules = Vehicule.query.order_by(Vehicule.id).all()
        vehicules_formatted = [formatVehicule(vehicule.id) for vehicule in vehicules]
        return Response.success_response(200, "OK", "Liste des vehicules récupérée avec succès", vehicules_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@vehicule.route('/delete/<int:id>', methods=['DELETE'])
@token_required
def delete(current_user, current_utilisateur, id):
    vehicule = Vehicule.query.get(id)
    if vehicule is not None:
        try:
            vehicule.delete()
            return Response.success_response(200, "OK", "Véhicule supprimé avec succès", None)
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500
    else:
        return Response.error_response(400, "Bad request", "vehicule non existant"), 400
