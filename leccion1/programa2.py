import sys
import gc

# Creamos un objeto y vemos cuántos 'nombres' lo conocen
data = {"clave": "valor"}
print(f"Referencias iniciales: {sys.getrefcount(data) - 1}") # El -1 es por el llamado a la función

# Referencia circular: El objeto se apunta a sí mismo
contenedor = []
contenedor.append(contenedor) 

del contenedor # Borramos el nombre, pero el objeto vive en el limbo (ref_count > 0)

# Forzamos la limpieza de ciclos
encontrados = gc.collect()
print(f"Objetos basura detectados por el GC: {encontrados}")