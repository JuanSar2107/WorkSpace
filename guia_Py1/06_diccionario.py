concesionario = []

for i in range(1, 4):
    print(f"\nRegistro del vehículo {i}")

    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    precio = float(input("Ingrese el precio: "))

    
    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }

    concesionario.append(vehiculo)


print("\n📋 Informe Final de Vehículos Registrados:\n")

for auto in concesionario:
    print(f"Vehículo registrado: Marca {auto['marca']}, "
          f"Modelo {auto['modelo']}, "
          f"Precio: ${auto['precio']}")