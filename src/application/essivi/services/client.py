from src.application.essivi.models.client import Client
from src.application.essivi.services.commercial import simpleFormatCommercial


def formatClient(id):
    client = getWithId(id)
    try:
        return {
            'id': client.id,
            'nom': client.nom,
            'prenom': client.prenom,
            'numTel': client.numTel,
            'longitude': client.longitude,
            'latitude': client.latitude,
            'quartier': client.quartier,
            'dateEnrollement': client.dateEnrollement.strftime("%Y-%m-%d %H:%M:%S:%f"),
            'commercial': simpleFormatCommercial(client.commercial_id)
        }

    except Exception as e:
        print(e)

def formatOfId(id):
    client = Client.query.get(id)
    return client.format()

def exists(id):
    client = Client.query.get(id)
    return client if client is not None else False

def getWithId(id):
    return Client.query.get(id)

def getAll():
    return Client.query.get.all()
