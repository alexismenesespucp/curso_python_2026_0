class ProcesadorAlgoritmico:
    def __init__(self, datos):
        self.datos = datos

    # 1. Método de instancia: Usa los datos del objeto
    def ejecutar(self):
        return sum(self.datos)

    # 2. Método de Clase: Fábrica para crear el objeto desde un string
    @classmethod
    def desde_csv(cls, cadena_csv):
        lista_datos = [int(x) for x in cadena_csv.split(",")]
        return cls(lista_datos) # Retorna una instancia de la clase

    # 3. Método Estático: Función de utilidad pura
    @staticmethod
    def validar_dato(x):
        return isinstance(x, int) and x > 0

# Uso profesional
valido = ProcesadorAlgoritmico.validar_dato(10)
instancia = ProcesadorAlgoritmico.desde_csv("1,2,3,4")
print(instancia.ejecutar())