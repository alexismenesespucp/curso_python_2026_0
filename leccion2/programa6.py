class DatasetPro:
    """Simula una lista que carga datos bajo demanda."""
    def __init__(self, size):
        self._data = [None] * size

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        # Aquí podrías poner lógica de carga de base de datos
        print(f"Accediendo al índice {index}...")
        return self._data[index]

    def __setitem__(self, index, valor):
        print(f"Guardando {valor} en posición {index}...")
        self._data[index] = valor

# Uso profesional
db = DatasetPro(100)
db[5] = "Muestra_A" # Llama a __setitem__
item = db[5]         # Llama a __getitem__
print(f"Total elementos: {len(db)}") # Llama a __len__

print(db)