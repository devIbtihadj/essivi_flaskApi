from src.application.Utils.responses import Response
from src.application.authentification.routes.auth import token_required
from src.application.essivi import occupation_bp as occupationCtr
from src.application.essivi.models.ocuupation import Occupation
from src.application.essivi.services.occupation import formatOccupation


@occupationCtr.route('/affecter/idV/<int:idV>/idC/<int:idC>', methods=['POST'])
@token_required
def affecter(current_user, current_utilisateur, idV, idC):
    try:
        occupation = Occupation(comercial_id=idC, vehicule_id=idV)
        occupation.insert()
        Response.success_response(200, "OK", "Affectation effectuée avec succès", formatOccupation(occupation.id)), 200
    except:
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400


@occupationCtr.route('/supprimer/<int:id>', methods=['POST'])
@token_required
def supprimer(current_user, current_utilisateur, id):
    try:
        occupation = Occupation.query.get(id)
        occupation.delete()
        return Response.success_response(200, "OK", "Affectation retirée avec succès", formatOccupation(occupation.id)), 200
    except:
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400


@occupationCtr.route('/get/all', methods=['GET'])
@token_required
def affectations_actuelles(current_user, current_utilisateur, id):
    try:
        occupations = Occupation.query.filter_by(Occupation.dateFin is None).order_by(Occupation.id).all()
        occupations_formatted = [formatOccupation(occupation.id) for occupation in occupations]
        return Response.success_response(200, "OK", "Affectation retirée avec succès", occupations_formatted), 200
    except:
        return Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400
