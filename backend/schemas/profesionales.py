def profesionalSh(item):
    return {
        "id": str(item.get("_id")),
        "dni": item.get("dni"),
        "nombre": item.get("nombre"),
        "apellido": item.get("apellido"),
        "cuil": item.get("cuil"),
        "fechaAlta": item.get("fechaAlta"),
        "observacion": item.get("observacion"),
        "empresas": item.get("empresas"),
        "activo": item.get("activo"),
    }

def profesionalesSh(items) -> list:
    return [profesionalSh(item) for item in items]
