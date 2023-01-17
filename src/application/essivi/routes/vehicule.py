from flask import request

from src.application.Utils.responses import Response
from src.application.essivi import vehicule_bp as vehicule
from src.application import db
from src.application.authentification.routes.auth import token_required
from src.application.essivi.models.vehicule import Vehicule



@vehicule.route('/creer', methods=['POST'])
@token_required
def create(current_user, current_utilisateur):
    data = request.get_json()
    try:
        vehicule = Vehicule(immatriculation=data['immatriculation'], vehicule_vehicule_id=data['vehicule_vehicule_id'])
        vehicule.insert()
        Response.success_response(200, "OK", "vehicule enregistré avec succès", vehicule.format())
    except:
        Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400


@vehicule.route('/update/<int:id>', methods=['PUT'])
@token_required
def update(current_user, current_utilisateur, id):
    data = request.get_json()
    try:
        vehicule = Vehicule.query.filter_by(id=id).first()
        vehicule.immatriculation = data['immatriculation']
        vehicule.type_vehicule_id = data['type_vehicule_id']
        vehicule.update()
        Response.success_response(200, "OK", "vehicule enregistré avec succès", vehicule.format())
    except:
        Response.error_response(400, "Bad request", "Veuillez remplir les champ requis"), 400


@vehicule.route('/get/all', methods=['GET'])
@token_required
def create(current_user, current_utilisateur):
    try:
        vehicules = Vehicule.query.order_by(Vehicule.id).all()
        vehicules_formatted = [vehicule.format() for vehicule in vehicules]
        Response.success_response(200, "OK", "Liste des vehicules récupérée avec succès", vehicules_formatted)
    except:
        Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@vehicule.route('/delete/<int:id>', methods=['DELETE'])
@token_required
def delete(current_user, current_utilisateur, id):
    vehicule = Vehicule.query.get(id)
    if vehicule is not None:
        try:
            vehicule.delete()
        except:
            Response.error_response(500, "Internal server error", "Problème du serveur"), 500
    else:
        Response.error_response(400, "Bad request", "vehicule non existant"), 400
