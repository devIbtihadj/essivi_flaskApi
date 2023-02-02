from datetime import datetime

#from src.application.essivi.models.commercial_client import Commercial_client
# from src.application.essivi.models.commercial import Commercial
# from src.application.essivi.models.commercial_client import Commercial_client
from src.application.extensions import db
from sqlalchemy import and_


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    longitude = db.Column(db.String(10), nullable=False)
    latitude = db.Column(db.String(10), nullable=False)
    quartier = db.Column(db.String(25), nullable=False)
    numTel = db.Column(db.String(8), nullable=False)
    dateEnrollement = db.Column(db.DateTime(), default=datetime.today())

    commercial_id = db.Column(db.Integer, db.ForeignKey('commercials.id'), nullable=False)
    commandes = db.relationship('Commande', backref='clients', lazy=True)

    def __init__(self, nom, prenom, numTel, longitude, latitude, quartier, commercial_id):
        self.quartier = quartier
        self.nom = nom
        self.prenom = prenom
        self.numTel = numTel
        self.latitude = latitude
        self.longitude = longitude
        self.commercial_id = commercial_id

    def format(self):
        try:
            #commercial_client = Commercial_client.query.filter(and_(Commercial_client.dateFin is None, Commercial_client.client_id == self.id)).first()

            # print(commercial_client)

            return {
                'id': self.id,
                'nom': self.nom,
                'prenom': self.prenom,
                'numTel': self.numTel,
                'longitude': self.longitude,
                'latitude': self.latitude,
                'quartier': self.quartier,
                'dateEnrollement': self.dateEnrollement.strftime("%Y-%m-%d %H:%M:%S:%f")
            }
        # 'commercial_client': Commercial_client.formatOfId(commercial_client.id)

        except Exception as e:
            print(e)




    def insert(self):
        try:
            db.session.add(self)
            # db.session.commit()
            db.session.flush()
            return self.id
        except Exception as e:
            print(e)
            print("err client insert")

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
