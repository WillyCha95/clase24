#El parentesis no se puede modificar

a_comprar = ("lacteos", "panificados", "frutas", "verduras", "carnes")

#a_comprar.append("Embutidos")
#a_comprar.append("Bebidas")

for elemento in a_comprar:
    print("Debo comprar", elemento)
    if elemento == 'frutas':
        continue
    print("+Bueno, ya compre", elemento)
print("Hola, ya he vuelto del super!")

