from Clase_persona import Persona


class futbolista:
    def __init__(
        self,
        nombre,
        apellido,
        fecha_nacimiento,
        nacionalidad,
        dorsal,
        posicion,
        puntuaje_indivual,
    ):

        if not isinstance(dorsal, int):
            return "El dorsal debe de ser un número entero."

        if not isinstance(posicion, str):
            return "La posicion debe de ser un string."

        if not isinstance(puntuaje_indivual, int):
            return "El puntuaje_indivual debe de ser un número entero."

        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)

        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjeta_amarilla = 0
        self.total_tarjeta_roja = 0
        self.goles = 0
        self.asistencias = 0
        self.puntuaje_indivual = puntuaje_indivual

    def mostrar_datos(self):
        return {
            **super().mostrar_datos(),
            "dorsal": self.dorsal,
            "posicion": self.posicion,
            "total_tarjeta_amarilla": self.total_tarjeta_amarilla,
            "total_tarjeta_roja": self.total_tarjeta_roja,
            "goles": self.goles,
            "asistencias": self.asistencias,
            "puntuaje_indivual": self.puntuaje_indivual,
        }

    def actualizar_datos(
        self,
        nuevoNombre,
        nuevoApellido,
        nuevaFecha_nacimiento,
        nuevaNacionalidad,
        nuevoDorsal,
        nuevaPosicion,
        nuevoTotal_tarjeta_amarilla,
        nuevoTotal_tarjeta_roja,
        nuevoGoles,
        nuevaAsistencias,
        nuevoPuntuaje_indivual,
    ):

        if not isinstance(nuevoDorsal, int):
            return "El dorsal debe de ser un número entero."

        if not isinstance(nuevaPosicion, str):
            return "La posicion debe de ser un string."

        if not isinstance(nuevoTotal_tarjeta_amarilla, int):
            return "El total de tarjetas amarillas deben de ser números enteros."

        if not isinstance(nuevoTotal_tarjeta_roja, int):
            return "El total de tarjetas rojas deben de ser números enteros."

        if not isinstance(nuevoGoles, int):
            return "Los goles deben de ser números enteros."

        if not isinstance(nuevaAsistencias, int):
            return "Las asistencias deben de ser números enteros."

        if not isinstance(nuevoPuntuaje_indivual, int):
            return "El puntuaje_indivual debe de ser un número entero."

        self.nombre = nuevoNombre
        self.apellido = nuevoApellido
        self.fecha_nacimiento = nuevaFecha_nacimiento
        self.nacionalidad = nuevaNacionalidad
        self.dorsal = nuevoDorsal
        self.posicion = nuevaPosicion
        self.total_tarjeta_amarilla = nuevoTotal_tarjeta_amarilla
        self.total_tarjeta_roja = nuevoTotal_tarjeta_roja
        self.goles = nuevoGoles
        self.asistencias = nuevaAsistencias
        self.puntuaje_indivual = nuevoPuntuaje_indivual

        return True

    def registrar_gol(self):

        self.goles += 1
        return True

    def registrar_asistencia(self):

        self.asistencias += 1
        return True

    def registrar_tarjeta(self, tipo):

        if tipo == "amarilla":

            self.total_tarjeta_amarilla += 1
            return True

        else:

            self.total_tarjeta_roja += 1
            return True
