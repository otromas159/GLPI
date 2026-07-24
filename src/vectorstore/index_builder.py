import json
from pathlib import Path

from src.vectorstore.chroma_manager import coleccion


def construir_indice():

    carpeta = Path("knowledge_cases")

    for archivo in carpeta.glob("*.json"):

        with open(archivo, encoding="utf8") as f:

            conocimiento = json.load(f)

        documento = f"""
Problema

{conocimiento["problema"]}

Acciones

{" ".join(conocimiento["acciones"])}

Solución

{conocimiento["solucion"]}
"""

        coleccion.add(

            ids=[str(conocimiento["id"])],

            documents=[documento],

            metadatas=[

                {

                    "categoria": conocimiento["categoria"]

                }

            ]

        )

        print(f"Indexado Ticket #{conocimiento['id']}")