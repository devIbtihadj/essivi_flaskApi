from flask import request

from src.application import db
from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import livraison_bp as livraisonCtrl
from src.application.essivi.models.commande import Commande
from src.application.essivi.models.livraison import Livraison
from src.application.essivi.services.livraison import simpleFormatLivraison

@livraisonCtrl.route('/creer/idCml/<int:idCml>/idCde/<int:idCde>', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur, idCml, idCde):
    try:
        #data = request.get_json()
        livraison = Livraison(commercial_id=idCml, commande_id=idCde)
        livraison.insert()
        commande = Commande.query.filter_by(id=idCde).first()
        commande.livraison_id = livraison.id
        db.session.commit()
        return Response.success_response(200, "OK", "Livraison enregistrée avec succès",
                                         simpleFormatLivraison(livraison.id)), 200
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Problème"), 400


@livraisonCtrl.route('/get/delivered/<int:id>', methods=['GET'])
@token_required
def getCommercialAllDelivered(current_user, current_utilisateur, id):
    try:
        #data = request.get_json()
        livraisons = Livraison.query.filter_by(commercial_id=id).all()
        livraisons_formatted = [simpleFormatLivraison(livraison.id) for livraison in livraisons]

        return Response.success_response(200, "OK", "Livraison enregistrée avec succès",
                                         livraisons_formatted), 200
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Problème"), 400


