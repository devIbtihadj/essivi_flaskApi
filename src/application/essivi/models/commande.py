from __future__ import annotations


from datetime import datetime

from src.application.extensions import db


class Commande(db.Model):
    __tablename__ = 'commandes'
    id = db.Column(db.Integer, primary_key=True)
    date_cde = db.Column(db.DateTime(), default=datetime.utcnow)
    date_voulu_reception = db.Column(db.DateTime(), nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    livraison_id = db.Column(db.Integer, db.ForeignKey('livraisons.id'), nullable=True)

    details_commandes = db.relationship('Detail_cde', backref='commandes', lazy=True)

    def __int__(self, date_voulu_reception, client_id):
        self.date_voulu_reception = date_voulu_reception
        self.client_id = client_id

    def insert(self):
        db.session.add(self)
        db.session.flush()
        return self.id

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def exists(id):
        commande = Commande.query.get(id)
        return commande if commande is not None else False

    @staticmethod
    def getWithId(id):
        return Commande.query.get(id)

    @staticmethod
    def getAll():
        return Commande.query.get.all()
