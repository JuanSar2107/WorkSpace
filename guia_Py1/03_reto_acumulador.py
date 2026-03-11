print("🛒 Caja Registradora")

total = 0  

for i in range(1, 6):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    total = total + precio  

print(f"\nEl total de la compra es: ${total}")