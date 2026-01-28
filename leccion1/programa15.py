import sys

# 1. Comparación de peso en memoria
# Lista: Calcula y guarda 10 millones de elementos
millon_lista = [x**2 for x in range(10_000_000)]
print(f"Memoria lista: {sys.getsizeof(millon_lista) / 1024**2:.2f} MB")

# Generador: Solo guarda la "fórmula" para crearlos
millon_gen = (x**2 for x in range(10_000_000))
print(f"Memoria generador: {sys.getsizeof(millon_gen)} bytes") # ¡Casi nada!

# 2. Uso práctico en algoritmos de reducción
# sum() acepta un generador directamente. No creamos la lista intermedia.
total_pares = sum(x for x in range(1_000_000) if x % 2 == 0)