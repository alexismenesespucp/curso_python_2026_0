from collections import deque

# 1. Buffer circular: Solo guarda los últimos 5 elementos
historial = deque(maxlen=5)

for i in range(10):
    historial.append(f"Evento_{i}")
    print(list(historial)) # Observen cómo 'Evento_0' desaparece solo

# 2. Eficiencia comparada (Algoritmos de búsqueda)
# En un BFS (Búsqueda en anchura), el uso de pop(0) en listas destruye el performance.
# Usemos popleft() en deque para garantizar O(1).
queue = deque(["nodo_raiz"])
while queue:
    actual = queue.popleft() # Eficiente
    # ... procesar hijos ...
    queue.append("hijo_n")