CATEGORIAS = {

    "wifi": "Infraestructura",

    "red": "Infraestructura",

    "vpn": "Infraestructura",

    "correo": "Correo",

    "outlook": "Correo",

    "exchange": "Correo",

    "impresora": "Impresoras",

    "excel": "Office",

    "word": "Office",

    "sharepoint": "Microsoft 365",

    "dynamics": "Dynamics",

    "rol": "Permisos",

    "permiso": "Permisos",

    "usuario": "Usuarios"

}

def clasificar(ticket):

    texto = (
        ticket.titulo + " " +
        ticket.descripcion
    ).lower()

    for palabra, categoria in CATEGORIAS.items():

        if palabra in texto:

            return categoria

    return "General"