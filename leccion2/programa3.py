class Motor:
    def __init__(self, temperatura_inicial):
        self._temperatura = temperatura_inicial # Convención de 'privado'

    @property
    def temperatura(self):
        """Getter: Se accede como motor.temperatura"""
        print("Leyendo sensor térmico...")
        return f"{self._temperatura}°C"

    @temperatura.setter
    def temperatura(self, valor):
        """Setter: Se accede como motor.temperatura = 90"""
        if valor > 120:
            raise ValueError("¡Sobrecalentamiento crítico!")
        print(f"Ajustando temperatura a {valor}")
        self._temperatura = valor

# Uso profesional
m = Motor(20)
print(m.temperatura)  # Acceso como atributo, pero llama al método
m.temperatura = 130    # Validación transparente