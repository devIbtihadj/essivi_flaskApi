from src.application.essivi.models.livraison import Livraison
#from src.application.essivi.services.commande import simpleFormatCommande
from src.application.essivi.services.commercial import simpleFormatCommercial

# TODO  CHECK THIS IN COMMANDES LIVRAISON2 :



def simpleFormatLivraison(id):
    livraison = getWithId(id)
    return {
        'id': livraison.id,
        'date_heure': livraison.date_heure.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'commercial': simpleFormatCommercial(livraison.commercial_id),
    }





def formatOfId(id):
    livraison = Livraison.query.get(id)
    return livraison.format()


def exists(id):
    livraison = Livraison.query.get(id)
    return livraison if livraison is not None else False


def getWithId(id):
    return Livraison.query.get(id)


def getAll():
    return Livraison.query.get.all()