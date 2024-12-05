def empleadoSh(item):
    return {
        "id": str(item.get("_id")),
        "nombre": item.get("nombre"),
        "apellido": item.get("apellido"),
        "celular": item.get("celular"),
        "dni": item.get("dni"),
        "capacitaciones": item.get("capacitaciones"),
        "activo": item.get("activo"),
    }

def empleadosSh(items) -> list:
    return [empleadoSh(item) for item in items]
