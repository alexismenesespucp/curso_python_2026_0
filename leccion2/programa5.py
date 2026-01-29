class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        # Permitimos sumar Vector + Vector
        if isinstance(otro, Vector):
            return Vector(self.x + otro.x, self.y + otro.y)
        raise TypeError("Solo se pueden sumar vectores entre sí")

    def __eq__(self, otro):
        # Definimos cuándo dos vectores son "iguales" algorítmicamente
        return self.x == otro.x and self.y == otro.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(1, 3)
v3 = v1 + v2  # Llama a v1.__add__(v2) bajo el capó
print(v3)     # Vector(3, 7)
print(v1 == Vector(2, 4)) # True