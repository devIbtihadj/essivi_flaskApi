from __future__ import annotations

from src.application.extensions import db


class Marque(db.Model):
    __tablename__ = 'marques'
    id = db.Column(db.Integer, primary_key=True)
    libelle_marque = db.Column(db.String(20), nullable=False)

    def __int__(self, libelle_marque):
        self.libelle_marque = libelle_marque

    def format(self):
        return {
            'id': self.id,
            'libelle_marque': self.libelle_marque
        }

    @staticmethod
    def formatOfId(id):
        marque = Marque.query.get(id)
        return marque.format()

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
        marque = Marque.query.get(id)
        return marque if marque is not None else False

    @staticmethod
    def getWithId(id):
        return Marque.query.get(id)

    @staticmethod
    def getAll():
        return Marque.query.get.all()
