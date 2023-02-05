from __future__ import annotations
from datetime import datetime

from src.application.extensions import db


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



    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

