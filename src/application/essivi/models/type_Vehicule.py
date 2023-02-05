from __future__ import annotations
from src.application.extensions import db


class Type_Vehicule(db.Model):
    __tablename__ = 'types_vehicules'
    id = db.Column(db.Integer, primary_key=True)
    libelle_type = db.Column(db.String(15), nullable=False, unique=True)
    image = db.Column(db.String(200), nullable=False)

    def __int__(self, libelle_type, image):
        self.libelle_type = libelle_type
        self.image=image



    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

