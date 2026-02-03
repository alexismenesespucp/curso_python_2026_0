from collections import namedtuple
from dataclasses import dataclass

# 1. Namedtuple: Inmutable, ligera como una tupla, legible como un objeto

Punto = namedtuple('Punto', ['x', 'y', 'z'])
p1 = Punto(10, 20, 30)
# p1.x = 50  # Lanza AttributeError: Inmutabilidad garantizada

# 2. Dataclass: El estándar moderno para POO de datos
@dataclass(slots=True) # slots=True elimina el __dict__ y ahorra memoria masiva
class Nodo:
    id: int
    label: str
    peso: float = 1.0

n1 = Nodo(1, "Inicio", 5.5)
print(n1) # Genera automáticamente un __repr__ útil: Nodo(id=1, label='Inicio', peso=5.5)