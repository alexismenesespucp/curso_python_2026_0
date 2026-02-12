from typing import List, Optional, Union

# Definición con anotaciones de tipo
def procesar_ids(ids: List[Union[int, str]], prefix: Optional[str] = None) -> List[str]:
    resultado: List[str] = []
    for id_val in ids:
        clean_id = str(id_val).strip()
        if prefix:
            resultado.append(f"{prefix}_{clean_id}")
        else:
            resultado.append(clean_id)
    return resultado

# Esto pasaría el linter de tipos
print(procesar_ids([101, " 102 "], prefix="USR"))

# Esto lanzaría una alerta en el IDE/Mypy inmediatamente
# procesar_ids(101) # Error: Se esperaba una lista