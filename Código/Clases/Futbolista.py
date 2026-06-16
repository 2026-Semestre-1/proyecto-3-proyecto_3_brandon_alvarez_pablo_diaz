class futbolista:
    def __init__(self, dorsal, posicion, puntuaje_indivual):

        if not isinstance(dorsal, int):
            return "El dorsal debe de ser un número entero."

        if not isinstance(posicion, str):
            return "La posicion debe de ser un string."

        if not isinstance(puntuaje_indivual, int):
            return "El puntuaje_indivual debe de ser un número entero."

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
        n_dorsal,
        n_posicion,
        n_total_tarjeta_amarilla,
        n_total_tarjeta_roja,
        n_goles,
        n_asistencias,
        n_puntuaje_indivual,
    ):

        if not isinstance(n_dorsal, int):
            return "El dorsal debe de ser un número entero."

        if not isinstance(n_posicion, str):
            return "La posicion debe de ser un string."

        if not isinstance(n_total_tarjeta_amarilla, int):
            return "El total de tarjetas amarillas deben de ser números enteros."

        if not isinstance(n_total_tarjeta_roja, int):
            return "El total de tarjetas rojas deben de ser números enteros."

        if not isinstance(n_goles, int):
            return "Los goles deben de ser números enteros."

        if not isinstance(n_asistencias, int):
            return "Las asistencias deben de ser números enteros."

        if not isinstance(n_puntuaje_indivual, int):
            return "El puntuaje_indivual debe de ser un número entero."

        self.dorsal = n_dorsal
        self.posicion = n_posicion
        self.total_tarjeta_amarilla = n_total_tarjeta_amarilla
        self.total_tarjeta_roja = n_total_tarjeta_roja
        self.goles = n_goles
        self.asistencias = n_asistencias
        self.puntuaje_indivual = n_puntuaje_indivual

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
