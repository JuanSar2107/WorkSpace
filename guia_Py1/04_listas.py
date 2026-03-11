colores = ["Rojo", "Azul", "Verde"]

print("Lista actual:", colores)

color_eliminar = input("Escribe un color que no te guste: ")

if color_eliminar in colores:
    colores.remove(color_eliminar)
    print("Color eliminado.")
else:
    print("Ese color no está en la lista.")

print("Lista final:", colores)