#Con las listas, se puede modificar durante la ejecucion del programa

a_comprar = ["lacteos", "panificados", "frutas", "verduras", "carnes"]

a_comprar.append("Embutidos")
a_comprar.append("Bebidas")

for elemento in a_comprar:
    print("Debo comprar", elemento)
    if elemento == 'frutas':
        break
    print("+Bueno, ya compre", elemento)
print("Hola, ya he vuelto del super!")
