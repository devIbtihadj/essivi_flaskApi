import datetime

from flask import request
from sqlalchemy import and_

from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import commercial_client_bp as commercial_client
from src.application.essivi.models.commande import Commande
from src.application.essivi.models.commercial_client import Commercial_client


@commercial_client.route('/creer/idComm/<int:idComm>/idCli/<int:idCli>', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur, idComm, idCli):
    try:
        commercial_client = Commercial_client(commercial_id=idComm, client_id=idCli)
        return Response.success_response(200, "OK", "Enrégistré avec succès", commercial_client.format()), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


@commercial_client.route('/get/<int:id>', methods=['GET'])
@token_required
def get(current_user, current_utilisateur, id):
    try:
        commercial_client = Commercial_client.query.get(id)
        return Response.success_response(200, "OK", "Récupéré avec succès", commercial_client.format()), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


@commercial_client.route('/change/idComm/<int:idComm>/idCli/<int:idCli>', methods=['PUT'])
@token_required
def change_commercial_for_this_client(current_user, current_utilisateur, idComm, idCli):
    try:
        commercial_client__old = Commercial_client.query.filter \
            (and_(Commercial_client.dateFin is None, Commercial_client.client_id == idCli)).first()
        commercial_client__old.date_fin = datetime.datetime.utcnow()
        commercial_client__old.update()
        commercial_client__new = Commercial_client(commercial_id=idComm, client_id=idCli)
        return Response.success_response(200, "OK", "Récupéré avec succès", commercial_client__new.format()), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500
