import asyncio

async def fetch_data(id):
    print(f"Consultando ID {id}...")
    await asyncio.sleep(0.5) # Simula I/O asíncrono
    return {"id": id, "data": "info"}

async def main():
    # El poder de asyncio.gather: 
    # Ejecuta una lista de corrutinas en paralelo y espera sus resultados.
    ids = [1, 2, 3, 4, 5]
    tareas = [fetch_data(i) for i in ids]
    
    resultados = await asyncio.gather(*tareas)
    print(f"Procesados {len(resultados)} elementos.")

# Ejecución
# asyncio.run(main())