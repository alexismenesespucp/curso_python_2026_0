class Robot:
    def comando_moverse(self): print("Moviendo...")
    def comando_parar(self): print("Parando...")

bot = Robot()
orden_remota = "parar" # Esto vendría de un socket o API

# Construimos el nombre del método dinámicamente
nombre_metodo = f"comando_{orden_remota}"

# Buscamos si el objeto tiene ese atributo/método
if hasattr(bot, nombre_metodo):
    func = getattr(bot, nombre_metodo)
    func() # Ejecutamos la función encontrada
else:
    print("Comando no reconocido")