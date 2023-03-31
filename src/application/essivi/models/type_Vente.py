from __future__ import annotations

from src.application.extensions import db



class Type_vente(db.Model):
    __tablename__ = 'types_ventes'
    id = db.Column(db.Integer, primary_key=True)
    libelle_type_vente = db.Column(db.String(20), nullable=False)
    prix_unit = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(150), nullable=True)
    qte_contenu_unitaire = db.Column(db.Float, nullable=False)
    qte_composition = db.Column(db.Integer, default=1)
    marque_id = db.Column(db.Integer, db.ForeignKey('marques.id'), nullable=False)

    details_commandes = db.relationship('Detail_cde', backref='types_ventes', lazy=True)




    def __init__(self, libelle_type_vente, prix_unit, image, qte_composition, marque_id, qte_contenu_unitaire):
        self.libelle_type_vente = libelle_type_vente
        self.prix_unit = prix_unit
        self.image = image
        self.qte_contenu_unitaire = qte_contenu_unitaire
        self.qte_composition = qte_composition
        self.marque_id = marque_id



    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

