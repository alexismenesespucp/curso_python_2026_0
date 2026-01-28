# 1. Intercambio Atómico (Swap)
# Python evalúa el lado derecho primero (crea una tupla en memoria) 
# y luego desempaqueta en el lado izquierdo.
a, b = 10, 20
a, b = b, a 

# 2. Desestructuración de flujos (Head, Mid, Tail)
records = [1, "Admin", "Login", "Success", "192.168.1.1", 0.05]

id_user, role, *logs, ip, latency = records

print(f"User {id_user} ({role})")
print(f"Eventos intermedios: {logs}") # ['Login', 'Success']
print(f"Conexión desde {ip} con {latency}s de lag")

# 3. Ignorar valores (Convención del guion bajo)
# Si solo queremos el primero y el último de una lista de 1000:
first, *_, last = range(1000)