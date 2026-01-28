# Definición formal: objeto[start:stop:step]
data = list(range(20))

# 1. Extracción de patrones
pares = data[::2]      # [0, 2, 4, ..., 18]
invertido = data[::-1]  # Inversión total en una línea

# 2. Modificación in-place (Potentísimo)
# Podemos reemplazar una sección del array por otra de distinto tamaño
data[1:5] = [99, 99] 
print(f"Data tras reemplazo: {data}") # El array se encoge automáticamente

# 3. El objeto slice (Para desacoplar la lógica)
# Imaginen que procesan archivos de ancho fijo
CAMPO_NOMBRE = slice(0, 10)
CAMPO_EDAD = slice(10, 13)

linea = "Juan Perez 030"
print(f"Nombre: '{linea[CAMPO_NOMBRE]}', Edad: {linea[CAMPO_EDAD]}")