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

# Al llamar a la función, realmente ejecutamos el wrapper
#algoritmo_complejo(1_000_000)
def registrar_metodos(cls):
    """Envuelve todos los métodos de la clase para loguear su llamada."""
    for nombre, valor in vars(cls).items():
        if callable(valor):
            # Envolvemos el método (usando un decorador simple)
            setattr(cls, nombre, medir_tiempo(valor)) 
    return cls

@registrar_metodos
class CalculoCientifico:
    def simulacion_a(self):
        time.sleep(0.5)
    
    def simulacion_b(self):
        time.sleep(0.3)

# Ahora, cualquier instancia de esta clase tendrá logueo automático en sus métodos
calc = CalculoCientifico()
calc.simulacion_b()