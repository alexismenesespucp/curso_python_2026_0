def fabricar_multiplicador(n):
    # 'n' queda atrapado en el closure de la función interna
    def multiplicar(x):
        return x * n
    return multiplicar

# Creamos funciones especializadas
duplicar = fabricar_multiplicador(2)
triplicar = fabricar_multiplicador(3)

print(duplicar(10)) # 20
print(triplicar(10)) # 30

# Inspección técnica: ¿Dónde vive 'n'?
print(duplicar.__closure__[0].cell_contents) # 2