from collections import defaultdict, Counter, deque

# 1. Grafos rápidos con defaultdict
# Evita el error 'KeyError' y la lógica de inicialización manual
grafo = defaultdict(list)
conexiones = [('A', 'B'), ('A', 'C'), ('B', 'D')]

for origen, destino in conexiones:
    grafo[origen].append(destino) # No requiere verificar si el origen existe

# 2. Análisis de frecuencias (Counter)
texto = "python es rapido porque python usa c"
frecuencias = Counter(texto.split())
print(f"Top 2 palabras: {frecuencias.most_common(2)}")

# 3. Deque para algoritmos de BFS (Breadth-First Search)
cola = deque(["tarea1", "tarea2"])
cola.append("tarea3")      # O(1) al final
cola.appendleft("urgente") # O(1) al inicio (En lista normal sería O(n))
print(f"Siguiente a procesar: {cola.popleft()}")