import time

def reintento(veces, espera):
    """Decorador que reintenta una función en caso de fallo."""
    def decorador_real(func):
        def wrapper(*args, **kwargs):
            intentos = 0
            while intentos < veces:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    intentos += 1
                    print(f"Fallo {intentos}/{veces}. Reintentando en {espera}s...")
                    time.sleep(espera)
            return func(*args, **kwargs) # Último intento sin captura
        return wrapper
    return decorador_real

@reintento(veces=3, espera=2)
def conectar_servidor():
    raise ConnectionError("Servidor no responde")

conectar_servidor() # Ejecutará la lógica de reintento automáticamente