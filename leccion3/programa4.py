from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

urls = ["https://google.com", "https://python.org", "https://github.com"]

def descargar(url):
    with urllib.request.urlopen(url) as response:
        return f"{url}: {response.status}"

# Cambiar de hilos a procesos es tan fácil como cambiar el nombre del Executor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Lanzamos todas las tareas
    futuros = {executor.submit(descargar, url): url for url in urls}
    
    for futuro in as_completed(futuros):
        url = futuros[futuro]
        try:
            data = futuro.result() # Aquí esperamos el resultado
            print(data)
        except Exception as e:
            print(f"{url} generó un error: {e}")