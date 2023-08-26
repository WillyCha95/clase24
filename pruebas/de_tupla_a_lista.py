a_comprar = ("lacteos", "panificados", "frutas", "verduras", "carnes")
comprado = []

for articulo in a_comprar:
    if articulo == 'verduras' or articulo == 'panificados':
        break
    comprado.append(articulo)
    print("He conseguido:", comprado)