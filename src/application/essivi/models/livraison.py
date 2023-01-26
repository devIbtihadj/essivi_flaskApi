from datetime import datetime

from typing import TYPE_CHECKING

#from src.application.essivi.models.commande import Commande

if TYPE_CHECKING:
    from src.application.essivi.models.commercial import Commercial
    from src.application.essivi.models.payement import Payement

from src.application.extensions import db


class Livraison(db.Model):
    __tablename__ = 'livraisons'
    id = db.Column(db.Integer, primary_key=True)
    date_heure = db.Column(db.DateTime(), default=datetime.utcnow)

    payements = db.relationship('Payement', backref='livraisons', lazy=True)
    commercial_id = db.Column(db.Integer, db.ForeignKey('commercials.id'), nullable=False)
    commande_id = db.Column(db.Integer, db.ForeignKey('commandes.id'), nullable=False)

    def __int__(self, commande_id, commercial_deliver_id):
        self.commande_id = commande_id
        self.commercial_id = commercial_deliver_id

    def format(self):
        payements = Payement.query.filter_by(livraison_id=self.id).order_by(Payement.id.desc()).all()
        payements_formatted = [payement.format() for payement in payements]
        return {
            'id': self.id,
            'date_heure' : self.date_heure,
            'commande' : Commande.formatOfId(self.commande_id),
            'commercial': Commercial.formatOfId(self.commercial_id),
            'payements': payements_formatted
        }




    @staticmethod
    def formatOfId(id):
        livraison = Livraison.query.get(id)
        return livraison.format()

    def insert(self):
        db.session.add(self)
        # db.session.commit()
        db.session.flush()
        return self.id

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def exists(id):
        livraison = Livraison.query.get(id)
        return livraison if livraison is not None else False

    @staticmethod
    def getWithId(id):
        return Livraison.query.get(id)

    @staticmethod
    def getAll():
        return Livraison.query.get.all()
