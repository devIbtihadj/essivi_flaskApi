from typing import TYPE_CHECKING

from flask import request

from src.application import db
from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required

from sqlalchemy import and_
from src.application.essivi import client_bp as clientCtrl
from src.application.essivi.models.client import Client
from src.application.essivi.models.commande import Commande
from src.application.essivi.services.client import formatClient
from src.application.essivi.services.commande import formatCommande, simpleFormatCommandeWithDetails, \
    simpleFormatCommande


@clientCtrl.route('/creer/comm/<int:id>', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur, id):
    data = request.get_json()
    if (data['nom'] is None or data['prenom'] is None or data['numTel'] is None or data['longitude'] is None or data[
        'latitude'] is None or data[
        'quartier'] is None or
            id is None):
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400
    try:
        client = Client(nom=data['nom'], prenom=data['prenom'], numTel=data['numTel'], longitude=data['longitude'],
                        latitude=data['latitude'],
                        quartier=data['quartier'], commercial_id=id)
        client_id_inserted = client.insert()
        print(client_id_inserted)
        client.id = client_id_inserted
        db.session.commit()
        return Response.success_response(200, "OK", "Affectation effectuée avec succès", formatClient(client.id)), 200
    except Exception as e:
        print(e)
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 400


@clientCtrl.route('/update/comm/<int:id>', methods=['PUT'])
@token_required
def update(current_user, current_utilisateur, id):
    data = request.get_json()
    if (data['id'] is None or data['nom'] is None or data['numTel'] is None or data['prenom'] is None or data[
        'longitude'] is None or data['latitude'] is None or data[
        'quartier'] is None or
            id is None):
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400
    else:
        try:
            client = Client.query.get(data['id'])
            client.nom = data['nom']
            client.prenom = data['prenom']
            client.numTel = data['numTel']
            client.longitude = data['longitude']
            client.latitude = data['latitude']
            client.quartier = data['quartier']
            client.update()
            return Response.success_response(200, "OK", "Modifications effectuées avec succès",  formatClient(client.id)), 200
        except:
            return Response.error_response(500, "Internal server error", "Erreur de serveur"), 400


@clientCtrl.route('/<int:id>/commandes/all', methods=['GET'])
@token_required
def all_commandes_for_this_client(current_user, current_utilisateur, id):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter_by(client_id=id).order_by(Commande.id).all()
            print(commandes)
            commandes_formatted = [formatCommande(cmd.id) for cmd in commandes]
            return Response.success_response(200, "OK", "Liste des commandes du client récupérées avec succès",
                                             commandes_formatted), 200
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


# TODO REVOIR LE DOUBLON

# @client.route('/<int:id>/commandes/all', methods=['GET'])
# @token_required
# def all_commandes_for_this_client(current_user, current_utilisateur, id):
#     if id is None:
#         return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
#     else:
#         try:
#             commandes = Commande.query.filter_by(client_id=id).order_by(Commande.id).all()
#             commandes_formatted = [cmd.format() for cmd in commandes]
#             return Response.success_response(200, "OK", "Liste des commandes du client récupérées avec succès",
#                                              commandes_formatted), 200
#         except:
#             return Response.error_response(500, "Internal server error", "Problème du serveur"), 500
#

@clientCtrl.route('/<int:id>/commandes/notdelivred', methods=['GET'])
@token_required
def all_commandes_for_this_client_but_not_delivred(current_user, current_utilisateur, id):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter(and_(client_id=id, livraison_id=None)).order_by(Commande.id).all()
            print("commandes")
            print(commandes)
            commandes_formatted = [simpleFormatCommande(cmd.id) for cmd in commandes]
            return Response.success_response(200, "OK",
                                             "Liste des commandes non livrées du client récupérées avec succès",
                                             commandes_formatted), 200
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@clientCtrl.route('/commandes/notdelivred', methods=['GET'])
@token_required
def all_commandes_not_delivred(current_user, current_utilisateur):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter_by(livraison_id=None).order_by(Commande.id).all()
            commandes_formatted = [simpleFormatCommandeWithDetails(cmd.id) for cmd in commandes]
            return Response.success_response(200, "OK",
                                             "Liste des commandes non livrées des clients récupérées avec succès",
                                             commandes_formatted), 200
        except Exception as e:
            print(e)
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500



@clientCtrl.route('/commande/<int:id>', methods=['GET'])
@token_required
def getCommande(current_user, current_utilisateur, id):
    return Response.success_response(200, "OK",
                                     "Commande récupérée avec succès",
                                     simpleFormatCommande(id)), 200



@clientCtrl.route('/get/all', methods=['GET'])
@token_required
def all_clients(current_user, current_utilisateur):
    try:
        clients = Client.query.all()
        clients_formatted = [formatClient(client.id) for client in clients]
        return Response.success_response(200, "OK", "Liste récupérée avec succès", clients_formatted), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


@clientCtrl.route('/get/<int:id>/', methods=['GET'])
@token_required
def getClient(current_user, current_utilisateur, id):
    try:
        clients = Client.query.get(id)
        clients_formatted = [formatClient(client.id) for client in clients]
        return Response.success_response(200, "OK", "Liste récupérée avec succès", clients_formatted), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500
