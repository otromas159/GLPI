def construir_documento(ticket):

    partes = []

    partes.append(f"TICKET #{ticket.id}")

    partes.append("")

    partes.append("TÍTULO")

    partes.append(ticket.titulo)

    partes.append("")

    partes.append("DESCRIPCIÓN")

    partes.append(ticket.descripcion)

    partes.append("")

    partes.append("SEGUIMIENTOS")

    if ticket.seguimientos:

        for numero, seguimiento in enumerate(ticket.seguimientos, start=1):

            partes.append(f"{numero}. {seguimiento}")

    else:

        partes.append("Sin seguimientos")

    partes.append("")

    partes.append("SOLUCIÓN")

    if ticket.solucion:

        partes.append(ticket.solucion)

    else:

        partes.append("Sin solución registrada")

    return "\n".join(partes)