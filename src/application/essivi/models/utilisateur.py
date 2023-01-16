from datetime import datetime

from src.application.extensions import db


class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    numTel = db.Column(db.String(8), nullable=False)
    date_creation_compte = db.Column(db.DateTime(), default=datetime.utcnow)
    type = db.Column(db.String(20), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "utilisateurs",
        "polymorphic_on": type
    }

    def __int__(self, nom, prenom, numTel, user_id):
        self.nom=nom
        self.prenom=prenom
        self.numTel=numTel
        self.user_id=user_id
