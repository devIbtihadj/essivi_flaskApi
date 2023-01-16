from src.application.essivi.models import type_Vehicule
from src.application.extensions import db


class VoitureService:
    def create_type_voiture(self, type: type_Vehicule):
        db.insert.add(type)
        db.session.commit()
