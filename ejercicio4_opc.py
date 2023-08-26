"""
cargar una lista con N numeros
"""

N = int(input("Introduce el valor para la cantidad de numeros: "))
lista = []
suma_no_0 = []
promedio = 0

for x in range(0, N):
    nro = int(input("ingresa un numero: "))
    lista.append(nro)
    if nro != 0:
        suma_no_0.append(nro)

promedio = sum(suma_no_0) / len(suma_no_0)

print("mi listado es: ", lista)
print("la suma de los no ceros es de", suma_no_0)
print(" y su cantidad es de: ", suma_no_0)
print("El promedio es de: ", promedio)