from flask import request

from src.application import db
from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import livraison_bp as livraison
from src.application.essivi.models.livraison import Livraison
#from src.application.essivi.models.commande import Commande
from sqlalchemy import and_

from src.application.essivi.models.payement import Payement


@livraison.route('/creer/idCml/<int:idCml>/idCde/<int:idCde>', methods=['POST'])
@token_required
def creer(current_user, current_utilisateur, idCml, idCde):
    data = request.get_json()
    livraison = Livraison(commercial_deliver_id=idCml, commande_id=idCde)
    inserted_id = livraison.insert()
    if data['montant'] is None:
        pass
    else:
        payement = Payement(montant=data['montant'], commercial_id=idCml, livraison_id=inserted_id)
        payement.insert()
    db.session.commit()
    return Response.success_response(200, "OK", "Livraison enregistrée avec succès", livraison.format()), 200