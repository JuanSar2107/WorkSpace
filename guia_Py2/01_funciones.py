def calcular_area_rectangulo(base: float, altura: float) -> float:
    area: float = base * altura
    return area

resultado: float = calcular_area_rectangulo(5.0, 3.0)
print("El área del rectángulo es:", resultado)

def es_mayor_de_edad(edad: int) -> bool:
    if edad >= 18:
        return True
    else:
        return False

edad_usuario: int = 20

if es_mayor_de_edad(edad_usuario):
    print("Es mayor de edad")
else:
    print("Es menor de edad")