usuarios = [
    {"id": 1, "username": "admin", "status": "active"},
    {"id": 2, "username": "editor", "status": "inactive"},
    {"id": 3, "username": "guest", "status": "active"}
]

# 1. Dict Comprehension: Crear un mapa de búsqueda rápido (ID -> Username)
# Solo para usuarios activos
mapa_usuarios = {u["id"]: u["username"] for u in usuarios if u["status"] == "active"}
print(mapa_usuarios) # {1: 'admin', 3: 'guest'}

# 2. Set Comprehension: Extraer dominios únicos de una lista de emails
emails = ["dev@google.com", "boss@google.com", "user@python.org", "dev@google.com"]
dominios = {e.split("@")[1] for e in emails}
print(dominios) # {'google.com', 'python.org'} -> Deduplicación automática $O(n)$