# 1. Unión moderna de diccionarios (Merge)
config_base = {"visibilidad": True, "timeout": 30}
config_usuario = {"timeout": 60, "tema": "dark"}

# El operador | crea un nuevo dict. El operador |= actualiza in-place.
config_final = config_base | config_usuario 
print(config_final) # {'visibilidad': True, 'timeout': 60, 'tema': 'dark'}

# 2. Diccionarios por comprensión (Dict Comprehension)
# Ejemplo: Invertir un mapa de ID -> Nombre a Nombre -> ID
id_to_name = {101: "Alice", 102: "Bob", 103: "Charlie"}
name_to_id = {v: k for k, v in id_to_name.items()}

# 3. La eficiencia de las Vistas
claves = id_to_name.keys()
id_to_name[104] = "Dave"
print(104 in claves) # True (La vista se actualizó sin re-calcular nada)