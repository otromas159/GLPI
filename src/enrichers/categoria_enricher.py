def enriquecer_categoria(knowledge):

    texto = (
        knowledge.problema
        + " "
        + knowledge.solucion
    ).lower()

    if "outlook" in texto:
        knowledge.categoria = "Correo"

    elif "impresora" in texto:
        knowledge.categoria = "Impresión"

    elif "wifi" in texto:
        knowledge.categoria = "Red"

    elif "dynamics" in texto:
        knowledge.categoria = "Dynamics"

    elif "permiso" in texto:
        knowledge.categoria = "Permisos"

    else:
        knowledge.categoria = "General"

    return knowledge