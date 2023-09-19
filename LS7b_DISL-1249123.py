# Diego Ignacio Sanchez Lopez - 1249123
# Introduccion a la programacion (Laboratorio)
# Ejercicio 2 (laboratorio semana 7)
# 19 de septiembre de 2023

# Objetivo: Agregar un menu con el ejercicio anterior y el usuario eleja una operacion aritmetrica
#Entrada: Dos números enteros.
#Procesos principales
#Salida: Resultado de las operaciones básicas aritméticas.


while True:
    print("Ejercicio 1: Operaciones aritméticas")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Exponenciación")
    print("7. Cociente")
    print("8. Salir")

    opcion = int(input("Ingrese el número de la operación deseada: "))

    if opcion == 1:
        resultado = num1 + num2
        operacion = "suma"
    elif opcion == 2:
        resultado = num1 - num2
        operacion = "resta"
    elif opcion == 3:
        resultado = num1 * num2
        operacion = "multiplicación"
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            operacion = "división"
        else:
            print("No se puede dividir entre cero.")
            continue
    elif opcion == 5:
        resultado = num1 % num2
        operacion = "módulo"
    elif opcion == 6:
        resultado = num1 ** num2
        operacion = "exponenciación"
    elif opcion == 7:
        resultado = num1 // num2
        operacion = "cociente"
    elif opcion == 8:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una operación válida.")
        continue

    print(f"{num1} {operacion} {num2} = {resultado}\n")