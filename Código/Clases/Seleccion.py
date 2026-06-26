from Clases.Pais import Pais
from Clases.Entrenador import Entrenador


# ==============================
# Nombre: largo_jugadores
# Entradas: lista_jugadores
# Salidas: Cantidad de jugadores en la seleccion
# Restricciones:
# ==============================
def largo_jugadores(lista_jugadores):

    largo = 0

    for i in lista_jugadores:

        largo += 1

    return largo


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
        }

    def agregar_jugador(self, futbolista):

        cantidad_actual = 0

        for _ in self.jugadores:
            cantidad_actual += 1

        if cantidad_actual < 23:
            self.jugadores += [futbolista]
            return True

        return False

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

    def asignar_entrenador(self, entrenador):

        if isinstance(entrenador, Entrenador):
            self.entrenador = entrenador
            return True

        return False

    def registrar_resultado(self, goles_favor, goles_contra, tarjetas_am, tarjetas_roj):

        self.total_goles_favor += goles_favor
        self.total_goles_contra += goles_contra
        self.total_tarjetas_amarillas += tarjetas_am
        self.total_tarjetas_rojas += tarjetas_roj
        return True

    def ordenamiento_jugadores(self):

        hubo_cambio = True

        largo = largo_jugadores(self.jugadores)

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

    def calcular_fuerza_equipo(self):

        jugadores_ordenados = self.ordenamiento_jugadores()

        if largo_jugadores(jugadores_ordenados) < 11:
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
