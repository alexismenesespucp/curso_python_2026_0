import multiprocessing
import os

def calcular_cuadrado(n):
    # Esto se ejecuta en un núcleo distinto
    print(f"Proceso {os.getpid()} calculando...")
    return n * n

if __name__ == "__main__":
    numeros = [10**6, 10**7, 10**8]
    
    # Creamos un pool de procesos (normalmente igual al # de núcleos)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        resultados = pool.map(calcular_cuadrado, numeros)
    
    print(f"Resultados finales: {resultados}")