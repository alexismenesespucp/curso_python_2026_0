# 1. Funciones en estructuras de datos
def suma(a, b): return a + b
def resta(a, b): return a - b

operaciones = {
    "add": suma,
    "sub": resta,
    "mul": lambda a, b: a * b # Función anónima rápida
}

# Ejecución dinámica según lógica algorítmica
op = "mul"
resultado = operaciones[op](10, 5) # 50

# 2. Funciones como argumentos (Higer-order functions)
def aplicar_transformacion(datos, func):
    """Aplica una lógica arbitraria a una colección."""
    return [func(x) for x in datos]

sensores = [10.5, 12.2, 9.8]
# Pasamos la función interna de Python 'round' como parámetro
print(aplicar_transformacion(sensores, round)) # [10, 12, 10]