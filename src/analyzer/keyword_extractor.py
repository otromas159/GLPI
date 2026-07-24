KEYWORDS = {

    "wifi": [
        "wifi",
        "wi-fi",
        "inalambrica"
    ],

    "impresora": [
        "impresora",
        "impresion",
        "imprimir",
        "duplex"
    ],

    "outlook": [
        "outlook",
        "correo",
        "mail",
        "exchange"
    ],

    "office": [
        "office",
        "word",
        "excel",
        "powerpoint"
    ],

    "dynamics": [
        "dynamics",
        "pedido",
        "compra",
        "inventario",
        "almacen"
    ],

    "permisos": [
        "permiso",
        "rol",
        "perfil",
        "acceso"
    ]
}
def extraer_keywords(texto):

    texto = texto.lower()

    encontrados = set()

    for categoria, palabras in KEYWORDS.items():

        for palabra in palabras:

            if palabra in texto:

                encontrados.add(categoria)

    return sorted(encontrados)