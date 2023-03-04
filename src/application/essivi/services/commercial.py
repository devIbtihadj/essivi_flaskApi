from src.application.authentification.models.user import User
from src.application.essivi.models.client import Client
from src.application.essivi.models.commercial import Commercial
from src.application.essivi.services.client2 import formatClient2SansCoommercial


def formatCommercial(id):
    commercial = getWithId(id)
    clients = Client.query.filter_by(commercial_id=commercial.id).all()
    clients_formatted = [formatClient2SansCoommercial(client.id) for client in clients]
    return {
        'id': commercial.id,
        'prenom': commercial.prenom,
        'nom': commercial.nom,
        'numTel': commercial.numTel,
        'numIdentification': commercial.numIdentification,
        'quartier': commercial.quartier,
        'nomPersonnePrevenir': commercial.nomPersonnePrevenir,
        'prenomPersonnePrevenir': commercial.prenomPersonnePrevenir,
        'contactPersonnePrevenir': commercial.contactPersonnePrevenir,
        'user': User.formatOfId(commercial.user_id),
        'clients': clients_formatted if clients_formatted else None
    }


def simpleFormatCommercial(id):
    commercial = getWithId(id)
    return {
        'id': commercial.id,
        'prenom': commercial.prenom,
        'nom': commercial.nom,
        'numTel': commercial.numTel,
        'numIdentification': commercial.numIdentification,
        'quartier': commercial.quartier,
        'nomPersonnePrevenir': commercial.nomPersonnePrevenir,
        'prenomPersonnePrevenir': commercial.prenomPersonnePrevenir,
        'contactPersonnePrevenir': commercial.contactPersonnePrevenir,
        'user': User.formatOfId(commercial.user_id)
    }



def formatOfId(id):
    commercial = Commercial.query.get(id)
    return commercial.format()



def formatOfIdSimple(id):
    commercial = Commercial.query.get(id)
    return commercial.formatSimple()



def exists(id):
    commercial = Commercial.query.get(id)
    return commercial if commercial is not None else False


def getWithId(id):
    return Commercial.query.get(id)


def getAll():
    return Commercial.query.get.all()
