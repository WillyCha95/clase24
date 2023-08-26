"""
Cargar una lista de N numeros, sumar sus componentes e
imprimir la suma y el promedio de los numeros
"""

# intentar hacer 
def main():
    try:
        n = int(input("Ingrese la cantidad de números: "))
        numeros = []

        for i in range(n):
            numero = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)

        suma = sum(numeros)
        promedio = suma / n

        print(f"Suma de los números: {suma}")
        print(f"Promedio de los números: {promedio:.2f}")
        
    except ValueError:
        print("Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()
