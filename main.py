# This is a sample Python script.
from datetime import datetime

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.application import create_app, db

from src.application.essivi.models.utilisateur import Utilisateur
from src.application.essivi.models.commercial import Commercial
from src.application.essivi.models.type_Vehicule import Type_Vehicule
from src.application.essivi.models.marque import Marque
from src.application.essivi.models.payement import Payement
from src.application.essivi.models.vehicule import Vehicule
from src.application.essivi.models.client import Client
from src.application.essivi.models.ocuupation import Occupation
from src.application.essivi.models.emballage import Emballage
from src.application.essivi.models.detail_Cde import Detail_cde
from src.application.essivi.models.commande import Commande
from src.application.essivi.models.admin import Admin
from src.application.essivi.models.type_Vente import Type_vente
from src.application.essivi.models.client import Client
from src.application.essivi.models.livraison import Livraison

from src.application.authentification.routes import auth
from src.application.essivi.routes import marque
from src.application.essivi.routes import type_vehicule
from src.application.essivi.routes import vehicule
from src.application.essivi.routes import commercial_client
from src.application.essivi.routes import client
from src.application.essivi.routes import payement
from src.application.essivi.routes import utilisateurs
from src.application.essivi.routes import occupation
from src.application.essivi.routes import type_vente
from src.application.essivi.routes import livraison
from src.application.essivi.routes import commercial
from src.application.essivi.routes import commande



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()

    flask_app.run()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
