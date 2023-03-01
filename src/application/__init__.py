import os
from flask_cors import CORS
from src.application.authentification import auth_bp
# from src.application.essivi.routes import *
from src.application.essivi import *

#from src.application.essivi.routes import *

from .extensions import db, migrate
from src.application.essivi.models import *
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from flask import Flask, Blueprint

login_manager = LoginManager()
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()


def create_app(config_type):
    app = Flask(__name__)
    app.static_folder='essivi\\ressources\\'
    print(app.static_folder)
    print(os.path.dirname(app.instance_path))
    CORS(app)
    config_file = os.path.join(os.getcwd() + '\\src\\config', config_type + '.py')
    app.config.from_pyfile(config_file)
    app.register_blueprint(auth_bp)
    app.register_blueprint(marque_bp)
    app.register_blueprint(type_vehicule_bp)
    app.register_blueprint(vehicule_bp)
    app.register_blueprint(occupation_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(livraison_bp)
    app.register_blueprint(payement_bp)
    app.register_blueprint(type_vente_bp)
    app.register_blueprint(commande_bp)
    app.register_blueprint(commercial_bp)
    app.register_blueprint(commercial_client_bp)

    db.init_app(app)
    # initialize login manager
    login_manager.init_app(app)
    # initialize bcrypt
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    migrate.init_app(app, db, render_as_batch=True)

    return app
