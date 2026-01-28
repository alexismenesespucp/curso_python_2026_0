# Caso A: El peligro de la mutabilidad (Listas)
original = [1, 2, 3]
alias = original 
alias.append(99)

print(f"¿Misma identidad?: {id(original) == id(alias)}") # True
print(f"Original modificado: {original}") # [1, 2, 3, 99]

# Caso B: Inmutabilidad y 'Re-binding' (Enteros)
a = 1000
print(f"ID inicial: {id(a)}")
a = a + 1 
print(f"ID final:   {id(a)}") # El ID CAMBIA. El objeto '1000' sigue igual en memoria.

# Caso C: La excepción de los objetos pequeños (Interning)
m, n = 10, 10
print(m is n) # True. Python pre-asigna enteros del -5 al 256 para optimizar.

# El curso es bastante interesante
