dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

numero = int(input("Ingresa un número del 1 al 7: "))

if 1 <= numero <= 7:
    print("El día correspondiente es:", dias_semana[numero - 1])
else:
    print("Número fuera de rango.")
