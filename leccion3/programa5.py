import asyncio

async def tarea_asincrona(nombre, demora):
    print(f"Tarea {nombre}: Iniciando (esperará {demora}s)")
    # 'await' cede el control al Event Loop. No bloquea el hilo.
    await asyncio.sleep(demora) 
    print(f"Tarea {nombre}: Finalizada")
    return f"Resultado de {nombre}"

async def main():
    # Lanzamos tareas concurrentes en el mismo hilo
    print("Iniciando orquestador...")
    t1 = asyncio.create_task(tarea_asincrona("A", 2))
    t2 = asyncio.create_task(tarea_asincrona("B", 1))
    
    # Esperamos a que ambas terminen
    r1 = await t1
    r2 = await t2
    print(f"Resultados: {r1}, {r2}")

# Punto de entrada para el mundo asíncrono
if __name__ == "__main__":
    asyncio.run(main())