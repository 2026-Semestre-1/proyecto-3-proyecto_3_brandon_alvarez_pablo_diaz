# ====================================== Librerias =================================================
import random
from Clases.Partido import Partido

# ==================================================================================================


# ======================================= Clase Fase ===============================================
# Nombre: Fase
# Entradas: nombre_fase.
# Salidas: nombre_fase, partidos, penales y fecha_temporal.
# Restricciones:
# ==================================================================================================
class Fase:

    def __init__(self, nombre_fase):

        if not isinstance(nombre_fase, str):
            print("Error: el nombre de la fase no es válida")
            return

        self.nombre_fase = nombre_fase
        self.partidos = []
        self.penales = []
        self.fecha_temporal = "01/01/2026"

    # ================================= Función registrar juego ========================================
    # Nombre: registrar_juego
    # Entradas: equipo1 y equipo2.
    # Salidas: Crea un nuevo Partido entre los dos equipos y lo agrega a la fase.
    # Restricciones:
    # ==================================================================================================

    def registrar_juego(self, equipo1, equipo2):

        fecha_asignada = self.fecha_temporal

        nuevo_partido = Partido(equipo1, equipo2, self.nombre_fase, "", fecha_asignada)

        self.partidos += [nuevo_partido]

    # ================================= Función jugar fase =============================================
    # Nombre: jugar_fase
    # Entradas: ninguna
    # Salidas: Simula todos los partidos de la fase. En caso de empate, simula penales.
    # Restricciones:
    # ==================================================================================================

    def jugar_fase(self):
        self.penales = []  # por si se recorre dos veces, entonces se reinicia

        for partido in self.partidos:
            partido.simular()

            if partido.goles_equipo1 == partido.goles_equipo2:

                penales_equipo1 = 0
                penales_equipo2 = 0

                while penales_equipo1 == penales_equipo2:
                    penales_equipo1 = random.randint(2, 5)
                    penales_equipo2 = random.randint(2, 5)

            self.penales += [[partido, penales_equipo1, penales_equipo2]]

    # ================================= Función mostrar juegos =========================================
    # Nombre: mostrar_juegos
    # Entradas: ninguna
    # Salidas: Muestra los resultados de todos los partidos de la fase.
    # Restricciones:
    # ==================================================================================================

    def mostrar_juegos(self):  # sujeto a cambios
        lista_textos = []

        for partido in self.partidos:

            texto_partido = partido.mostrar_resultado()

            for registro in self.penales:
                if registro[0] == partido:  # es para buscar el partido exacto

                    penales_equipo1 = registro[1]
                    penales_equipo2 = registro[2]

                    texto_partido += f" (Penales: {penales_equipo1} - {penales_equipo2})"

            lista_textos += [texto_partido]

        return lista_textos

    # ================================= Función obtener clasificados =========================================
    # Nombre: obtener_clasificados
    # Entradas: ninguna
    # Salidas: Retorna la lista de equipos ganadores que avanzan a la siguiente fase.
    # Restricciones:
    # ==================================================================================================

    def obtener_clasificados(self):
        lista_ganadores = []

        for partido in self.partidos:
            ganador = partido.generar_ganador()

            if ganador is None:  # si es None, entonces es un empate

                for registro in self.penales:
                    if registro[0] == partido:  # se busca el partido exacto

                        penales_equipo1 = registro[1]
                        penales_equipo2 = registro[2]

                        if (
                            penales_equipo1 > penales_equipo2
                        ):  # se define el ganador de los empates
                            lista_ganadores += [partido.equipo_1]
                        else:
                            lista_ganadores += [partido.equipo_2]

            else:  # sino hay empate, entonces avanza el ganador directamente
                lista_ganadores += [ganador]

        return lista_ganadores
