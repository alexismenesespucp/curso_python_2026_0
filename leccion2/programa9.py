from collections import defaultdict
import json

# 1. El Mixin de infraestructura
class ExportableMixin:
    def a_json(self):
        # Convertimos el defaultdict a dict normal para serializar
        data = {k: list(v) for k, v in self._adj.items()}
        return json.dumps(data)

# 2. La Clase Core con Protocolos Dunder
class RedNeuronal(ExportableMixin):
    def __init__(self):
        # Usamos sets para evitar conexiones duplicadas automáticamente
        self._adj = defaultdict(set)

    def conectar(self, u, v):
        self._adj[u].add(v)

    def __getitem__(self, nodo):
        """Permite acceso tipo grafo['A']"""
        return self._adj[nodo]

    def __add__(self, otra):
        """Sobrecarga del operador + para fusionar grafos"""
        if not isinstance(otra, RedNeuronal):
            raise TypeError("Solo se pueden fusionar redes entre sí")
        
        nueva_red = RedNeuronal()
        # Copiamos la red actual
        for u, vecinos in self._adj.items():
            for v in vecinos: nueva_red.conectar(u, v)
        # Fusionamos la otra
        for u, vecinos in otra._adj.items():
            for v in vecinos: nueva_red.conectar(u, v)
        return nueva_red

    def __repr__(self):
        return f"RedNeuronal(nodos={len(self._adj)}, aristas={sum(len(v) for v in self._adj.values())})"

# --- PRUEBA DE FUEGO ---
red_a = RedNeuronal()
red_a.conectar("Neurona_1", "Neurona_2")

red_b = RedNeuronal()
red_b.conectar("Neurona_2", "Neurona_3")

# Fusión algorítmica elegante
red_total = red_a + red_b

print(red_total)             # RedNeuronal(nodos=2, aristas=2)
print(red_total["Neurona_2"]) # {'Neurona_3'}
print(red_total.a_json())    # {"Neurona_1": ["Neurona_2"], "Neurona_2": ["Neurona_3"]}