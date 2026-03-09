class SistemaSeguridad:

    def __init__(self, pin_acceso: int):
        self.usuario: str = "Admin"
        self.__pin_secreto: int = pin_acceso
        self._alarma_activada: bool = True


    def desactivar_alarma(self, intento_pin: int) -> None:

        if intento_pin == self.__pin_secreto:
            self._alarma_activada = False
            print("Alarma desactivada.")
        else:
            print("INTRUSO DETECTADO. Llamando a la policía.")


casa_central = SistemaSeguridad(1234)

casa_central.desactivar_alarma(9999)
casa_central.desactivar_alarma(1234)