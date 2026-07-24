from src.database.connection import obtener_conexion


def obtener_solucion(id_ticket: int) -> str:

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT content
        FROM glpi_itilsolutions
        WHERE itemtype='Ticket'
        AND items_id=%s
        LIMIT 1
    """, (id_ticket,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado:
        return resultado[0]

    return ""