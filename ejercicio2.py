"""
calcule la suma de los 4 primeros números pares desde un número que introducimos por teclado. Es decir, si insertamos un 5, nos haga la suma de 6+8+10+12
"""

"""
lista = []
numero = input("Introduce un numero por favor: ")
numero = int (numero)

if numero % 2 != 0:
    numero+=1 # numero = numero + 1 es lo mismo
for n in range(numero, (numero + 6) + 1):
    if n % 2 == 0:
        lista.append(n)
print("La suma de ", lista, "es", sum(lista))
"""

"""
En forma de tupla
"""

tupla = (0,2,4,6)
numero = input("Introduce un numero por favor: ")
numero = int (numero)
suma_texto = ""
suma_nro = 0
if numero % 2 != 0:
    numero+=1
for constante in tupla:
    suma_texto += str(numero+constante) + '+'
    suma_nro += numero+constante
    print("Mi suma", suma_texto, "es:", suma_nro)
