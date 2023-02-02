from datetime import datetime

from src.application.essivi.models.client import Client
from src.application.essivi.models.commercial import Commercial
# from src.application.essivi.models.commercial import Commercial
from src.application.extensions import db


class Commercial_client(db.Model):
    __tablename__ = 'commercials_clients'
    id = db.Column(db.Integer, primary_key=True)
    dateDebut = db.Column(db.DateTime(), default=datetime.utcnow)
    dateFin = db.Column(db.DateTime(), nullable=True)
    commercial_id = db.Column(db.Integer, db.ForeignKey('commercials.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)

    def __int__(self, commercial_id, client_id):
        self.commercial_id = commercial_id
        self.client_id = client_id

    def format(self):
        return {
            'id': self.id,
            'dateDebut':  self.dateDebut.strftime("%Y-%m-%d %H:%M:%S:%f"),
            'dateFin': self.dateFin.strftime("%Y-%m-%d %H:%M:%S:%f") if self.dateFin else None,
            'commercial': Commercial.formatOfIdSimple(self.commercial_id),
            'client': Client.formatOfId(self.client_id)
        }

    @staticmethod
    def formatOfId(id):
        commercial_client = Commercial_client.query.get(id)
        return commercial_client.format()

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
        commercial_client = Commercial_client.query.get(id)
        return commercial_client if commercial_client is not None else False

    @staticmethod
    def getWithId(id):
        return Commercial_client.query.get(id)

    @staticmethod
    def getAll():
        return Commercial_client.query.get.all()
