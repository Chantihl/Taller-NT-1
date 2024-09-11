#Elabore un programa para la facultad de Ingeniería que pida 400 números e indique si ese número es par o impar; me muestre un listado y me indique cuantos son pares y cuantos son impares.


import random

# Generar 400 números aleatorios entre 1 y 1000
numeros = [random.randint(1, 1000) for _ in range(400)]

# Variables para contar pares e impares
pares = 0
impares = 0

# Crear un listado de resultados
resultado = []

# Determinar si cada número es par o impar
for numero in numeros:
    if numero % 2 == 0:
        resultado.append(f"{numero} es par")
        pares += 1
    else:
        resultado.append(f"{numero} es impar")
        impares += 1

# Imprimir el listado de resultados
print("Listado de numeros:")
for res in resultado:
    print(res)

# Imprimir la cantidad de pares e impares
print(f"\nCantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")


