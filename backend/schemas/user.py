def UserSh(item):
    return {
        "id": str(item.get("_id")),
        "correo": item.get("correo"),
        "name": item.get("name"),
        "lastName": item.get("lastName"),
        "phone": item.get("phone"),
        "empresas": item.get("empresas")
    }

def UsersSh(items) -> list:
    return [UserSh(item) for item in items]