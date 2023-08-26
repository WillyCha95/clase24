"""
Cargar una lista de N componentes.
"""

lista = []
lista_impar = []
for x in range(0,9999999):
    componente = input("Introduce un numero: ")
    if componente == 'para loco':
        break
    componente = int(componente)
    lista.append(componente)
    if componente % 2 != 0:
        lista_impar.append(componente)
print(lista, "la suma de los valores impares es de", sum(lista_impar))