class Base:
    def mensaje(self):
        print("Mensaje desde Base")

class LoggerMixin(Base):
    def mensaje(self):
        print("Logueando acción...")
        super().mensaje() # ¿A quién llama aquí?

class ValidadorMixin(Base):
    def mensaje(self):
        print("Validando datos...")
        super().mensaje()

class SistemaFinal(ValidadorMixin, LoggerMixin):
    pass

# Prueba del flujo
s = SistemaFinal()
s.mensaje()

# Inspección del MRO: El orden jerárquico real
print(SistemaFinal.__mro__)
# Output: (SistemaFinal, ValidadorMixin, LoggerMixin, Base, object)