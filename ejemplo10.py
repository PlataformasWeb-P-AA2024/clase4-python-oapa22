archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()
lineas = [l.split("|") for l in lineas]

for x in lineas:
    cadena = """<b>Torneo:</b> %s <br> <b>\nGanador:</b> %s""" % (x[0], x[9])
    print(cadena)

    archivo_generado = open("data/%s" % (x[9]), "w")
    archivo_generado.writelines("%s\n" % (cadena))
    archivo_generado.close()