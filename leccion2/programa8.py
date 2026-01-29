import json

class JSONSerializerMixin:
    """Añade la capacidad de convertirse en JSON a cualquier clase."""
    def to_json(self):
        # vars(self) devuelve el __dict__ del objeto
        return json.dumps(vars(self), indent=2)

class Nodo(JSONSerializerMixin):
    def __init__(self, id, etiqueta):
        self.id = id
        self.etiqueta = etiqueta

class Conexion(JSONSerializerMixin):
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

# Ahora ambas clases tienen .to_json() sin compartir una base compleja
n = Nodo(1, "Server_01")
print(n.to_json())