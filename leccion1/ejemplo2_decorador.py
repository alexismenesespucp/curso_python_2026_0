USUARIO_AUTENTICADO = False

def require_autentication(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return wrapper

@require_autentication
def eliminar_base_datos():
    print("Base de datos eliminada")

print("Intento 1(No logueado)")
eliminar_base_datos()

USUARIO_AUTENTICADO = True

print("Intento 2(Autenticado)")

eliminar_base_datos()