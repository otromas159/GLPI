from src.database.connection import obtener_conexion


def obtener_seguimientos(id_ticket: int) -> list[str]:

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT content
        FROM glpi_itilfollowups
        WHERE itemtype='Ticket'
        AND items_id=%s
        ORDER BY date_creation
    """, (id_ticket,))

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return [fila[0] for fila in resultados]