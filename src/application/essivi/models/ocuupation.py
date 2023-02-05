from __future__ import annotations
from datetime import datetime

from src.application.essivi.models.commercial import Commercial
from src.application.essivi.models.vehicule import Vehicule
from src.application.extensions import db
from typing import TYPE_CHECKING


class Occupation(db.Model):
    __tablename__ = 'ocuupations'
    id = db.Column(db.Integer, primary_key=True)
    dateDebut = db.Column(db.DateTime(), default=datetime.utcnow)
    dateFin = db.Column(db.DateTime(), nullable=True)

    commercial_id = db.Column(db.Integer, db.ForeignKey('commercials.id'), nullable=False)
    vehicule_id = db.Column(db.Integer, db.ForeignKey('vehicules.id'), nullable=False)

    def __init__(self, comercial_id, vehicule_id):
        self.commercial_id = comercial_id
        self.vehicule_id = vehicule_id

    def format(self):
        return {
            'id': self.id,
            'dateDebut': self.dateDebut,
            'dateFin': self.dateFin,
            'commercial': Commercial.formatOfId(self.commercial_id),
            'vehicule': Vehicule.formatOfId(self.vehicule_id)

        }

    @staticmethod
    def formatOfId(id):
        occupation = Occupation.query.get(id)
        return occupation.format()

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
        occupation = Occupation.query.get(id)
        return occupation if occupation is not None else False

    @staticmethod
    def getWithId(id):
        return Occupation.query.get(id)

    @staticmethod
    def getAll():
        return Occupation.query.get.all()
