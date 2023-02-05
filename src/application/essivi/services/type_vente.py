from src.application.essivi.models.marque import Marque
from src.application.essivi.models.type_Vente import Type_vente
from src.application.essivi.services.marque import formatMarque


def formatType_Vente(id):
    type_vente = getWithId(id)
    return {
        'id': type_vente.id,
        'libelle_type_vente': type_vente.libelle_type_vente,
        'prix_unit': type_vente.prix_unit,
        'image': type_vente.image,
        'qte_composition': type_vente.qte_composition,
        'marque': formatMarque(type_vente.marque_id)

    }



def formatOfId(id):
    type_vente = Type_vente.query.get(id)
    return type_vente.format()

def exists(id):
    type_vente = Type_vente.query.get(id)
    return type_vente if type_vente is not None else False


def getWithId(id):
    return Type_vente.query.get(id)


def getAll():
    return Type_vente.query.get.all()