# Demostración de la jerarquía y nonlocal
contador = 10
def cronometro():
    contador = 0  # Ámbito Enclosing
    
    def incrementar():
        nonlocal contador # Sin esto, Python lanzaría UnboundLocalError al asignar
        contador += 1
        return contador
    
    return incrementar

mi_contador = cronometro()
print(mi_contador()) # 1
print(mi_contador()) # 2

# Nota: Si usas 'global', buscarías fuera de cronometro(), 
# rompiendo la encapsulación del objeto.