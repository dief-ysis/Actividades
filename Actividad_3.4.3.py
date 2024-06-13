def validar_lista_numeros():
    while True:
        numeros = input("Ingrese una lista de números enteros separados por espacios: ")
        numeros = numeros.split()
        try:
            numeros = [int(num) for num in numeros]
            return numeros
        except ValueError:
            print("Error: Por favor, asegúrese de ingresar solo números enteros. Intente nuevamente.")

numeros = validar_lista_numeros()
print("Lista de números ingresada:", numeros)

numeros_pares = []
numeros_impares = []

for numero in numeros:
    mod = numero % 2
    if mod == 0:
        numeros_pares.append(numero)
    else: 
        numeros_impares.append(numero)

print("Numeros pares: ", numeros_pares)
print("Numeros impares: ", numeros_impares)
