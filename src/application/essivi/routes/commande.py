from __future__ import annotations

from flask import request

from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import commande_bp as commande
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
from src.application.essivi.models.commande import Commande
from src.application.essivi.models.detail_Cde import Detail_cde
from src.application.extensions import db

@commande.route('/creer', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur):
    try:
        data = request.get_json()
        print(data)

        comamnde = Commande(date_voulu_reception=data['date_voulu_reception'], client_id=data['client_id'])

        commande_inserted_id = comamnde.insert()

        print(comamnde)

        for i in range (len(data['details_commandes'])):
            detail = Detail_cde(qte=data['details_commandes'][i]['qte'], commande_id=commande_inserted_id,
                                type_vente_id=data['details_commandes'][i]['type_vente_id'])



            print(detail)
            detail.insert()

        db.session.commit()
        return Response.success_response(200, "OK", "Commande enrégistrée avec succès", comamnde.format()), 200
    except Exception as e:
        print(e)
        return Response.error_response(400, "Bad request", "Veuillez remplir tous les champs"), 400


# @commande.route('/<int:idCom>/all', methods=['GET'])
# @token_required
# def allLivraisonsDoneByCommercial(current_user, current_utilisateur, idCom):
#     try:
#         commercial = Commercial.query.find_by(id=idCom).all()
#         commandes = Commande.query.filter_by(commercial_id=idCom).order_by(Client.id.desc()).all()
#         livraisons_formatted = [livraison.format() for livraison in livraisons]