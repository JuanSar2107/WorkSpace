class Empleado:

    def __init__(self, nombre: str, salario: float):
        self.nombre: str = nombre
        self.salario: float = salario


    def trabajar(self) -> None:
        print(self.nombre, "está cumpliendo su horario regular.")



class Desarrollador(Empleado):

    def programar(self) -> None:
        print(self.nombre, "está escribiendo código Python.")



class Gerente(Empleado):

    def trabajar(self) -> None:
        print(self.nombre, "está en una reunión estratégica.")



dev = Desarrollador("Carlos", 3500)
jefe = Gerente("Ana", 6000)

dev.trabajar()
dev.programar()

jefe.trabajar()