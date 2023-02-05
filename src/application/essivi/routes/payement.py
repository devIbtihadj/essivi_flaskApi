from flask import request

from src.application import db
from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import payement_bp as payementCtrl

from src.application.essivi.models.payement import Payement


@payementCtrl.route('/creer/idCml/<int:idCml>/idLivr/<int:idLivr>', methods=['POST'])
@token_required
def effectuer(current_user, current_utilisateur, idCml, idLivr):
    data = request.get_json()
    payement = Payement(montant=data['montant'], commercial_id=idCml, livraison_id=idLivr)
    payement.insert()
    db.session.commit()
    return Response.success_response(200, "OK", "Payement enregistré avec succès", payement.format()), 200

