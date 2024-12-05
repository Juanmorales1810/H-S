def cursoSh(item):
    return {
        "id": str(item.get("_id")),
        "nombre": item.get("nombre"),
        "fecha": item.get("fecha"),
        "descripcion": item.get("descripcion"),
        "activo": item.get("activo"),
    }

def cursosSh(items) -> list:
    return [cursosSh(item) for item in items]
