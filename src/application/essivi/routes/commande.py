from __future__ import annotations

from flask import request

from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import commande_bp as commandeCtrl
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
from src.application.essivi.models.commande import Commande as CommandeModel
from src.application.essivi.models.detail_Cde import Detail_cde
from src.application.essivi.services.commande import formatCommande, simpleFormatCommande
from src.application.essivi.services.livraison2 import formatLivraison
from src.application.extensions import db

@commandeCtrl.route('/creer', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur):
    try:
        data = request.get_json()
        print(data)

        comamnde = CommandeModel(date_voulu_reception=data['date_voulu_reception'], client_id=data['client_id'])

        commande_inserted_id = comamnde.insert()

        print("inserted id")
        print(commande_inserted_id)
        print(comamnde)

        for i in range (len(data['details_commandes'])):
            detail = Detail_cde(qte=data['details_commandes'][i]['qte'], commande_id=commande_inserted_id,
                                type_vente_id=data['details_commandes'][i]['type_vente_id'])

            print("-------")
            print(detail)
            detail.insert()

        print("******")
        db.session.commit()
        return Response.success_response(200, "OK", "Commande enrégistrée avec succès", formatCommande(commande_inserted_id)), 200
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Veuillez remplir tous les champs"), 400






@commandeCtrl.route('/delivered/all', methods=['GET'])
@token_required
def allLivraisons(current_user, current_utilisateur):
    try:
        commandes = CommandeModel.query.all()
        commandes_concerned = [commande for commande in commandes if
                                commande.livraison_id is not None]
        livraisons_formatted = [formatLivraison(commande.livraison_id) for commande in commandes_concerned]
        return Response.success_response(200, "OK", "Liste des livraisons récupérée avec succès", livraisons_formatted)
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Problème"), 400



@commandeCtrl.route('/notdelivered/all', methods=['GET'])
@token_required
def allLivraisonsNotDone(current_user, current_utilisateur):
    try:
        # TODO HERE MY INSERT ----- ORDER BY
        commandes = CommandeModel.query.order_by(CommandeModel.id.desc()).all()
        commandes_concerned = [commande for commande in commandes if
                                commande.livraison_id is None]
        commandes_formatted = [formatCommande(commande.id) for commande in commandes_concerned]
        return Response.success_response(200, "OK", "Liste des commandes récupérée avec succès", commandes_formatted)
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Problème"), 400














# @commande.route('/<int:idCom>/all', methods=['GET'])
# @token_required
# def allLivraisonsDoneByCommercial(current_user, current_utilisateur, idCom):
#     try:
#         commercial = Commercial.query.find_by(id=idCom).all()
#         commandes = Commande.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
#         livraisons_formatted = [livraison.format() for livraison in livraisons]