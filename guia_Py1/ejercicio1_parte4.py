mis_amigos = []

for i in range(1, 4):
    nombre = input(f"Ingrese el nombre del amigo {i}: ")
    mis_amigos.append(nombre)

print("\nSaludos:")
for amigo in mis_amigos:
    print(f"Hola {amigo}, ¡qué gusto verte!")