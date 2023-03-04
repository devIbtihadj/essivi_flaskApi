from flask import request

from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import commercial_bp as commercialCtrl
from src.application.essivi.models.client import Client
from src.application.essivi.models.commande import Commande
from src.application.essivi.models.commercial import Commercial

from src.application.essivi.models.commercial_client import Commercial_client
from src.application.essivi.models.livraison import Livraison
from src.application.essivi.models.payement import Payement
from src.application.essivi.services.client import formatClient
from src.application.essivi.services.commande import simpleFormatCommandeWithDetails, \
    simpleFormatCommandeWithDetailsForCommercial
from src.application.essivi.services.commercial import formatCommercial
from src.application.essivi.services.livraison2 import formatLivraison


@commercialCtrl.route('/all', methods=['GET'])
@token_required
def allCommercials(current_user, current_utilisateur):
    try:
        commercials = Commercial.query.order_by(Commercial.id).all()
        commercials_formatted = [formatCommercial(commercial.id) for commercial in commercials]
        return Response.success_response(http_code=200, http_message="OK", message="Liste récupérée avec succès",
                                         data=commercials_formatted), 200
    except Exception as e:
        print(e)
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


# @commercial.route('/client/all/<int:idCom>', methods=['GET'])
# @token_required
# def allClientsForCommercial(current_user, current_utilisateur, id):
#     try:
#         commercials_clients = Commercial_client.query.filter_by(commercial_id=id).order_by(Commercial_client.id).all()
#         print(commercials_clients)
#         commercial_client_formatted = [cc.format() for cc in commercials_clients]
#         return Response.success_response(http_code=200, http_message="OK", message="Liste récupérée avec succès",
#                                          data=commercial_client_formatted), 200
#     except:
#         return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500
#

# TODO ALL CLIENTS FOR COMMERCIAL

@commercialCtrl.route('/<int:idCom>/clients/all', methods=['GET'])
@token_required
def allCientsForCommercial(current_user, current_utilisateur, idCom):
    try:
        clients = Client.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
        clients_formatted = [formatClient(client.id) for client in clients]
        return Response.success_response(200, "OK", "Liste des clients récupérée avec succès", clients_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


# @commercial.route('/<int:idCom>/payements/all', methods=['GET'])
# @token_required
# def allPayementsRecievedByCommercial(current_user, current_utilisateur, idCom):
#     try:
#         payements = Payement.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
#         payements_formatted = [formatPayement(payement.id) for payement in payements]
#         return Response.success_response(200, "OK", "Liste des payements récupérée avec succès", payements_formatted)
#     except:
#         return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


@commercialCtrl.route('/<int:idCom>/payements/all', methods=['GET'])
@token_required
def allLivraisonsDoneByCommercial(current_user, current_utilisateur, idCom):
    try:
        livraisons = Livraison.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
        livraisons_formatted = [formatLivraison(livraison.id) for livraison in livraisons]
        return Response.success_response(200, "OK", "Liste des livraisons récupérée avec succès", livraisons_formatted)
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500





# TODO THIS ONE DOES NOT WORK VERRY WELL
@commercialCtrl.route('/<int:idCom>/commandes/notdelivered', methods=['GET'])
@token_required
def all_commandes_not_delivredForCommercial(current_user, current_utilisateur, idCom):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter_by(livraison_id=None).order_by(Commande.id).all()
            clients = Client.query.filter_by(commercial_id=idCom).all()

            print(type(commandes))
            mesCommande = [Commande(id=0)]
            print(len(mesCommande))

            print(mesCommande[0])
            for commande in commandes:
                for client in clients:
                    if (commande.client_id == client.id):
                        mesCommande = mesCommande.append(commande)
            del mesCommande[Commande(id=0)]
            commandes_formatted = [simpleFormatCommandeWithDetails(cmd.id) for cmd in mesCommande]
            return Response.success_response(200, "OK",
                                             "Liste des commandes non livrées des clients récupérées avec succès",
                                             commandes_formatted), 200
        except Exception as e:
            print(e)
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500
