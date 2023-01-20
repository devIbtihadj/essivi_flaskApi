from datetime import datetime

from src.application.essivi.models.client import Client
from src.application.essivi.models.livraison import Livraison
#from src.application.essivi.models.livraison import Livraison
from src.application.extensions import db


class Commande(db.Model):
    __tablename__ = 'commandes'
    id = db.Column(db.Integer, primary_key=True)
    date_cde = db.Column(db.DateTime(), default=datetime.utcnow)
    date_voulu_reception = db.Column(db.DateTime(), nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    livraisons = db.relationship('Livraison', backref='commandes', lazy=True)

    def __int__(self, date_voulu_reception, client_id):
        self.date_voulu_reception = date_voulu_reception
        self.client_id = client_id

    def format(self):
        livraisons = Livraison.query.filter_by(commande_id=self.id).order_by(Livraison.id).all()
        livraisons_formatted = [livraison.format() for livraison in livraisons]
        return {
            'id': self.id,
            'date_cde': self.date_cde,
            'date_voulu_reception': self.date_voulu_reception,
            'client': Client.formatOfId(self.client_id),
            'livraisons' : livraisons_formatted
        }

    @staticmethod
    def formatOfId(id):
        commande = Commande.query.get(id)
        return commande.format()

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
        commande = Commande.query.get(id)
        return commande if commande is not None else False

    @staticmethod
    def getWithId(id):
        return Commande.query.get(id)

    @staticmethod
    def getAll():
        return Commande.query.get.all()
