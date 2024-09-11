#Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable, registrando un puntaje que se clasifica de la siguiente forma si tiene 2 puntos está con un funcionamiento defectuoso, si tiene 3 puntos el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo.


import random

# Generar puntajes aleatorios entre 2 y 4 para 407 cabinas
puntajes = [random.randint(2, 4) for _ in range(407)]

# Contadores para cada categoría
cont_defectuoso = 0
cont_moderado = 0
cont_optimo = 0

# Crear un listado para almacenar los resultados de clasificacion
resultados = []

# Clasificar el funcionamiento de cada cabina y contar
for puntaje in puntajes:
    if puntaje == 2:
        estado = "Funcionamiento defectuoso"
        cont_defectuoso += 1
    elif puntaje == 3:
        estado = "Funcionamiento moderado"
        cont_moderado += 1
    elif puntaje == 4:
        estado = "Funcionamiento optimo"
        cont_optimo += 1
    else:
        estado = "Puntaje fuera de rango"  # Para cubrir cualquier puntaje no esperado

    resultados.append((puntaje, estado))

# Imprimir el listado de resultados
print("Resultados del funcionamiento de las cabinas:")
for puntaje, estado in resultados:
    print(f"Puntaje: {puntaje}, Estado: {estado}")

# Imprimir los totales por categoria
print(f"\nTotal de cabinas con funcionamiento defectuoso: {cont_defectuoso}")
print(f"Total de cabinas con funcionamiento moderado: {cont_moderado}")
print(f"Total de cabinas con funcionamiento óptimo: {cont_optimo}")
