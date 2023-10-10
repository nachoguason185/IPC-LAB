# Pensamiento computacional
# Sección 17
# Fecha: 10 de octubre 2023
# Autor: Ignacio Sánchez
# Objetivo: Crear un módulo con las funciones necesarias para convertir una cantidad expresada en centímetros.
# Entrada: Centrimetros a diferentes unidades de medida.
# Proceso principales: 
# Salida: Cantidad coonvertida

def cm_to_metros(cm):
    metros = cm / 100.0
    return metros

def cm_to_kilometros(cm):
    kilometros = cm / 100000.0
    return kilometros

def cm_to_pulgadas(cm):
    pulgadas = cm / 2.54
    return pulgadas

def cm_to_pies(cm):
    pies = cm / 30.48
    return pies

def main():
    cm = float(input("Ingresa la cantidad en centímetros: "))

    metros = cm_to_metros(cm)
    print(f"{cm} centímetros son {metros} metros.")

    kilometros = cm_to_kilometros(cm)
    print(f"{cm} centímetros son {kilometros} kilómetros.")

    pulgadas = cm_to_pulgadas(cm)
    print(f"{cm} centímetros son {pulgadas} pulgadas.")

    pies = cm_to_pies(cm)
    print(f"{cm} centímetros son {pies} pies.")

if __name__ == "__main__":
    main()









