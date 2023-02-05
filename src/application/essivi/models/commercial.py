from __future__ import annotations

from src.application.extensions import db
from src.application.essivi.models.utilisateur import Utilisateur


class Commercial(Utilisateur):
    __tablename__ = 'commercials'
    id = db.Column(db.Integer, db.ForeignKey("utilisateurs.id"), primary_key=True)
    __mapper_args__ = {
        "polymorphic_identity": "commercials"
    }
    numIdentification = db.Column(db.String(5), nullable=False)
    quartier = db.Column(db.String(25), nullable=True)
    nomPersonnePrevenir = db.Column(db.String(25), nullable=True)
    prenomPersonnePrevenir = db.Column(db.String(30), nullable=True)
    contactPersonnePrevenir = db.Column(db.String(8), nullable=True)

    clients_registered = db.relationship('Client', backref='commercials', lazy=True)
    livraisons = db.relationship('Livraison', backref='commercials', lazy=True)

    def __int__(self, nom, prenom, numTel, user_id,numIdentification, quartier, nomPersonnePrevenir, prenomPersonnePrevenir,
                contactPersonnePrevenir):
        Utilisateur.__int__(self, nom, prenom, numTel, user_id)
        self.numIdentification = numIdentification
        self.quartier = quartier
        self.nomPersonnePrevenir = nomPersonnePrevenir
        self.prenomPersonnePrevenir = prenomPersonnePrevenir
        self.contactPersonnePrevenir = contactPersonnePrevenir


    def format(self):
        return {
            'id': self.id,
            'prenom': self.prenom,
            'nom': self.nom,
            'numTel': self.numTel

        }

    @staticmethod
    def formatOfIdSimple(id):
        commercial = Commercial.query.get(id)
        return commercial.format()



    def insert(self):
        try:
            db.session.add(self)
        except:
            print("exception 500 from my server")

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

