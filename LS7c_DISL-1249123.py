# Diego Ignacio Sanchez Lopez - 1249123
# Introduccion a la programacion (Laboratorio)
# Ejercicio 2 (laboratorio semana 7)
# 19 de septiembre de 2023

# Objetivo: Programja con jerarquia de operaciones
#Entrada: Dos números enteros.
#Procesos principales
#Salida: Resultado de las operaciones básicas aritméticas.


print("Ejercicio 3: Jerarquía de operaciones")

# Permitir al usuario ingresar tres números
a = float(input("Ingrese el valor de 'a': "))
b = float(input("Ingrese el valor de 'b': "))
c = float(input("Ingrese el valor de 'c': "))

# Calcular y mostrar los resultados de las expresiones
resultado1 = a * b + c
resultado2 = a * (b + c)
resultado3 = (a / b) * c
resultado4 = (3 * a + 2 * b) / (c ** 2)

print(f"Resultado de axb+c: {resultado1}")
print(f"Resultado de a * (b + c): {resultado2}")
print(f"Resultado de a/b*c: {resultado3}")
print(f"Resultado de 3a+2b/c^2: {resultado4}")