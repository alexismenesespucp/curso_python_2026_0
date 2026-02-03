def guardar_datos(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@guardar_datos
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

import time

inicio = time.time()
print(f"Fibonacci de 35:{fibonacci(35)}")
fin = time.time()

print(f"Tiempo de ejecución:{fin-inicio}")