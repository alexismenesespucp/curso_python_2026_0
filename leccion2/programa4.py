class Sensor:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        # Lo que ve el cliente: "Sensor Temperatura: 25.5"
        return f"Sensor {self.nombre}: {self.valor}"

    def __repr__(self):
        # Lo que ve el dev: "Sensor(nombre='Temperatura', valor=25.5)"
        return f"Sensor(nombre={self.nombre!r}, valor={self.valor!r})"

# Prueba en consola
s = Sensor("Voltaje", 220)
print(s)
print(str(s))  # Para reportes
print(repr(s)) # Para debugging técnico/logs