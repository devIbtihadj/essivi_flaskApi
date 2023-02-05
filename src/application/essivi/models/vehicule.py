from src.application.extensions import db


class Vehicule(db.Model):
    __tablename__ = 'vehicules'
    id = db.Column(db.Integer, primary_key=True)
    immatriculation = db.Column(db.String(8), nullable=False, unique=True)

    type_vehicule_id = db.Column(db.Integer, db.ForeignKey('types_vehicules.id'), nullable=False)

    def __int__(self, immatriculation, type_vehicule_id):
        self.immatriculation = immatriculation
        self.type_vehicule_id = type_vehicule_id



    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
