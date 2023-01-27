from flask import request

from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import client_bp as client
from src.application.essivi.models.client import Client
from src.application.essivi.models.commande import Commande
from sqlalchemy import and_


@client.route('/creer/comm/<int:id>', methods=['POST'])
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
        client.insert()
        return Response.success_response(200, "OK", "Affectation effectuée avec succès", client.format()), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 400


@client.route('/update/comm/<int:id>', methods=['PUT'])
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
            return Response.success_response(200, "OK", "Modifications effectuées avec succès", client.format()), 200
        except:
            return Response.error_response(500, "Internal server error", "Erreur de serveur"), 400


@client.route('/<int:id>/commandes/all', methods=['GET'])
@token_required
def all_commandes_for_this_client(current_user, current_utilisateur, id):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter_by(client_id=id).order_by(Commande.id).all()
            commandes_formatted = [cmd.format() for cmd in commandes]
            return Response.success_response(200, "OK", "Liste des commandes du client récupérées avec succès",
                                             commandes_formatted), 200
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500

# TODO REVOIR LE DOUBLON

@client.route('/<int:id>/commandes/all', methods=['GET'])
@token_required
def all_commandes_for_this_client(current_user, current_utilisateur, id):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter_by(client_id=id).order_by(Commande.id).all()
            commandes_formatted = [cmd.format() for cmd in commandes]
            return Response.success_response(200, "OK", "Liste des commandes du client récupérées avec succès",
                                             commandes_formatted), 200
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@client.route('/<int:id>/commandes/notdelivred', methods=['GET'])
@token_required
def all_commandes_for_this_client_but_not_delivred(current_user, current_utilisateur, id):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter(and_(client_id=id, livraisons=None)).order_by(Commande.id).all()
            commandes_formatted = [cmd.format() for cmd in commandes]
            return Response.success_response(200, "OK", "Liste des commandes non livrées du client récupérées avec succès",
                                             commandes_formatted), 200
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@client.route('/commandes/notdelivred', methods=['GET'])
@token_required
def all_commandes_not_delivred(current_user, current_utilisateur):
    if id is None:
        return Response.error_response(400, "Bad request", "Précisez l'id du client"), 400
    else:
        try:
            commandes = Commande.query.filter(livraisons=None).order_by(Commande.id).all()
            commandes_formatted = [cmd.format() for cmd in commandes]
            return Response.success_response(200, "OK", "Liste des commandes non livrées du client récupérées avec succès",
                                             commandes_formatted), 200
        except:
            return Response.error_response(500, "Internal server error", "Problème du serveur"), 500


@client.route('/get/all', methods=['GET'])
@token_required
def all_clients(current_user, current_utilisateur):
    try:
        clients = Client.query.all()
        clients_formatted = [client.format() for client in clients]
        return Response.success_response(200, "OK", "Liste récupérée avec succès", clients_formatted), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500


@client.route('/get/<int:id>/', methods=['GET'])
@token_required
def getClient(current_user, current_utilisateur, id):
    try:
        clients = Client.query.get(id)
        clients_formatted = [client.format() for client in clients]
        return Response.success_response(200, "OK", "Liste récupérée avec succès", clients_formatted), 200
    except:
        return Response.error_response(500, "Internal server error", "Erreur de serveur"), 500
