from src.application.essivi.models.commande import Commande
from src.application.essivi.models.detail_Cde import Detail_cde
from src.application.essivi.models.livraison import Livraison
from src.application.essivi.services.client import formatClient, formatClientForCommercial
from src.application.essivi.services.detail_Cde import simpleFormatDetail_Cde
from src.application.essivi.services.livraison import simpleFormatLivraison


def formatCommande(id):
    try:
        commande = getWithId(id)
        print(commande.id)
        livraison = Livraison.query.filter_by(commande_id=commande.id).first()
        print(livraison)
        details_commandes = Detail_cde.query.filter_by(commande_id=commande.id).all()
        print(details_commandes)

        details_commandes_formated = [simpleFormatDetail_Cde(detail.id) for detail in details_commandes]
        print(detail.id for detail in details_commandes)
        print("details_commandes_formated")
        print(details_commandes_formated)

        return {
            'id': commande.id,
            'date_cde': commande.date_cde.strftime("%Y-%m-%d %H:%M:%S:%f"),
            'date_voulu_reception': commande.date_voulu_reception.strftime("%Y-%m-%d %H:%M:%S:%f"),
            'client': formatClient(commande.client_id),
            'livraison': simpleFormatLivraison(commande.livraison_id) if livraison else None,
            'details': details_commandes_formated if details_commandes_formated else None
        }
    except Exception as e:
        print("Exception */**/**/*")
        print(e)


def simpleFormatCommande(id):
    commande = getWithId(id)
    details_commandes = Detail_cde.query.filter_by(commande_id=commande.id).all()
    details_commandes_formated = [simpleFormatDetail_Cde(detail.id) for detail in details_commandes]
    print(detail.id for detail in details_commandes)
    return {
        'id': commande.id,
        'date_cde': commande.date_cde.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'date_voulu_reception': commande.date_voulu_reception.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'client': formatClient(commande.client_id),
        'details': details_commandes_formated if details_commandes_formated else None
    }

def simpleFormatCommandeWithDetails(id):
    commande = getWithId(id)
    return {
        'id': commande.id,
        'date_cde': commande.date_cde.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'date_voulu_reception': commande.date_voulu_reception.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'client': formatClient(commande.client_id)
    }

def simpleFormatCommandeWithDetailsForCommercial(id, idComm):
    commande = getWithId(id)
    return {
        'id': commande.id,
        'date_cde': commande.date_cde.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'date_voulu_reception': commande.date_voulu_reception.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'client': formatClientForCommercial(commande.client_id, idComm) if formatClientForCommercial(commande.client_id, idComm) else None
    }


def formatOfId(id):
    commande = Commande.query.get(id)
    return commande.format()


def formatOfIdSimple(id):
    commande = Commande.query.get(id)
    return commande.formatOfIdSimpleRetrn()


def getWithId(id):
    commande = Commande.query.get(id)
    return commande
