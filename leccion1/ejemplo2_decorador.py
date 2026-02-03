usuarios = {"Pepito": "admin","juancito":"user", "pancracio":"guest"}
usuario = ""
funciones_permitidas_por_usuario = ("check_status")

def require_autentication(func):
    def wrapper(*args,**kwargs):
        if usuarios[usuario] == "admin":
            func(*args,**kwargs)
            return True
        elif usuarios[usuario] == "user":
            if func.__name__ in funciones_permitidas_por_usuario:
                func(*args,**kwargs)
                return True
        print(f" No se puede ejecutar la funcion: {func.__name__} con el usuario {usuario}")
        return False
    return wrapper

@require_autentication
def eliminar_base_datos():
    print("Base de datos eliminada")

@require_autentication
def agregar_usuario(nombre):
    print(f"Agregando usuario: {nombre}")

@require_autentication
def check_status():
    print("Estado verificado")

usuario = "Pepito"
eliminar_base_datos()

usuario = "juancito"
agregar_usuario("donatela")

usuario = "Pepito"
check_status()

usuario = "juancito"
check_status()

usuario = "pancracio"
check_status()
