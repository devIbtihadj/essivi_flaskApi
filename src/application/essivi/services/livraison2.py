from src.application.essivi.models.livraison import Livraison
from src.application.essivi.services.commande import simpleFormatCommande
from src.application.essivi.services.commercial import simpleFormatCommercial


def formatLivraison(id):
    livraison = Livraison.query.get(id)
    return {
        'id': livraison.id,
        'date_heure': livraison.date_heure.strftime("%Y-%m-%d %H:%M:%S:%f"),
        'commande': simpleFormatCommande(livraison.commande_id),
        'commercial': simpleFormatCommercial(livraison.commercial_id),
    }