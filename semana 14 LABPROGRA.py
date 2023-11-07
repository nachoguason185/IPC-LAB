# Pensamiento computacional
# Sección 17
# Fecha: 7 de novimebre 2023
# Autor: Ignacio Sánchez
# Objetivo: Crear una clase con los atributos respectivos.
# Entrada: Insertar marca de carro, descuento y disponivilidad 


class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = True
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precio_en_dolares = self.precio / self.tipoCambioDolar
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio de venta: Q{self.precio}, Precio en dólares: ${precio_en_dolares}, {self.MostrarDisponibilidad()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.precio = self.precio - self.descuentoAplicado
        self.DefinirPrecio(self.precio)

auto = Automovil()
auto.DefinirMarca("JAC T8 pro")
auto.DefinirModelo(2023)
auto.DefinirPrecio(270000.0)
auto.DefinirTipoCambio(7.75)

print(auto.MostrarInformacion())  
auto.AplicarDescuento(10000.0) 
print(auto.MostrarInformacion()) 
auto.CambiarDisponibilidad()  
print(auto.MostrarInformacion())  
