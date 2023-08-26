"""range (desde 10 al 36 de 7 en 7)"""

"""
for x in range(10,36,7):
    print(x)
"""

#Esto es diccionario en Python, clave por ejemplo nombre apellido etc. debe poner entre comilla para que funcione

import os

colorFavorito = "negro"

persona = {
    "nombre":"Marcos",
    "apellido":"Benitez",
    "edad": 25,
    "color_favorito": colorFavorito
}

print("persona", persona)

for clave in persona:
    print("en posicion", clave,"vale:", persona[clave])

directorio = 'C:\\Escritorio\\Clases DW\\clase.24\\pruebas\\'

with os.scandir(directorio) as archivos:
    for archivo in archivos:
        print("El archivo es", archivo.name)
        print(archivo.name.split("."))

