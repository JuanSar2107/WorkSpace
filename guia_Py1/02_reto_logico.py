print("Bienvenido a la Montaña Rusa")

estatura = float(input("Ingresa tu estatura en cm: "))
edad = int(input("Ingresa tu edad: "))

if estatura > 150 and edad > 12:
    print("Acceso permitido. ¡Disfruta la montaña rusa!")
else:
    print("Acceso denegado. No cumples los requisitos.")