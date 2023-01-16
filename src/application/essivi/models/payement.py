from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application.essivi.models.commercial import Commercial
    from src.application.essivi.models.livraison import Livraison
from src.application.extensions import db


class Payement(db.Model):
    __tablename__ = 'payements'
    id = db.Column(db.Integer, primary_key=True)
    montant = db.Column(db.Integer(), nullable=False)
    date_heure = db.Column(db.DateTime(), default=datetime.utcnow)

    livraison_id = db.Column(db.Integer, db.ForeignKey('livraisons.id'), nullable=False)
    commercial_id = db.Column(db.Integer, db.ForeignKey('commercials.id'), nullable=False)

    def __init__(self, montant, livraison_id, commercial_id):
        self.montant = montant
        self.livraison_id = livraison_id
        self.commercial_id = commercial_id

    def format(self):
        return {
            'id': self.id,
            'montant': self.montant,
            'date_heure': self.date_heure,
            'livraison': Livraison.formatOfId(self.livraison_id),
            'commercial': Commercial.formatOfId(self.commercial_id)
        }

    @staticmethod
    def formatOfId(id):
        payement = Payement.query.get(id)
        return payement.format()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def exists(id):
        payement = Payement.query.get(id)
        return payement if payement is not None else False

    @staticmethod
    def getWithId(id):
        return Payement.query.get(id)

    @staticmethod
    def getAll():
        return Payement.query.get.all()
