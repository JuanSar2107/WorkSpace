class Vehiculo:

    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio


vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Ford", "Mustang", 2022)

print("Vehículo 1:", vehiculo1.marca, vehiculo1.modelo, vehiculo1.anio)
print("Vehículo 2:", vehiculo2.marca, vehiculo2.modelo, vehiculo2.anio)