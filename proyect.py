from itertools import combinations
from collections import defaultdict


def frequent_itemsets(transactions, k):

    # Creación de diccionario para almacenar el conteo de cada conjunto de artículos
    dic_conteo = defaultdict(int)

    # Para obtener el conjunto de todos los artículos
    articulos = set(articulo for transaccion in transactions for articulo in transaccion)

    for tam_subcon in range(2, len(articulos)+1):
        #Generar todos los subconjuntos de longitud tam_subcon
        for transaccion in transactions:
            for subconjunto in combinations(transaccion, tam_subcon):
                dic_conteo[frozenset(subconjunto)] += 1

    # Para seleccionar solo los subconjuntos que aparecen al menos "K" veces
    resultado = [set(conjunto) for conjunto, conteo in dic_conteo.items() if conteo >= k]

    return resultado



def construir_grafo_coocurrencia(transacciones, k):
    # Diccionario para contar la co-ocurrencia entre cada par de artículos
    conteo_coocurrencia = defaultdict(int)

    # Contar co-ocurrencias de pares de artículos en las transacciones
    for transaccion in transacciones:
        for articulo1, articulo2 in combinations(transaccion, 2):
            conteo_coocurrencia[frozenset([articulo1, articulo2])] += 1

    # Grafo de co-ocurrencia
    grafo_coocurrencia = defaultdict(set)

    # Crear aristas en el grafo para pares de artículos que cumplen con el umbral k
    for par, conteo in conteo_coocurrencia.items():
        if conteo >= k:
            articulo1, articulo2 = list(par)
            grafo_coocurrencia[articulo1].add(articulo2)
            grafo_coocurrencia[articulo2].add(articulo1)

    return grafo_coocurrencia



def encontrar_comunidades(grafo):
    # Conjunto para llevar registro de nodos visitados
    visitados = set()
    comunidades = []

    # Función auxiliar para DFS
    def dfs(nodo, comunidad):
        # Marcar el nodo como visitado y añadirlo a la comunidad actual
        visitados.add(nodo)
        comunidad.append(nodo)
        # Recorrer nodos adyacentes
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                dfs(vecino, comunidad)

    # Encontrar todos los componentes conectados
    for nodo in grafo:
        if nodo not in visitados:
            comunidad = []
            dfs(nodo, comunidad)
            comunidades.append(comunidad)

    return comunidades



transacciones = [
    {"leche", "pan", "huevos", "cereal", "jugo"},
    {"leche", "pan", "huevos"},
    {"leche", "jugo", "cereal"},
    {"cereal", "jugo", "mantequilla", "pan"},
    {"huevos", "pan", "jugo"},
    {"leche", "huevos", "jugo"},
    {"pan", "mantequilla", "miel"},
    {"leche", "pan", "huevos", "miel"},
    {"cereal", "jugo", "pan"},
    {"leche", "pan", "huevos", "cereal", "jugo"},
    {"miel", "cereal", "jugo"},
    {"leche", "mantequilla", "huevos", "pan"},
    {"miel", "huevos", "pan"},
    {"cereal", "leche", "miel"},
    {"jugo", "huevos", "pan"},
    {"pan", "jugo", "huevos", "leche"},
    {"cereal", "leche", "huevos", "miel"},
    {"leche", "jugo", "cereal", "miel"},
    {"pan", "jugo", "huevos", "leche", "miel"},
    {"huevos", "mantequilla", "pan"},
    {"cereal", "pan", "jugo"},
    {"leche", "pan", "huevos", "cereal"},
    {"mantequilla", "pan", "cereal"},
    {"miel", "cereal", "jugo", "pan"},
    {"huevos", "pan", "leche", "cereal"},
    {"pan", "jugo", "huevos"},
    {"cereal", "mantequilla", "miel", "pan"},
    {"leche", "miel", "jugo"},
    {"pan", "jugo", "leche", "miel"},
    {"huevos", "jugo", "pan", "miel"}
]


k = 3
print(frequent_itemsets(transacciones, k))
grafo = construir_grafo_coocurrencia(transacciones, k)
print(grafo)
print(encontrar_comunidades(grafo))
