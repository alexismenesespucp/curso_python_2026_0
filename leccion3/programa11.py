import cProfile
import pstats

def algoritmo_ineficiente():
    # Ejemplo: Concatenación de strings en bucle (lento)
    s = ""
    for i in range(10000):
        s += str(i)
    return s

# Ejecutamos el profiler
with cProfile.Profile() as pr:
    algoritmo_ineficiente()

# Mostramos los resultados ordenados por tiempo acumulado
stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats(10) # Ver las 10 funciones más costosas