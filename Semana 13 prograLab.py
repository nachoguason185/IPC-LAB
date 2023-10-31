# Pensamiento computacional
# Sección 17
# Fecha: 31 de octubre 2023
# Autor: Ignacio Sánchez
# Objetivo: Crear una clase con los atributos respectivos.
# Entrada: Insertar nombre, apellido, nacimiento, apellido de casada

class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_de_casada = ""
        self.fecha_de_nacimiento = ""

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_de_casada(self, apellido_de_casada):
        self.apellido_de_casada = apellido_de_casada

    def insertar_fecha_de_nacimiento(self, fecha_de_nacimiento):
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        return self.apellidos

    def obtener_fecha_de_nacimiento(self):
        return self.fecha_de_nacimiento

    def devolver_nombre_completo(self):
        nombre_completo = self.nombres + " " + self.apellidos
        if self.apellido_de_casada:
            nombre_completo += " " + self.apellido_de_casada
        return nombre_completo

    def devolver_edad(self):
        # Aquí debes calcular la edad a partir de la fecha de nacimiento
        # Asumiendo que la fecha de nacimiento es una cadena con formato "YYYY-MM-DD"
        if self.fecha_de_nacimiento:
            import datetime
            fecha_nacimiento = datetime.datetime.strptime(self.fecha_de_nacimiento, "%Y-%m-%d")
            fecha_actual = datetime.datetime.now()
            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            return edad
        else:
            return None

# Ejemplo de uso
persona = Persona()
persona.insertar_nombres("Aurelio")
persona.insertar_apellidos("Casillas")
persona.insertar_apellido_de_casada("Perdomo")
persona.insertar_fecha_de_nacimiento("1999-05-18")

print("Nombre completo:", persona.devolver_nombre_completo())
print("Edad:", persona.devolver_edad())


