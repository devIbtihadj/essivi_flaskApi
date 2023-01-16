from datetime import datetime

from flask_login import UserMixin
from dataclasses import dataclass


from src.application import db, bcrypt, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(60))


    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def format(self):
        return {
            'email': self.email,
        }

    @staticmethod
    def formatOfId(id):
        user = User.query.get(int(id))
        return user.format()

    def check_password(self, password) -> bool:
        return bcrypt.check_password_hash(self.user_password, password)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            print("err user insert")

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
