"""
Cargar una lista con N numeros y luego hallar el promedio de los
"""

numeros = []
cantidad = 0
suma = 0
promedio = 0

for nro in range(0, 9999):
    numero = input("Ingresa un numero: ")
    if numero == 'sali de aca':
        break
    numero = int(numero)
    if numero != 0:
        suma = suma + numero
        cantidad = cantidad + 1
    numeros.append(numero)
    promedio = suma / cantidad

    print("mi listado es: ", numeros)
    print("la suma de los no ceros es de", suma)
    print(" y su cantidad es de: ", cantidad)
    print("El promedio es de: ", promedio)

