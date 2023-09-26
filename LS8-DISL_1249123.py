# Laboratorio de programacion seccion 17
# 26/09/2023
# Ejercicio: Factorial
# Diego Ignacio Sanchez Lopez
# Objetivo: Realizar un programa que muestre un menu que el usuario pueda ingresar numeros de 1 a 3. 
# Entrada: Numero de uno a 3 y numeros ingresados por el usuario. 
#Proceso principales: tomar un numero e incrementar en uno a uno

# Función para calcular el factorial de un número
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Función para generar la secuencia de Fibonacci hasta la posición n
def generar_fibonacci(numero):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < numero:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence

while True:
    # Mostrar el menú
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    # Solicitar la opción al usuario
    opcion = input("Ingrese el número de opción que desea ejecutar: ")

    if opcion == "1":
        # Opción 1: Calcular el factorial
        numero = int(input("Ingrese un número para calcular el factorial: "))
        resultado = calcular_factorial(numero)
        print(f"{numero}! =", end=" ")
        for i in range(1, numero + 1):
            print(i, end=" * " if i < numero else "\n")
    elif opcion == "2":
        # Opción 2: Generar la secuencia de Fibonacci
        numero = int(input("Ingrese un número para generar la secuencia de Fibonacci: "))
        fibonacci_sequence = generar_fibonacci(numero)
        print(", ".join(map(str, fibonacci_sequence)))
    elif opcion == "3":
        # Opción 3: Salir del programa
        print("¡Hasta luego!")
        break
    else:
        # Opción inválida
        print("Opción no válida. Por favor, ingrese una opción válida.")

# Fin del programa
