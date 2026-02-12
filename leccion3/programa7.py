import multiprocessing
import time

def algoritmo_pesado(numeros):
    # Simulación de carga intensa de CPU
    return [sum(range(n)) for n in numeros]

if __name__ == "__main__":
    data = [10**7, 10**7, 10**7, 10**7]
    
    # 1. Ejecución Secuencial
    start = time.perf_counter()
    algoritmo_pesado(data)
    print(f"Secuencial: {time.perf_counter() - start:.2f}s")
    
    # 2. Ejecución Paralela (Aprovechando todos los cores)
    start = time.perf_counter()
    chunk_size = len(data) // multiprocessing.cpu_count() or 1
    with multiprocessing.Pool() as pool:
        pool.map(algoritmo_pesado, [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)])
    print(f"Paralelo: {time.perf_counter() - start:.2f}s")