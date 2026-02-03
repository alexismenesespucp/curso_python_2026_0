def fabricar_multiplicador(n,m,u):
    # 'n' queda atrapado en el closure de la función interna
    def multiplicar(x):
        return f"{u} : {x * n + m}"
    return multiplicar

# Creamos funciones especializadas
duplicar = fabricar_multiplicador(2,5, "valor")
triplicar = fabricar_multiplicador(3,10, "deuda")

print(duplicar(10)) # 20
print(triplicar(10)) # 30

# Inspección técnica: ¿Dónde vive 'n'?
print(duplicar.__closure__[1].cell_contents) # 2