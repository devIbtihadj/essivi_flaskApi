from flask import Blueprint

type_vehicule_bp = Blueprint("type_vehicule_bp", __name__, url_prefix='/type_vehicule')

vehicule_bp = Blueprint("vehicule_bp", __name__, url_prefix='/vehicule')

occupation_bp = Blueprint("occupation_bp", __name__, url_prefix='/occupation')

client_bp = Blueprint("client_bp", __name__, url_prefix='/client')

# emballage_bp = Blueprint("emballage_bp", __name__, url_prefix='/emballage')

marque_bp = Blueprint("marque_bp", __name__, url_prefix='/marque')

livraison_bp = Blueprint("livraison_bp", __name__, url_prefix='/livraison')

payement_bp = Blueprint("payement_bp", __name__, url_prefix='/payement')

type_vente_bp = Blueprint("type_vente_bp", __name__, url_prefix='/type_vente')

commande_bp = Blueprint("commande_bp", __name__, url_prefix='/commande')