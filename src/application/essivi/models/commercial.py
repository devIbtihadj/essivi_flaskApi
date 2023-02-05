from __future__ import annotations

from src.application.authentification.models.user import User
from src.application.essivi.models.client import Client
from src.application.extensions import db
from sqlalchemy import and_
from src.application.essivi.models.utilisateur import Utilisateur
from typing import TYPE_CHECKING


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
        # commercials_clients = Commercial_client.query.filter \
        #     (and_(Commercial_client.dateFin is None, Commercial.id == self.id)).all()
        # commercials_clients_formatted = [commercial_client.format() for commercial_client in commercials_clients]

        clients = Client.query.filter_by(commerial_id=self.id).all()
        clients_formatted = [client.format() for client in clients]
        return {
            'id': self.id,
            'prenom': self.prenom,
            'nom': self.nom,
            'numTel': self.numTel,
            'numIdentification': self.numIdentification,
            'quartier': self.quartier,
            'nomPersonnePrevenir': self.nomPersonnePrevenir,
            'prenomPersonnePrevenir': self.prenomPersonnePrevenir,
            'contactPersonnePrevenir': self.contactPersonnePrevenir,
            'user' : User.formatOfId(self.user_id),
            'clients': clients_formatted if clients_formatted else None
        }

    def formatSimple(self):
        commercial = Commercial.query.get(self.id)
        return {
            'id': self.id,
            'prenom': self.prenom,
            'nom': self.nom,
            'numTel': self.numTel,
            'numIdentification': self.numIdentification,
            'quartier': self.quartier,
            'nomPersonnePrevenir': self.nomPersonnePrevenir,
            'prenomPersonnePrevenir': self.prenomPersonnePrevenir,
            'contactPersonnePrevenir': self.contactPersonnePrevenir,
            'user' : User.formatOfId(self.user_id)
        }
    @staticmethod
    def formatOfId(id):
        commercial = Commercial.query.get(id)
        return commercial.format()

    @staticmethod
    def formatOfIdSimple(id):
        commercial = Commercial.query.get(id)
        return commercial.formatSimple()


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

    @staticmethod
    def exists(id):
        commercial = Commercial.query.get(id)
        return commercial if commercial is not None else False

    @staticmethod
    def getWithId(id):
        return Commercial.query.get(id)

    @staticmethod
    def getAll():
        return Commercial.query.get.all()
