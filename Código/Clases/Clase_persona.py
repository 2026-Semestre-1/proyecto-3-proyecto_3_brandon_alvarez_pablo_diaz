class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe de ser un string.")

        if not isinstance(apellido, str):
            raise TypeError("El apellido debe de ser un string.")

        if not isinstance(fecha_nacimiento, str):
            raise TypeError(
                "La fecha de nacimiento debe de ser un string de la forma DD/MM/AAAA."
            )

        if not isinstance(nacionalidad, str):
            raise TypeError("La nacionalidad debe de ser un string.")

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

    def mostrar_datos(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_nacimiento": self.fecha_nacimiento,
            "nacionalidad": self.nacionalidad,
        }
