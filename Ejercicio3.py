import heapq

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.vecinos = {}
        self.distancia = {}

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)

    def agregar_arista(self, origen, destino, distancia):
        self.vecinos.setdefault(origen, []).append(destino)
        self.vecinos.setdefault(destino, []).append(origen)
        self.distancia[(origen, destino)] = distancia
        self.distancia[(destino, origen)] = distancia

def dijkstra(grafo, origen):
    cola = [(0, origen)]
    visitados = set()
    distancia_minima = {origen: 0}
    padres = {}
    while cola:
        (distancia, nodo_actual) = heapq.heappop(cola)
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        for vecino in grafo.vecinos[nodo_actual]:
            distancia_total = distancia + grafo.distancia[(nodo_actual, vecino)]
            if vecino not in distancia_minima or distancia_total < distancia_minima[vecino]:
                distancia_minima[vecino] = distancia_total
                padres[vecino] = nodo_actual  # Almacenar el nodo padre
                heapq.heappush(cola, (distancia_total, vecino))
    return distancia_minima, padres

def reconstruir_ruta(padres, origen, destino):
    ruta = [destino]
    while destino != origen:
        destino = padres[destino]
        ruta.append(destino)
    ruta.reverse()
    return ruta

# Crear el grafo de la Tierra Media
tierra_media = Grafo()
tierra_media.agregar_nodo("Rivendell")
tierra_media.agregar_nodo("Minas Tirith")
tierra_media.agregar_nodo("Moria")
tierra_media.agregar_nodo("Bree")
tierra_media.agregar_nodo("Gondor")

tierra_media.agregar_arista("Rivendell", "Minas Tirith", 120)
tierra_media.agregar_arista("Rivendell", "Moria", 100)
tierra_media.agregar_arista("Minas Tirith", "Gondor", 150)
tierra_media.agregar_arista("Minas Tirith", "Bree", 80)
tierra_media.agregar_arista("Bree", "Gondor", 100)
tierra_media.agregar_arista("Gondor", "Moria", 200)

# Calcular la ruta más corta desde Rivendell a todas las demás ciudades
distancia_minima, padres = dijkstra(tierra_media, "Rivendell")

# Imprimir las distancias mínimas desde Rivendell a todas las ciudades
for ciudad, distancia in distancia_minima.items():
    print(f"Distancia mínima desde Rivendell a {ciudad}: {distancia}")

# Reconstruir la ruta óptima desde Rivendell a Gondor
origen = "Rivendell"
destino = "Gondor"
ruta_optima = reconstruir_ruta(padres, origen, destino)
print(f"Ruta óptima desde {origen} hasta {destino}: {' -> '.join(ruta_optima)}")
