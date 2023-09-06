# Laboratorio de programacion seccion 17
# 5/09/2023
# Diego Ignacio Sanchez Lopez
# Objetivo: Crear un programa en python que calcule la raiz de un numero.
# Entrada: Numero 1, Numero 2
# Proceso: 
# Paso 1: Solicitar al usuario que ingrese los numeros
numero1 = float(input("Ingrese el primer numero:"))
numero2 = float(input("Ingrese el segundo numero:"))

# Paso 2: Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2 

# Aseguremonos de que el denominador no sea cero antes de realizar la division
if numero2 != 0: 
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

# Paso 3: Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division:{division}")
