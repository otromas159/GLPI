import json
import os
from dataclasses import asdict


def exportar_conocimiento(conocimiento):

    carpeta = "knowledge"

    os.makedirs(carpeta, exist_ok=True)

    ruta = os.path.join(
        carpeta,
        f"{conocimiento.id}.json"
    )

    with open(
        ruta,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            asdict(conocimiento),
            archivo,
            indent=4,
            ensure_ascii=False
        )