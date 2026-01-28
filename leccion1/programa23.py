def procesar_archivo(ruta):
    f = None
    try:
        f = open(ruta, 'r')
        datos = f.read()
    except FileNotFoundError:
        print("El archivo no existe.")
    else:
        # Solo entramos aquí si el archivo se leyó bien
        print(f"Procesados {len(datos)} caracteres.")
        return datos.upper()
    finally:
        # Garantizamos el cierre del recurso
        if f:
            f.close()
            print("Recurso liberado.")

# Nota: Veremos que 'with' (Context Managers) automatiza esto, 
# pero es vital entender el flujo base.