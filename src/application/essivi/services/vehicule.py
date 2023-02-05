from src.application.essivi.models.vehicule import Vehicule
from src.application.essivi.services.type_vehicule import formatType_Vehicule


def formatVehicule(id):
    vehicule = getWithId(id)
    return {
        'id': vehicule.id,
        'immatriculation': vehicule.immatriculation,
        'type_vehicule.py': formatType_Vehicule(vehicule.type_vehicule_id)
    }


def formatOfId(id):
    vehicule = Vehicule.query.get(id)
    return vehicule.format()

def getWithId(id):
    return Vehicule.query.get(id)