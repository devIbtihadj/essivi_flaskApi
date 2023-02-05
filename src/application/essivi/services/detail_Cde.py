from src.application.essivi.models.detail_Cde import Detail_cde
#from src.application.essivi.services.commande import simpleFormatCommande
from src.application.essivi.services.type_vente import formatType_Vente


def formatDetail_Cde(id):
    detail_cde = getWithId(id)
    return {
        'id': detail_cde.id,
        'qte': detail_cde.qte,
        'commande': simpleFormatCommande(detail_cde.commande_id),
        'type_vente': formatType_Vente(detail_cde.type_vente_id)
    }


def simpleFormatDetail_Cde(id):
    print(id)
    detail_cde = getWithId(id)
    print(detail_cde)
    print("simpleFormatDetail_Cde method")
    return {
        'id': detail_cde.id,
        'qte': detail_cde.qte,
        'type_vente': formatType_Vente(detail_cde.type_vente_id)
    }

def exists(id):
    detail = Detail_cde.query.get(id)
    return detail if detail is not None else False


def getWithId(id):
    return Detail_cde.query.get(id)


def getAll():
    return Detail_cde.query.get.all()