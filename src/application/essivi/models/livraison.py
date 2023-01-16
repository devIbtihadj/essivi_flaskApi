from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.application.essivi.models.commercial import Commercial
    from src.application.essivi.models.payement import Payement

from src.application.extensions import db


class Livraison(db.Model):
    __tablename__ = 'livraisons'
    id = db.Column(db.Integer, primary_key=True)
    date_heure = db.Column(db.DateTime(), default=datetime.utcnow)

    payements = db.relationship('Payement', backref='livraisons', lazy=True)
    commercial_deliver_id = db.Column(db.Integer, db.ForeignKey('commercials.id'), nullable=False)

    def __int__(self, payement_id, commercial_id):
        self.payement_id = payement_id
        self.commercial_id = commercial_id

    def format(self):
        return {
            'id': self.id,
            'commercial': Commercial.formatOfId(self.commercial_id),
            'payement': Payement.formatOfId(self.payement_id)
        }

    @staticmethod
    def formatOfId(id):
        livraison = Livraison.query.get(id)
        return livraison.format()

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
        livraison = Livraison.query.get(id)
        return livraison if livraison is not None else False

    @staticmethod
    def getWithId(id):
        return Livraison.query.get(id)

    @staticmethod
    def getAll():
        return Livraison.query.get.all()
