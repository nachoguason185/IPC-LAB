# Diego Ignacio Sanchez Lopez - 1249123
# Introduccion a la programacion (Laboratorio)
# Ejercicio 2 (laboratorio semana 7)
# 19 de septiembre de 2023

# Objetivo: Utilizando el ejercicio anterior pondremos en accion la formula cuadratica.
#Entrada: Dos números enteros.
#Procesos principales
#Salida: Resultado de las operaciones básicas aritméticas.


import math

def calcular_formula_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "Error: discriminante negativo"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Soluciones: x1 = {x1}, x2 = {x2}"

while True:
    print("Ejercicio 3: Jerarquía de operaciones")
    
    a = float(input("Ingrese el valor de 'a': "))
    b = float(input("Ingrese el valor de 'b': "))
    c = float(input("Ingrese el valor de 'c': "))

    print("Seleccione una operación:")
    print("1. axb+c")
    print("2. a * (b + c)")
    print("3. a/b*c")
    print("4. 3a+2b/c^2")
    print("5. Fórmula Cuadrática")
    print("6. Salir")

    opcion = int(input("Ingrese el número de la operación deseada: "))

    if opcion == 1:
        resultado = a * b + c
    elif opcion == 2:
        resultado = a * (b + c)
    elif opcion == 3:
        if b != 0:
            resultado = (a / b) * c
        else:
            resultado = "Error: división por cero"
    elif opcion == 4:
        if c != 0:
            resultado = (3 * a + 2 * b) / (c ** 2)
        else:
            resultado = "Error: división por cero"
    elif opcion == 5:
        resultado = calcular_formula_cuadratica(a, b, c)
    elif opcion == 6:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una operación válida.")
        continue

    print(f"Resultado: {resultado}\n")