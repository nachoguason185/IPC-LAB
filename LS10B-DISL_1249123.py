# Pensamiento computacional
# Sección 17
# Fecha: 10 de octubre 2023
# Autor: Ignacio Sánchez
# Objetivo: Crear el módulo principal para solicitar al usuario la cantidad de centímetros, y permitirle seleccionar la unidad de medida a la que desea convertir.
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
    while True:
        try:
            cm = float(input("Ingresa la cantidad en centímetros: "))
            unidad = input("Selecciona la unidad de medida (metros, kilometros, pulgadas, pies): ").lower()

            if unidad == "metros":
                resultado = cm_to_metros(cm)
                print(f"{cm} centímetros son {resultado} metros.")
            elif unidad == "kilometros":
                resultado = cm_to_kilometros(cm)
                print(f"{cm} centímetros son {resultado} kilómetros.")
            elif unidad == "pulgadas":
                resultado = cm_to_pulgadas(cm)
                print(f"{cm} centímetros son {resultado} pulgadas.")
            elif unidad == "pies":
                resultado = cm_to_pies(cm)
                print(f"{cm} centímetros son {resultado} pies.")
            else:
                print("Unidad de medida no válida. Por favor, selecciona entre metros, kilometros, pulgadas o pies.")

            continuar = input("¿Deseas realizar otra conversión? (s/n): ").lower()
            if continuar != 's':
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
