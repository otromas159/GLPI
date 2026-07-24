from src.vectorstore.chroma_manager import coleccion


def buscar(texto, cantidad=5):

    resultados = coleccion.query(

        query_texts=[texto],

        n_results=cantidad

    )

    return resultados