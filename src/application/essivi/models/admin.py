from src.application.essivi.models.utilisateur import Utilisateur
from src.application.extensions import db


class Admin(Utilisateur):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, db.ForeignKey("utilisateurs.id"), primary_key=True)
    __mapper_args__ = {
        "polymorphic_identity": "admins"
    }
