from flask import Blueprint

type_vehicule_bp = Blueprint("type_vehicule_bp", __name__, url_prefix='/type_vehicule')

vehicule_bp = Blueprint("vehicule_bp", __name__, url_prefix='/vehicule')