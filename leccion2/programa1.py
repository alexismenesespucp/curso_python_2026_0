class Singleton:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        # Si no existe la instancia, la creamos
        if cls._instancia is None:
            print("Creando el objeto físico en memoria...")
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, valor):
        print("Configurando el objeto...")
        self.valor = valor

# Prueba: Ambos nombres apuntan al MISMO ID de memoria
s1 = Singleton(10)
s2 = Singleton(20)
print(f"ID S1: {id(s1)} | ID S2: {id(s2)}") # Son idénticos
print(s1.valor) # 20 (S2 sobreescribió el valor del único objeto existente)