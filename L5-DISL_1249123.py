# Diego Ignacio Sanchez Lopez - 1249123
# Introduccion a la programacion (Laboratorio)
# Ejercicio 1 (laboratorio semana 6)
# 12 de septiembre de 2023

# Objetivo: Dado un numero entero, como dato, determinar si el mismo es positivo, negativo o cero.
#Entrada: Numero entero

print("Ejercicio 1")
v1 = input("Ingrese un numero entero:")
vnum = int(v1)
if vnum > 0:
    print("RESULTADO: Su numero es positivo")

elif vnum < 0:
    print("RESULTADO: Su numero es negativo")
else:
    print("RESULTADO: Su numero es 0")