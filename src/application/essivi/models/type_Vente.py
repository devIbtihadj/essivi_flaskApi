from src.application.essivi.models.emballage import Emballage
from src.application.essivi.models.marque import Marque
from src.application.extensions import db


class Type_vente(db.Model):
    __tablename__ = 'types_ventes'
    id = db.Column(db.Integer, primary_key=True)
    libelle_type_vente = db.Column(db.String(20), nullable=False)
    qte_unit = db.Column(db.Integer, nullable=False)
    prix_unit = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=False)

    marque_id = db.Column(db.Integer, db.ForeignKey('marques.id'), nullable=False)
    emballage_id = db.Column(db.Integer, db.ForeignKey('emballages.id'), nullable=False)

    def __init__(self, libelle_type_vente, qte_unit, prix_unit, image, marque_id, emballage_id):
        self.libelle_type_vente = libelle_type_vente
        self.qte_unit = qte_unit
        self.prix_unit = prix_unit
        self.image = image
        self.marque_id = marque_id
        self.emballage_id = emballage_id

    def format(self):
        return {
            'id': self.id,
            'libelle_type_vente': self.libelle_type_vente,
            'qte_unit': self.qte_unit,
            'prix_unit': self.prix_unit,
            'image': self.image,
            'marque': Marque.query.get(self.marque_id),
            'emballage': Emballage.query.get(self.emballage_id)

        }

    @staticmethod
    def formatOfId(id):
        type_vente = Type_vente.query.get(id)
        return type_vente.format()

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
        type_vente = Type_vente.query.get(id)
        return type_vente if type_vente is not None else False

    @staticmethod
    def getWithId(id):
        return Type_vente.query.get(id)

    @staticmethod
    def getAll():
        return Type_vente.query.get.all()