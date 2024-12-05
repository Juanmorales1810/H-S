def accidentesSh(item):
    return {
        "id": str(item.get("_id")),
        "codigo": item.get("codigo"),
        "nombre": item.get("nombre"),
        "descripcion": item.get("descripcion"),
        "activo": item.get("activo"),
    }

def accidentessSh(items) -> list:
    return [accidentesSh(item) for item in items]
