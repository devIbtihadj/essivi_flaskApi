from flask import request

from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import commercial_bp as commercial
from src.application.essivi.models.client import Client
from src.application.essivi.models.commercial import Commercial
from src.application.essivi.models.commande import Commande
from sqlalchemy import and_

from src.application.essivi.models.livraison import Livraison
from src.application.essivi.models.payement import Payement


@commercial.route('/all', methods=['GET'])
@token_required
def allCommercials(current_user, current_utilisateur):
    try:
        commercials = Commercial.query.order_by(Commercial.id).all()
        commercials_formatted = [commercial.format() for commercial in commercials]
        return Response.success_response(http_code=200, http_message="OK", message="Liste récupérée avec succès",
                                         data=commercials_formatted), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500



@commercial.route('/<int:idCom>/clients/all', methods=['GET'])
@token_required
def allCientsForCommercial(current_user, current_utilisateur, idCom):
        try:
            clients = Client.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
            clients_formatted = [client.format() for client in clients]
            return Response.success_response(200, "OK", "Liste des clients récupérée avec succès", clients_formatted)
        except:
            return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


@commercial.route('/<int:idCom>/payements/all', methods=['GET'])
@token_required
def allPayementsRecievedByCommercial(current_user, current_utilisateur, idCom):
    try:
        payements = Payement.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
        payements_formatted = [payement.format() for payement in payements]
        return Response.success_response(200, "OK", "Liste des payements récupérée avec succès", payements_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


@commercial.route('/<int:idCom>/payements/all', methods=['GET'])
@token_required
def allLivraisonsDoneByCommercial(current_user, current_utilisateur, idCom):
    try:
        livraisons = Livraison.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
        livraisons_formatted = [livraison.format() for livraison in livraisons]
        return Response.success_response(200, "OK", "Liste des livraisons récupérée avec succès", livraisons_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500

