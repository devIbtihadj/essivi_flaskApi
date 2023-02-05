from __future__ import annotations

from src.application.essivi.models.commande import Commande
from src.application.essivi.models.type_Vente import Type_vente
from src.application.extensions import db


class Detail_cde(db.Model):
    __tablename__ = 'details_cdes'
    id = db.Column(db.Integer, primary_key=True)
    qte = db.Column(db.Integer, nullable=False)
    commande_id = db.Column(db.Integer, db.ForeignKey('commandes.id'), nullable=False)
    type_vente_id = db.Column(db.Integer, db.ForeignKey('types_ventes.id'), nullable=False)

    def __int__(self, qte, commande_id, type_vente):
        self.commande_id = commande_id
        self.qte = qte
        self.type_vente = type_vente

    def format(self):
        return {
            'id': self.id,
            'qte': self.qte,
            'commande': Commande.formatOfId(self.commande_id),
            'type_vente': Type_vente.formatOfId(self.type_vente_id)
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # @staticmethod
    # def exists(id):
    #     type_vente = Type_vente.query.get(id)
    #     return type_vente if type_vente is not None else False
    #
    # @staticmethod
    # def getWithId(id):
    #     return Type_vente.query.get(id)

    # @staticmethod
    # def getAll():
    #     return Type_vente.query.get.all()