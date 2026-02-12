import asyncio
import httpx # Librería asíncrona moderna
import time

async def descargar_url(client, url):
    resp = await client.get(url)
    return resp.status_code

async def main():
    urls = ["https://www.google.com"] * 50
    
    async with httpx.AsyncClient() as client:
        start = time.perf_counter()
        # Disparamos 50 peticiones simultáneamente
        tareas = [descargar_url(client, url) for url in urls]
        resultados = await asyncio.gather(*tareas)
        
        end = time.perf_counter()
        print(f"50 peticiones terminadas en {end - start:.2f}s")
        print(f"Resultados (primeros 5): {resultados[:5]}")

# asyncio.run(main())