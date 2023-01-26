
from src.application.extensions import db


class Commercial_client(db.Model):
    __tablename__ = 'livraisons'
    id = db.Column(db.Integer, primary_key=True)
