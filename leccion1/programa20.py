# Data compleja: Lista de tuplas (Producto, Precio, Stock)
inventario = [
    ("Laptop", 1200, 5),
    ("Mouse", 25, 50),
    ("Monitor", 300, 15),
    ("Teclado", 80, 15)
]

# 1. Ordenar por Precio (segundo elemento)
orden_precio = sorted(inventario, key=lambda x: x[1])
print(orden_precio)
# 2. Ordenar por Stock (descendente) y luego por Nombre (ascendente)
# Aprovechamos que Python permite devolver tuplas en la clave
orden_mixto = sorted(inventario, key=lambda x: (-x[2], x[0]))
print(orden_mixto)
print(f"Top Stock: {orden_mixto[0]}")

# 3. Lambda con Diccionarios
users = [{"name": "Zoe", "age": 30}, {"name": "Alex", "age": 20}]
users.sort(key=lambda u: u["age"]) # Ordena in-place por edad
print(users)