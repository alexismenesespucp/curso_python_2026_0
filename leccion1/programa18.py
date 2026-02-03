import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        # Ejecutamos la función original
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"Función {func.__name__} tardó {fin - inicio:.6f}s")
        return resultado
    return wrapper

@medir_tiempo
def algoritmo_complejo(n):
    # Simulación de carga algorítmica
    return sum(i**2 for i in range(n))

@medir_tiempo
def contar_hasta(n):
    for i in range(n):
        i*1
    return True
    
contar_hasta(3000000)

# Al llamar a la función, realmente ejecutamos el wrapper
algoritmo_complejo(1_000_000)