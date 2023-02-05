from __future__ import annotations
from src.application.extensions import db
from src.application.essivi.models.utilisateur import Utilisateur

class Admin(Utilisateur):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, db.ForeignKey("utilisateurs.id"), primary_key=True)
    __mapper_args__ = {
        "polymorphic_identity": "admins"
    }

    def __int__(self, nom, prenom, numTel, user_id):
        Utilisateur.__int__(self, nom, prenom, numTel, user_id)

    def format(self):
        return {
            'id': self.id,
            'prenom': self.prenom,
            'nom': self.nom,
            'numTel': self.numTel

        }

    @staticmethod
    def formatOfIdSimple(id):
        admin = Admin.query.get(id)
        return admin.format()

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            print("admin insert, exception 500 from my server")

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
