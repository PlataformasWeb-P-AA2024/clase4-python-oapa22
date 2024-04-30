nombre = input("Ingrese nombre de persona: ")

edad = int(input("Ingrese edad de persona: "))

sueldo = float(input("Ingrese sueldo de persona: "))

mensajeFinal = "Nombre:%s\nEdad:%d\nSueldo:%.2f\n" % (nombre, edad, sueldo)

print(mensajeFinal)