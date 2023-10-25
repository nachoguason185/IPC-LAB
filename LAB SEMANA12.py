# Pensamiento computacional
# Sección 17
# Fecha: 25 de octubre 2023
# Autor: Ignacio Sánchez
# Objetivo: El programa debe solicitar al usuario la cantidad de contactos que va a ingresar.
# Entrada: Pida al usuario que ingrese el nombre y el número de teléfono de un contacto.

# Declare una variable de tipo lista
contactos = []

# Solicitar al usuario la cantidad de contactos a ingresar
n = int(input("Ingrese la cantidad de contactos que va a ingresar: "))

# Ciclo para agregar contactos a la lista
for i in range(n):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    contacto = [nombre, numero]
    contactos.append(contacto)

# Mostrar la lista de contactos completa
print("Lista de contactos completa:")
for contacto in contactos:
    print(contacto)

# Pedir al usuario que ingrese el nombre de un contacto existente y eliminarlo
nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
for contacto in contactos:
    if contacto[0] == nombre_eliminar:
        contactos.remove(contacto)

# Mostrar la lista de contactos actualizada
print("Lista de contactos actualizada:")
for contacto in contactos:
    print(contacto)

# Ordenar la lista de contactos alfabéticamente por el nombre
contactos.sort()

# Mostrar la lista ordenada
print("Lista de contactos ordenada alfabéticamente:")
for contacto in contactos:
    print(contacto)

# Pedir al usuario que ingrese un nuevo contacto en mayúsculas
nombre_mayusculas = input("Ingrese el nombre del nuevo contacto en mayúsculas: ")
numero = input("Ingrese el número de teléfono del nuevo contacto: ")
contacto_mayusculas = [nombre_mayusculas.upper(), numero]
contactos.append(contacto_mayusculas)

# Pedir al usuario que ingrese un nuevo contacto en una posición específica
posicion = int(input("Ingrese la posición donde debe guardar el nuevo contacto: "))
nombre_nuevo = input("Ingrese el nombre del nuevo contacto: ")
numero_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
contacto_nuevo = [nombre_nuevo, numero_nuevo]
contactos.insert(posicion, contacto_nuevo)

# Mostrar la lista de contactos completa
print("Lista de contactos completa:")
for contacto in contactos:
    print(contacto)

# Crear una copia de la lista de contactos original
contactos_copia = contactos.copy()

# Ordenar la copia alfabéticamente de forma descendente
contactos_copia.sort(key=lambda x: x[0], reverse=True)

# Mostrar la lista copiada y la lista original
print("Lista copiada ordenada alfabéticamente de forma descendente:")
for contacto in contactos_copia:
    print(contacto)

print("Lista de contactos original:")
for contacto in contactos:
    print(contacto)


