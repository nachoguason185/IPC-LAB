# Diego Ignacio Sanchez Lopez - 1249123
# Introduccion a la programacion (Laboratorio)
# Ejercicio 1 (laboratorio semana 6)
# 12 de septiembre de 2023

# Objetivo: Realizar un programa que indique el dia de la semana correspondiente al numero ingresado

#Entrada: Numero del 1 al 7

print("Ejercicio 2")
Numero = int(input("Ingresar un umero dl 1 al 7:"))

#Evaluar si el dato entra en el rango definido.
if Numero <= 0 or Numero > 7:
    print("Error. El numero a ingresar debe estar contenido entre 1 y 7")
elif Numero == 1:
    print("Lunes")
elif Numero == 2:
    print("Martes")
elif Numero == 3:
    print("Miercoles")
elif Numero == 4:
    print("Jueves")
elif Numero == 5:
    print("Viernes")
elif Numero == 6:
    print("Sabado")
elif Numero == 7:
    print("Domingo")
