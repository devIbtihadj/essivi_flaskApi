# from flask import request
#
# from src.application.Utils.responses import Response
# from src.application.essivi import emballage_bp as emballage
# from src.application import db
# from src.application.authentification.routes.auth import token_required
# from src.application.essivi.models.emballage import Emballage
#
#
# @emballage.route('/creer', methods=['POST'])
# @token_required
# def create(current_user, current_utilisateur):
#     data = request.get_json()
#     try:
#         emballage = Emballage(libelle_type=data['libelle_type'], image=data['image'])
#         type.insert()
#         Response.success_response(200, "OK", "Type de vehicule enregistré avec succès", type.format())
#     except:
#         Response.error_response(400, "Bad request", "Veuillez remplir les champs requis"), 400
#
#
# @emballage.route('/update/<int:id>', methods=['PUT'])
# @token_required
# def update(current_user, current_utilisateur, id):
#     data = request.get_json()
#     try:
#         type = Type_Vehicule.query.filter_by(id=id).first()
#         type.libelle_type = data['libelle_type']
#         type.image = data['image']
#         type.update()
#         return Response.success_response(200, "OK", "Type de vehicule enregistré avec succès", type.format())
#     except:
#         return Response.error_response(400, "Bad request", "Veuillez remplir les champ requis"), 400
#
#
# @emballage.route('/get/all', methods=['GET'])
# @token_required
# def create(current_user, current_utilisateur):
#     try:
#         types = Type_Vehicule.query.order_by(Type_Vehicule.id).all()
#         types_formatted = [type.format() for type in types]
#         return Response.success_response(200, "OK", "Liste des types de vehicules récupérée avec succès", types_formatted)
#     except:
#         return Response.error_response(500, "Internal server error", "Problème du serveur"), 500
#
#
# @emballage.route('/delete/<int:id>', methods=['DELETE'])
# @token_required
# def delete(current_user, current_utilisateur, id):
#     type = Type_Vehicule.query.get(id)
#     if type is not None:
#         try:
#             type.delete()
#         except:
#             return Response.error_response(500, "Internal server error", "Problème du serveur"), 500
#     else:
#         return Response.error_response(400, "Bad request", "Type non existant"), 400
