class GestionDeRecurso:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print(f"--- [SETUP] Reservando recurso: {self.nombre} ---")
        return self # Este es el objeto que recibe la variable 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type nos dice si hubo un error para poder hacer rollback si es necesario
        print(f"--- [TEARDOWN] Liberando recurso: {self.nombre} ---")
        if exc_type:
            print(f"LOG: El proceso falló con {exc_type.__name__}, pero el recurso se cerró igual.")
        return False # Permitir que la excepción se propague

# Uso profesional
try:
    with GestionDeRecurso("BaseDeDatos_Produccion") as db:
        print("Ejecutando consultas pesadas...")
        raise RuntimeError("Fallo de red") # Simulación de error
except Exception:
    pass