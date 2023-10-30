# Diccionarios para almacenar datos de clientes de diferentes tipos
administrativo = {}
catedratico = {}
estudiante = {}

def ingresar_datos_cliente():
    # Solicitar al usuario el tipo de cliente
    tipo_cliente = input("Ingrese el tipo de cliente (administrativo, catedrático o estudiante): ").lower()

    # Solicitar datos del cliente
    numero_carnet = input("Ingrese el número de carnet: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    # Crear un diccionario con los datos del cliente
    cliente = {
        "Numero de carnet": numero_carnet,
        "Nombre": nombre,
        "Apellido": apellido
    }

    # Almacenar el cliente en el diccionario correspondiente según el tipo
    if tipo_cliente == "administrativo":
        administrativo[numero_carnet] = cliente
    elif tipo_cliente == "catedrático":
        catedratico[numero_carnet] = cliente
    elif tipo_cliente == "estudiante":
        estudiante[numero_carnet] = cliente
    else:
        print("Tipo de cliente no válido. Los tipos válidos son: administrativo, catedrático o estudiante.")

def consultar_datos_cliente():
    numero_carnet = input("Ingrese el número de carnet a consultar: ")

    # Verificar en qué diccionario se encuentra el cliente y mostrar los datos
    if numero_carnet in administrativo:
        print("Datos del cliente administrativo:")
        print(administrativo[numero_carnet])
    elif numero_carnet in catedratico:
        print("Datos del cliente catedrático:")
        print(catedratico[numero_carnet])
    elif numero_carnet in estudiante:
        print("Datos del cliente estudiante:")
        print(estudiante[numero_carnet])
    else:
        print("Cliente no encontrado.")

# Bucle principal del programa
while True:
    opcion = input("1. Ingresar datos de un cliente\n2. Consultar datos de un cliente\n3. Salir\nSeleccione una opción: ")

    if opcion == "1":
        ingresar_datos_cliente()
    elif opcion == "2":
        consultar_datos_cliente()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
