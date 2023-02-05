from __future__ import annotations


from datetime import datetime

from src.application.essivi.models.detail_Cde import Detail_cde
from src.application.essivi.models.livraison import Livraison

from src.application.extensions import db
from src.application.essivi.models.client import Client


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

    def format(self):
        livraison = Livraison.query.filter_by(commande_id=self.id).first()
        details_commandes = Detail_cde.query.filter_by(commande_id=self.id).all()

        details_commandes_formates = [detail.format() for detail in details_commandes]

        return {
            'id': self.id,
            'date_cde': self.date_cde.strftime("%Y-%m-%d %H:%M:%S:%f"),
            'date_voulu_reception': self.date_voulu_reception.strftime("%Y-%m-%d %H:%M:%S:%f"),
            'client': Client.formatOfId(self.client_id),
            'livraison': livraison.formatSansCommande(self.livraison_id) if livraison else None,
            'details': details_commandes_formates if details_commandes_formates else None
        }

    def formatOfIdSimpleRetrn(self):
        return {
            'id': self.id,
            'date_cde': self.date_cde,
            'date_voulu_reception': self.date_voulu_reception,
            'client': Client.formatOfId(self.client_id)
        }

    @staticmethod
    def formatOfId(id):
        commande = Commande.query.get(id)
        return commande.format()

    @staticmethod
    def formatOfIdSimple(id):
        commande = Commande.query.get(id)
        return commande.formatOfIdSimpleRetrn()

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
