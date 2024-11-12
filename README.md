# Market Basket Analysis con Neo4j

Este proyecto implementa un análisis de **Market Basket** utilizando técnicas de co-ocurrencia y detección de comunidades en un grafo basado en Neo4j. El objetivo es encontrar patrones de co-ocurrencia entre productos y detectar comunidades de productos que frecuentemente se compran juntos.

## Descripción

El proyecto consta de una clase llamada `MarketBasket` que permite:

1. **Obtener transacciones de productos** desde una base de datos Neo4j.
2. **Encontrar conjuntos de artículos frecuentes** que se compran juntos usando un umbral mínimo `k`.
3. **Construir un grafo de co-ocurrencia** para representar las relaciones de co-ocurrencia entre productos.
4. **Detectar comunidades** en el grafo utilizando técnicas de búsqueda en profundidad (DFS) o búsqueda en amplitud (BFS).

## Requisitos

- Python 3.12
- Neo4j
- Bibliotecas de Python:
    - `neo4j`: Para interactuar con la base de datos Neo4j.
    - `networkx`: Para representar y manipular grafos.
    - `matplotlib`: Para visualizar grafos.
    - `collections`: Para manejar estructuras de datos como diccionarios y colas.
    - `os`: Para acceder a las variables de entorno.

Puedes instalar las dependencias usando `pip`:

```bash
pip install neo4j networkx matplotlib
```