from __future__ import annotations

from src.application.extensions import db


class Marque(db.Model):
    __tablename__ = 'marques'
    id = db.Column(db.Integer, primary_key=True)
    libelle_marque = db.Column(db.String(20), nullable=False)

    def __int__(self, libelle_marque):
        self.libelle_marque = libelle_marque



    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

