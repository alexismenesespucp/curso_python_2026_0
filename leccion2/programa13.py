# Una metaclase hereda de 'type'
class MetaValidadora(type):
    def __new__(cls, nombre, bases, dct):
        # Interceptamos la creación de la clase
        print(f"Analizando la clase: {nombre}")
        
        # Regla algorítmica: Todas las clases deben tener un método 'ejecutar'
        if 'ejecutar' not in dct:
            raise TypeError(f"Error Crítico: La clase {nombre} no implementa 'ejecutar'")
            
        return super().__new__(cls, nombre, bases, dct)

# Uso de la metaclase
class AlgoritmoValido(metaclass=MetaValidadora):
    def ejecutar(self):
        pass

# class AlgoritmoInvalido(metaclass=MetaValidadora):
#     pass # Esto lanzaría un TypeError al momento de IMPORTAR el script