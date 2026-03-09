def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    
    descuento_salud_pension: float = salario_base * 0.08
    salario_final: float = salario_base - descuento_salud_pension + bonificacion
    
    return salario_final


salario1: float = calcular_salario_neto(2000000)
salario2: float = calcular_salario_neto(2000000, 300000)

print("Salario sin bonificación:", salario1)
print("Salario con bonificación:", salario2)