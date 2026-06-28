# =========================================== Librerias ============================================
from Clases.Pais import Pais
from Clases.Entrenador import Entrenador
from Utilidades import largoLista

# ==================================================================================================


# ========================================= Clase Seleccion ==========================================
# Nombre: Seleccion
# Entradas: codigo_equipo, pais.
# Salidas: codigo_equipo, pais, entrenador, jugadores, total_goles_favor, total_goles_contra, total_tarjetas_amarillas, total_tarjetas_rojas, fuerza_equipo.
# Restricciones:
# ==================================================================================================
class Seleccion:
    def __init__(self, codigo_equipo, pais):

        if not isinstance(pais, Pais):
            raise TypeError("El atributo pais debe ser un objeto de la clase Pais.")

        self.codigo_equipo = codigo_equipo
        self.pais = pais
        self.entrenador = None
        self.jugadores = []
        self.total_goles_favor = 0
        self.total_goles_contra = 0
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.fuerza_equipo = 0
        self.fase_alcanzada = "Fase de Grupos"

    # =================================== Funcion mostrar datos ==================================
    # Nombre: mostrar_datos
    # Entradas: ninguna.
    # Salidas: Muestra la información de la selección, incluyendo país, entrenador y plantilla de jugadores.
    # Restricciones:
    # ==============================================================================================
    def mostrar_datos(self):

        datos_jugadores = []

        for jugador in self.jugadores:
            datos_jugadores += [jugador.mostrar_datos()]

        datos_entrenador = None

        if self.entrenador != None:
            datos_entrenador = self.entrenador.mostrar_datos()

        return {
            "codigo_equipo": self.codigo_equipo,
            "pais": self.pais.mostrar_datos(),
            "entrenador": datos_entrenador,
            "jugadores": datos_jugadores,
            "total_goles_favor": self.total_goles_favor,
            "total_goles_contra": self.total_goles_contra,
            "total_tarjetas_amarillas": self.total_tarjetas_amarillas,
            "total_tarjetas_rojas": self.total_tarjetas_rojas,
            "fuerza_equipo": self.fuerza_equipo,
            "fase_alcanzada": self.fase_alcanzada,
        }

    # =================================== Funcion agregar jugador ==================================
    # Nombre: agregar_jugador
    # Entradas: futbolista.
    # Salidas: True si el jugador fue agregado con éxito.
    # Restricciones:
    # ==============================================================================================
    def agregar_jugador(self, futbolista):

        cantidad_actual = 0

        for _ in self.jugadores:
            cantidad_actual += 1

        if cantidad_actual < 23:
            self.jugadores += [futbolista]
            return True

        return False

    # =================================== Funcion eliminar jugador =================================
    # Nombre: eliminar_jugador
    # Entradas: dorsal.
    # Salidas: True si el jugador fue eliminado con éxito.
    # Restricciones:
    # ==============================================================================================
    def eliminar_jugador(self, dorsal):

        nueva_lista = []
        eliminado = False

        for jugador in self.jugadores:

            if jugador.dorsal == dorsal and not eliminado:
                eliminado = True

            else:
                nueva_lista += [jugador]

        self.jugadores = nueva_lista

        return eliminado

    # =================================== Funcion asignar entrenador ===============================
    # Nombre: asignar_entrenador
    # Entradas: entrenador.
    # Salidas: True si el entrenador fue asignado con éxito.
    # Restricciones:
    # ==============================================================================================
    def asignar_entrenador(self, entrenador):

        if isinstance(entrenador, Entrenador):
            self.entrenador = entrenador
            return True

        return False

    # =================================== Funcion registrar resultado ==============================
    # Nombre: registrar_resultado
    # Entradas: goles_favor, goles_contra, tarjetas_am, tarjetas_roj.
    # Salidas: True si el resultado fue registrado con éxito.
    # Restricciones:
    # ==============================================================================================
    def registrar_resultado(self, goles_favor, goles_contra, tarjetas_am, tarjetas_roj):

        self.total_goles_favor += goles_favor
        self.total_goles_contra += goles_contra
        self.total_tarjetas_amarillas += tarjetas_am
        self.total_tarjetas_rojas += tarjetas_roj
        return True

    # =================================== Funcion ordenamiento jugadores ===========================
    # Nombre: ordenamiento_jugadores
    # Entradas: ninguna.
    # Salidas: Lista de jugadores ordenada por puntaje individual.
    # Restricciones:
    # ==============================================================================================
    def ordenamiento_jugadores(self):

        hubo_cambio = True

        largo = largoLista(self.jugadores)

        while hubo_cambio:

            temp = []

            hubo_cambio = False

            for i in range(largo):

                if temp != []:

                    if temp.puntaje_individual < self.jugadores[i].puntaje_individual:

                        self.jugadores[i - 1] = self.jugadores[i]
                        self.jugadores[i] = temp

                        hubo_cambio = True

                temp = self.jugadores[i]

        if largo > 11:

            lista_ordenada = []
            indice = 0

            while indice <= 10:

                lista_ordenada += [self.jugadores[indice]]

                indice += 1

            return lista_ordenada

        return self.jugadores

    # =================================== Funcion calcular fuerza equipo ===========================
    # Nombre: calcular_fuerza_equipo
    # Entradas: ninguna.
    # Salidas: Fuerza del equipo.
    # Restricciones:
    # ==============================================================================================
    def calcular_fuerza_equipo(self):

        jugadores_ordenados = self.ordenamiento_jugadores()

        if largoLista(jugadores_ordenados) < 11:
            return False

        promedio = 0

        factor_entrenador = 0

        for i in range(11):

            promedio += jugadores_ordenados[i].puntaje_individual

        promedio = promedio / 11

        if self.entrenador != None:

            factor_entrenador = self.entrenador.experiencia_anios * 4

            if factor_entrenador > 100:

                factor_entrenador = 100

        ranking_fifa = 100 - self.pais.ranking_fifa

        self.fuerza_equipo = (
            (promedio * 0.6) + (factor_entrenador * 0.25) + (ranking_fifa * 0.15)
        )

        return self.fuerza_equipo
