from src.application.essivi.models.type_Vehicule import Type_Vehicule


def formatType_Vehicule(id):
    type_vehicule = getWithId(id)
    return {
        'id': type_vehicule.id,
        'libelle_type': type_vehicule.libelle_type,
        'image': type_vehicule.image
    }



def formatOfId(id):
    type_vehicule = Type_Vehicule.query.get(id)
    return type_vehicule.format()



def exists(id):
    type_Vehicule = Type_Vehicule.query.get(id)
    return type_Vehicule if type_Vehicule is not None else False


def getWithId(id):
    return Type_Vehicule.query.get(id)


def getAll():
    return Type_Vehicule.query.get.all()
