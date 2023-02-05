from __future__ import annotations


from src.application.extensions import db


class Emballage(db.Model):
    __tablename__ = 'emballages'
    id = db.Column(db.Integer, primary_key=True)
    libelle_type_emballage = db.Column(db.String(30), nullable=False)

    def __int__(self, libelle_type_emballage):
        self.libelle_type_emballage = libelle_type_emballage

    def format(self):
        return {
            'id': self.id,
            'libelle_type_emballage': self.libelle_type_emballage
        }

    @staticmethod
    def formatOfId(id):
        emballage = Emballage.query.get(id)
        return emballage.format()

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
        emballage = Emballage.query.get(id)
        return emballage if emballage is not None else False

    @staticmethod
    def getWithId(id):
        return Emballage.query.get(id)

    @staticmethod
    def getAll():
        return Emballage.query.get.all()