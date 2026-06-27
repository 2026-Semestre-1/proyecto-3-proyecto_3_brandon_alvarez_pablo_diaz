# ========================================== Librerias =============================================
from Clases.Persona import Persona

# ==================================================================================================


# ======================================= Clase Futbolista =========================================
# Nombre: Futbolista
# Entradas: Clase Persona, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual.
# Salidas: nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual.
# Restricciones:
# ==================================================================================================
class Futbolista(Persona):
    def __init__(
        self,
        nombre,
        apellido,
        fecha_nacimiento,
        nacionalidad,
        dorsal,
        posicion,
        total_tarjetas_amarillas,
        total_tarjetas_rojas,
        goles,
        asistencias,
        puntaje_individual,
    ):
        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)

        if not isinstance(dorsal, int):
            raise TypeError("El dorsal debe de ser un número entero.")

        if not isinstance(posicion, str):
            raise TypeError("La posicion debe de ser un string.")

        if not isinstance(total_tarjetas_amarillas, int):
            raise TypeError(
                "El total de las tarjetas amarillas deben de ser números enteros"
            )

        if not isinstance(total_tarjetas_rojas, int):
            raise TypeError(
                "El total de las tarjetas rojas deben de ser números enteros"
            )

        if not isinstance(goles, int):
            raise TypeError("Los goles deben de ser números enteros")

        if not isinstance(asistencias, int):
            raise TypeError("Las asistencias deben de ser números enteros")

        if not isinstance(puntaje_individual, int):
            raise TypeError("El puntaje individual debe de ser un número.")

        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual

    # ================================= Función mostrar datos ==========================================
    # Nombre: mostrar_datos
    # Entradas: ninguna
    # Salidas: Datos de la Clase Persona, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias y puntaje_individual.
    # Restricciones:
    # ==================================================================================================

    def mostrar_datos(self):
        return {
            **super().mostrar_datos(),
            "dorsal": self.dorsal,
            "posicion": self.posicion,
            "total_tarjetas_amarillas": self.total_tarjetas_amarillas,
            "total_tarjetas_rojas": self.total_tarjetas_rojas,
            "goles": self.goles,
            "asistencias": self.asistencias,
            "puntaje_individual": self.puntaje_individual,
        }

    # ================================= Función actualizar datos =======================================
    # Nombre: actualizar_datos
    # Entradas: nuevoNombre, nuevoApellido, nuevaFecha_nacimiento, nuevaNacionalidad, nuevoDorsal, nuevaPosicion, nuevototal_tarjetas_amarillas, nuevototal_tarjetas_rojas, nuevoGoles, nuevaAsistencias y nuevopuntaje_individual.
    # Salidas: Permite modificar los atributos del futbolista.
    # Restricciones:
    # ==================================================================================================

    def actualizar_datos(
        self,
        nuevoNombre,
        nuevoApellido,
        nuevaFecha_nacimiento,
        nuevaNacionalidad,
        nuevoDorsal,
        nuevaPosicion,
        nuevototal_tarjetas_amarillas,
        nuevototal_tarjetas_rojas,
        nuevoGoles,
        nuevaAsistencias,
        nuevopuntaje_individual,
    ):

        if not isinstance(nuevoDorsal, int):
            return "El dorsal debe de ser un número entero."

        if not isinstance(nuevaPosicion, str):
            return "La posicion debe de ser un string."

        if not isinstance(nuevototal_tarjetas_amarillas, int):
            return "El total de tarjetas amarillas deben de ser números enteros."

        if not isinstance(nuevototal_tarjetas_rojas, int):
            return "El total de tarjetas rojas deben de ser números enteros."

        if not isinstance(nuevoGoles, int):
            return "Los goles deben de ser números enteros."

        if not isinstance(nuevaAsistencias, int):
            return "Las asistencias deben de ser números enteros."

        if not isinstance(nuevopuntaje_individual, int):
            return "El puntaje_individual debe de ser un número entero."

        self.nombre = nuevoNombre
        self.apellido = nuevoApellido
        self.fecha_nacimiento = nuevaFecha_nacimiento
        self.nacionalidad = nuevaNacionalidad
        self.dorsal = nuevoDorsal
        self.posicion = nuevaPosicion
        self.total_tarjetas_amarillas = nuevototal_tarjetas_amarillas
        self.total_tarjetas_rojas = nuevototal_tarjetas_rojas
        self.goles = nuevoGoles
        self.asistencias = nuevaAsistencias
        self.puntaje_individual = nuevopuntaje_individual

        return True

    # ================================= Función registrar gol =========================================
    # Nombre: registrar_gol
    # Entradas: Ninguna
    # Salidas: True si el gol se registra correctamente.
    # Restricciones:
    # ==================================================================================================

    def registrar_gol(self):

        self.goles += 1
        return True

    # ================================= Función registrar asistencia =======================================
    # Nombre: registrar_asistencia
    # Entradas: Ninguna
    # Salidas: True si la asistencia se registra correctamente.
    # Restricciones:
    # ==================================================================================================

    def registrar_asistencia(self):

        self.asistencias += 1
        return True

    # ================================= Función registrar tarjeta =======================================
    # Nombre: registrar_tarjeta
    # Entradas: tipo (string)
    # Salidas: True si la tarjeta se registra correctamente.
    # Restricciones: El tipo debe de ser "amarilla" o "roja".
    # ==================================================================================================

    def registrar_tarjeta(self, tipo):

        if tipo == "amarilla":

            self.total_tarjetas_amarillas += 1
            return True

        elif tipo == "roja":

            self.total_tarjetas_rojas += 1
            return True

        else:
            return f"La tarjeta {tipo}, es incorrecta, solo se permite roja o amarilla."
