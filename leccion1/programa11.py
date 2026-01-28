# 1. Enumerate: El fin de 'i = 0; i += 1'
nombres = ["Alice", "Bob", "Charlie"]
for idx, nombre in enumerate(nombres, start=1):
    print(f"Usuario {idx}: {nombre}")

# 2. Zip: Procesamiento paralelo de estructuras
precios = [100, 250, 80]
cantidades = [2, 1, 5]

# Cálculo de costo total usando zip y una expresión generadora
total = sum(p * c for p, c in zip(precios, cantidades))
print(f"Total compra: {total}")

# 3. Filter vs List Comprehension
# Extraer números primos de una lista (suponiendo función es_primo)
numeros = [2, 3, 4, 5, 6, 7, 8, 9]
primos = list(filter(es_primo, numeros))