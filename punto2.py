#Elabore un programa para el Éxito que determine el salario de los 1897 empleados de su compañía, teniendo en cuenta las comisiones y la seguridad social que debe pagar, e imprima el listado de la información. 


# DATOS RANDOM 
import random

# GENERAMOS DATOS PARA SALARIO, COMISION Y SGS
salarios = [random.randint(1000, 5000) for _ in range(1897)]  
comisiones = [random.randint(100, 1000) for _ in range(1897)]  
seguridad_social = [0.1 * salario for salario in salarios] 

# CALCULO SALARIAL DE CADA EMPLEADO
salarios_totales = []

for i in range(1897):
    salario_total = salarios[i] + comisiones[i] - seguridad_social[i]
    salarios_totales.append(salario_total)

# LISTADO DE LA INFORMACION DE LOS EMPLEADOS
print("Listado de salarios totales:")
for i in range(1897):
    print(f"Empleado {i + 1}: Salario Base = {salarios[i]}, Comisiones = {comisiones[i]}, Seguridad Social = {seguridad_social[i]:.2f}, Salario Total = {salarios_totales[i]:.2f}")








