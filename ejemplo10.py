archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()
lineas = [l.split("|") for l in lineas]

# Versión con los 25363 archivos:

# contador = 1
# for x in lineas:
#         cadena = """<b>Torneo:</b> %s <br> <b>\nGanador:</b> %s""" % (x[0], x[9])
#         print(cadena)
#
#         archivo_generado = open("data/ArchivoN_%s" % contador, "w")
#         archivo_generado.writelines("%s\n" % (cadena))
#         archivo_generado.close()
#         contador += 1

# Versión con límite de 100 para que no me explote la computadora:

contador = 1
bol = False
for x in lineas:
    if not bol:
        cadena = """<b>Torneo:</b> %s <br> <b>\nGanador:</b> %s""" % (x[0], x[9])
        print(cadena)

        archivo_generado = open("data/ArchivoN_%s" % contador, "w")
        archivo_generado.writelines("%s\n" % (cadena))
        archivo_generado.close()
        contador += 1
        if contador > 100:
            bol = True
