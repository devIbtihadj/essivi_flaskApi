from src.application.essivi.models.marque import Marque


def formatMarque(id):
    marque = getWithId(id)
    return {
        'id': marque.id,
        'libelle_marque': marque.libelle_marque
    }



def exists(id):
    marque = Marque.query.get(id)
    return marque if marque is not None else False


def getWithId(id):
    return Marque.query.get(id)


def getAll():
    return Marque.query.get.all()
