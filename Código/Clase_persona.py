class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):

        if not isinstance(nombre, str):
            return "El nombre debe de ser un string."

        if not isinstance(apellido, str):
            return "El apellido debe de ser un string."

        if not isinstance(fecha_nacimiento, str):
            return (
                "La fecha de nacimiento debe de ser un string de la forma DD/MM/AAAA."
            )

        if not isinstance(nacionalidad, str):
            return "La nacionalidad debe de ser un string."

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
