from collections import Counter

# RETO: ¿Son anagramas? (Mismas letras, distinto orden)
str1 = "pythonico"
str2 = "typhoconi"

# Enfoque A: Tradicional (Algoritmos 101)
def es_anagrama_tradicional(s1, s2):
    if len(s1) != len(s2): return False
    # ... lógica de conteo manual con bucles ...
    return sorted(s1) == sorted(s2) # O(n log n)

# Enfoque B: Pythonic (Uso de tablas de hash nativas)
def es_anagrama_pro(s1, s2):
    # Counter es O(n) y la comparación de dicts en Python es muy eficiente
    return Counter(s1) == Counter(s2)

print(f"¿Son anagramas?: {es_anagrama_pro(str1, str2)}")