import chromadb

cliente = chromadb.PersistentClient(
    path="./chroma"
)

coleccion = cliente.get_or_create_collection(
    name="glpi_cases"
)