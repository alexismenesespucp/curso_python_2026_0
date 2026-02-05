import sys
class ErrorDeValidacion(Exception):
    """Clase base para errores de nuestro sistema."""
    sys.exit(1)
    #pass

class SensorFueraDeRangoError(ErrorDeValidacion):
    def __init__(self, sensor_id, valor, limite):
        self.message = f"Sensor {sensor_id} reportó {valor}, excediendo el límite de {limite}"
        super().__init__(self.message)

# Uso en el algoritmo
def leer_sensor(id):
    valor = 150 # Simulación
    if valor > 100:
        raise SensorFueraDeRangoError(id, valor, 100)

try:
    leer_sensor("TEMP_01")
except SensorFueraDeRangoError as e:
    # Loguear el error y tomar acción correctiva
    print(f"ALERTA: {e}")
print("Continuar")