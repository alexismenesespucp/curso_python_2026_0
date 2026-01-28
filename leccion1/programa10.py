# 1. Operaciones de conjuntos (Sintaxis matemática pura)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a & set_b) # Intersección: {3, 4}
print(set_a | set_b) # Unión: {1, 2, 3, 4, 5, 6}
print(set_a - set_b) # Diferencia: {1, 2}

# 2. El poder del Frozenset
nodos_visitados = frozenset([10, 20, 30])
memoizacion = {
    nodos_visitados: "Ruta_Optima_A"
}

# 3. Rendimiento comparado
# Buscar en una lista de 10^6 elementos: milisegundos.
# Buscar en un set de 10^6 elementos: nanosegundos.