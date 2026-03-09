class CajeroAutomatico:

    def __init__(self):
        self.efectivo_disponible: float = 10000


    def solicitar_retiro(self) -> None:

        print("Bienvenido al Cajero")

        try:

            monto_str: str = input("Ingrese la cantidad a retirar: ")
            monto: float = float(monto_str)

            if monto == 0:
                raise ValueError("No puede retirar cero pesos")

            if monto > self.efectivo_disponible:
                raise ValueError("Fondos insuficientes")

            self.efectivo_disponible -= monto

            print("Retiro exitoso")
            print("Dinero restante en cajero:", self.efectivo_disponible)


        except ValueError as e:
            print("ERROR:", e)


        except Exception as e:
            print("ERROR CRÍTICO:", e)


        finally:
            print("Expulsando tarjeta...")
            print("Gracias por usar el cajero\n")



mi_cajero = CajeroAutomatico()

mi_cajero.solicitar_retiro()