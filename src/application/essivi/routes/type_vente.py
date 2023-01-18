from flask import request

from src.application.Utils.responses import Response
from src.application.essivi import type_vente_bp as type_vente
from src.application import db
from src.application.authentification.routes.auth import token_required
from src.application.essivi.models.type_Vente import Type_vente



