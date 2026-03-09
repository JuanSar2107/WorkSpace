class MascotaVirtual:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.energia = 10

    def jugar(self) -> None:
        self.energia -= 3
        print(self.nombre, "jugó. Energía actual:", self.energia)

    def dormir(self) -> None:
        self.energia += 5
        print(self.nombre, "durmió. Energía actual:", self.energia)


mascota = MascotaVirtual("Firulais")

mascota.jugar()
mascota.jugar()
mascota.dormir()