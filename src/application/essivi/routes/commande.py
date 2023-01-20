from flask import request

from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import commande_bp as commande
from src.application.essivi.models.commande import Commande


@commande.route('/creer/<int:idC>', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur, idC):
    try:
        data = request.get_json()
        comamnde = Commande(date_voulu_reception=data['date_voulu_reception'])
        comamnde.insert()
        Response.success_response(200, "OK", "Commande enrégistrée avec succès", comamnde.format()), 200
    except:
        Response.error_response(400, "Bad request", "Veuillez remplir tous les champs"), 400
