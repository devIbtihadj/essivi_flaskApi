from flask import Blueprint, request, jsonify, abort
from datetime import date
from ..models.utilisateur import Utilisateur

utilisateur_bp = Blueprint("utilisateur_bp", __name__, url_prefix='/user')