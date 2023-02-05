import json

from flask import request

from src.application.Utils.responses import Response
from src.application.essivi import type_vente_bp as type_vente
from src.application import db
from src.application.authentification.routes.auth import token_required
from src.application.essivi.models.type_Vente import Type_vente




@type_vente.route('/creer/<int:idM>', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur, idM):
    try:
        data = request.get_json()
        print(data)


        if not (data.get("image") is None):
            type_vente = Type_vente(libelle_type_vente=data['libelle_type_vente'],
                                prix_unit=data['prix_unit'],
                                qte_composition=data['qte_composition'], marque_id=idM, image=data['image'])
        else:
                type_vente = Type_vente(libelle_type_vente=data['libelle_type_vente'],
                                        prix_unit=data['prix_unit'],
                                        qte_composition=data['qte_composition'], marque_id=idM, image=None)
        type_vente.insert()
        return Response.success_response(200, "OK", "Type de vente enrégistré avec succès", type_vente.format()), 200
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Veuillez remplir tous les champs"), 400


@type_vente.route('/get/all/<int:idM>', methods=['GET'])
@token_required
def get_all(current_user, current_utilisateur, idM):
    try:
        type_ventes = Type_vente.query.filter_by(marque_id=idM).order_by(Type_vente.id).all()
        type_vente_formatted = [type_vente.format() for type_vente in type_ventes]
        return Response.success_response(200, "OK", "Liste des types de vente récupérée avec succès", type_vente_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Problème du serveur"), 500

