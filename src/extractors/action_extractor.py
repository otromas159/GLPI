ACCIONES = {

    "asign": "Asignación",

    "escal": "Escalamiento",

    "verific": "Verificación",

    "revis": "Revisión",

    "valid": "Validación",

    "configur": "Configuración",

    "instal": "Instalación",

    "actualiz": "Actualización",

    "cre": "Creación",

    "elimin": "Eliminación",

    "permis": "Asignación de permisos",

    "reinici": "Reinicio",

    "monitore": "Monitoreo",

    "prueba": "Pruebas",

    "cerr": "Cierre"

}

def extraer_acciones(ticket):

    acciones = set()

    texto = " ".join(ticket.seguimientos).lower()

    for raiz, nombre in ACCIONES.items():

        if raiz in texto:

            acciones.add(nombre)

    return sorted(acciones)