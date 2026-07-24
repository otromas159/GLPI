from pprint import pprint

from src.vectorstore.search import buscar

consulta = """
No puedo imprimir cheques desde Dynamics
"""

resultado = buscar(consulta)

pprint(resultado)