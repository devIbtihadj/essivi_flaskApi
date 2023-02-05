from src.application.essivi.models.ocuupation import Occupation
from src.application.essivi.services.commercial import simpleFormatCommercial
from src.application.essivi.services.vehicule import formatVehicule


def formatOccupation(id):
    occupation = getWithId(id)
    return {
        'id': occupation.id,
        'dateDebut': occupation.dateDebut,
        'dateFin': occupation.dateFin,
        'commercial': simpleFormatCommercial(occupation.commercial_id),
        'vehicule': formatVehicule(occupation.vehicule_id)

    }



def formatOfId(id):
    occupation = Occupation.query.get(id)
    return occupation.format()



def exists(id):
    occupation = Occupation.query.get(id)
    return occupation if occupation is not None else False


def getWithId(id):
    return Occupation.query.get(id)


def getAll():
    return Occupation.query.get.all()
