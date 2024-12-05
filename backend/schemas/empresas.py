def empresaSh(item):
    return {
        "id": str(item.get("_id")),
        "cuit": item.get("cuit"),
        "razonSocial": item.get("razonSocial"),
        "rubro": item.get("rubro"),
        "domicilio": item.get("domicilio"),
        "fechaAlta": item.get("fechaAlta"),
        "observacion": item.get("observacion"),
        "claveArt": item.get("claveArt"),
        "contacto": item.get("contacto"),
        "activo": item.get("activo"),
    }

def empresasSh(items) -> list:
    return [empresasSh(item) for item in items]
