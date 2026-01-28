# 1. Captura específica vs genérica
try:
    resultado = 10 / int(input("Divisor: "))
except ValueError as e:
    print(f"Error de entrada: Debes ingresar un número. Detalle: {e}")
except ZeroDivisionError:
    print("Error algorítmico: No se puede dividir por cero.")
except Exception as e:
    # Solo como último recurso, capturamos lo inesperado
    print(f"Error imprevisto de tipo {type(e).__name__}: {e}")