SOFTWARES = {

    "outlook": "Outlook",
    "excel": "Excel",
    "word": "Word",
    "powerpoint": "PowerPoint",

    "windows": "Windows",
    "linux": "Linux",

    "glpi": "GLPI",

    "dynamics": "Dynamics 365",

    "mysql": "MySQL",
    "sql": "SQL Server",

    "office": "Microsoft Office",

    "teams": "Teams",

    "chrome": "Google Chrome",

    "edge": "Microsoft Edge",

    "firefox": "Firefox",

    "acrobat": "Adobe Acrobat",

    "pdf": "PDF",

    "sharepoint": "SharePoint"

}
def enriquecer_software(knowledge):

    texto = (
        knowledge.problema
        + " "
        + knowledge.solucion
    ).lower()

    encontrados = []

    for palabra, nombre in SOFTWARES.items():

        if palabra in texto:

            encontrados.append(nombre)

    knowledge.software = sorted(set(encontrados))

    return knowledge