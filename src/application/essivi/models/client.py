from datetime import datetime

from src.application.extensions import db


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    longitude = db.Column(db.String(10), nullable=False)
    latitude = db.Column(db.String(10), nullable=False)
    quartier = db.Column(db.String(25), nullable=False)
    dateEnrollement = db.Column(db.DateTime(), default=datetime.today())

    commercial_id = db.Column(db.Integer, db.ForeignKey('commercials.id'), nullable=False)
    commandes = db.relationship('Commande', backref='clients', lazy=True)

    def __init__(self, nom, prenom, longitude, latitude, quartier):
        self.quartier = quartier
        self.nom = nom
        self.prenom = prenom
        self.latitude = latitude
        self.longitude = longitude

    def format(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'quartier': self.quartier,
            'dateEnrollement': self.dateEnrollement
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def formatOfId(id):
        client = Client.query.get(id)
        return client.format()

    @staticmethod
    def exists(id):
        client = Client.query.get(id)
        return client if client is not None else False

    @staticmethod
    def getWithId(id):
        return Client.query.get(id)

    @staticmethod
    def getAll():
        return Client.query.get.all()
