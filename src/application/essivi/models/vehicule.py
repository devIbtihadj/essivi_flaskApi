from src.application.extensions import db
from src.application.essivi.models.type_Vehicule import Type_Vehicule


class Vehicule(db.Model):
    __tablename__ = 'vehicules'
    id = db.Column(db.Integer, primary_key=True)
    immatriculation = db.Column(db.String(8), nullable=False, unique=True)

    type_vehicule_id = db.Column(db.Integer, db.ForeignKey('types_vehicules.id'), nullable=False)

    def __int__(self, immatriculation, type_vehicule_id):
        self.immatriculation = immatriculation
        self.type_vehicule_id = type_vehicule_id

    def format(self):
        return {
            'id': self.id,
            'immatriculation': self.immatriculation,
            'type_vehicule': Type_Vehicule.formatOfId(self.type_vehicule_id)
        }

    def formatOfId(id):
        vehicule = Vehicule.query.get(id)
        return vehicule.format()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
