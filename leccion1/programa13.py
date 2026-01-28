# Objetivo: Procesar una matriz de datos y extraer los cuadrados de los pares
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1. Aplanamiento y filtrado en una línea (Nested Comprehension)
# Estructura: [expresion for sublista in matriz for elemento in sublista if condicion]
pares_cuadrados = [x**2 for fila in matriz for x in fila if x % 2 == 0]
print(f"Pares al cuadrado: {pares_cuadrados}") # [4, 16, 36, 64]

# 2. Lógica IF-ELSE dentro de la comprensión
# Si el número es >= 5, lo dejamos igual; si no, ponemos 0
ajuste = [x if x >= 5 else 0 for fila in matriz for x in fila]