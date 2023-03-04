from src.application.essivi.models.client import Client


def formatClient2SansCoommercial(id):
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
            'dateEnrollement': client.dateEnrollement.strftime("%Y-%m-%d %H:%M:%S:%f")
        }

    except Exception as e:
        print(e)


def getWithId(id):
    return Client.query.get(id)