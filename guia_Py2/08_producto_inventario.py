class Producto:

    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:

        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            self.stock -= cantidad
            total = cantidad * self.precio

            print("Venta realizada")
            print("Producto:", self.nombre)
            print("Total:", total)
            print("Stock restante:", self.stock)

        except ValueError as e:
            print("Error:", e)


class ProductoPerecedero(Producto):

    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = dias_vencimiento


producto1 = Producto("Teclado", 50000, 10)

producto1.vender(3)
producto1.vender(20)


producto2 = ProductoPerecedero("Leche", 4000, 5, 7)

producto2.vender(2)
producto2.vender(10)