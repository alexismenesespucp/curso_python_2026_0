import threading
import time

def tarea_io_pesada(id):
    print(f"Hilo {id} esperando respuesta de red...")
    time.sleep(2) # Simula latencia de red
    print(f"Hilo {id} finalizado.")

# Creamos 5 hilos
hilos = []
for i in range(5):
    t = threading.Thread(target=tarea_io_pesada, args=(i,))
    hilos.append(t)
    t.start()

# Esperamos a que todos terminen
for t in hilos:
    t.join()

print("Todas las peticiones terminaron en ~2 segundos, no en 10.")