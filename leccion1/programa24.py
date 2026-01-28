# --- CÓDIGO "SMELLY" (ESTILO C/JAVA ANTIGUO) ---
def procesar_logs_feo(lista_logs):
    resultado = {}
    for log in lista_logs:
        if "error" in log:
            partes = log.split(":")
            usuario = partes[1]
            if usuario not in resultado:
                resultado[usuario] = []
            resultado[usuario].append(partes[2])
    return resultado

# --- CÓDIGO PYTHONIC (ESTILO SENIOR) ---
from collections import defaultdict

def procesar_logs_pro(lista_logs):
    # Usamos defaultdict para eliminar el 'if usuario not in resultado'
    errores_por_usuario = defaultdict(list)
    
    for log in lista_logs:
        try:
            # Unpacking avanzado para parsear el log
            _, usuario, mensaje = log.split(":")
        except ValueError:
            continue # Ignorar logs mal formateados
        else:
            if "error" in log.lower():
                errores_por_usuario[usuario].append(mensaje)
                
    return dict(errores_por_usuario)