# Lo que Python hace bajo el capó en un 'for'
data = [10, 20, 30]
it = iter(data) # Llama a data.__iter__()

try:
    while True:
        elemento = next(it) # Llama a it.__next__()
        print(f"Procesando: {elemento}")
except StopIteration:
    # El algoritmo de Python detecta el fin de la estructura
    print("Fin de la secuencia alcanzado de forma segura.")

# Implementación rápida de un Iterador Infinito (Algoritmo de ID único)
class Contador:
    def __init__(self, inicio):
        self.num = inicio
    def __iter__(self): return self
    def __next__(self):
        val = self.num
        self.num += 1
        return val

ids = Contador(1000)
print(next(ids)) # 1000
print(next(ids)) # 1001 (Consumo de memoria constante: O(1))