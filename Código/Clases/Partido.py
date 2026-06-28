# =========================================== Librerias ============================================
import random
from Clases.Seleccion import Seleccion

# ==================================================================================================


# ========================================= Clase Partido =========================================
# Nombre: Partido
# Entradas: equipo_1, equipo_2, fase, grupo, fecha.
# Salidas: equipo_1, equipo_2, fase, grupo, fecha.
# Restricciones:
# ==================================================================================================
class Partido:

    contador_id = 0

    def __init__(self, equipo_1, equipo_2, fase, grupo, fecha):

        Partido.contador_id += 1

        self.id_partido = Partido.contador_id
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.fase = fase
        self.grupo = grupo
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.fecha = fecha

    # =================================== Funcion simular ==========================================
    # Nombre: simular
    # Entradas: ninguna.
    # Salidas: ejecuta el algoritmo de simulación y asigna los goles de cada equipo..
    # Restricciones:
    # ==============================================================================================
    def simular(self):

        diferencia_fuerza = Seleccion.calcular_fuerza_equipo(self.equipo_1) - Seleccion.calcular_fuerza_equipo(self.equipo_2)

        if diferencia_fuerza < 0:
            diferencia_fuerza *= -1

        self.goles_equipo1 = random.randint(0, 4)
        self.goles_equipo2 = random.randint(0, 4)

        if diferencia_fuerza < 0:
            equipo_fuerte = "equipo1"
        elif diferencia_fuerza > 0:
            equipo_fuerte = "equipo2"
        else:
            equipo_fuerte = "empate_fuerza"

        if diferencia_fuerza > 15:
            if equipo_fuerte == "equipo1":
                self.goles_equipo1 = random.randint(1, 5)
            elif equipo_fuerte == "equipo2":
                self.goles_equipo2 = random.randint(1, 5)

        elif diferencia_fuerza > 30:
            if equipo_fuerte == "equipo1":
                self.goles_equipo1 = random.randint(2, 7)
                self.goles_equipo2 = random.randint(0, 3)
            elif equipo_fuerte == "equipo2":
                self.goles_equipo2 = random.randint(2, 7)
                self.goles_equipo1 = random.randint(0, 3)
        else:
            pass

        return self.goles_equipo1, self.goles_equipo2

    # =================================== Funcion generar ganador ==================================
    # Nombre: generar_ganador
    # Entradas: ninguna.
    # Salidas: el equipo que ganó el partido.
    # Restricciones:
    # ==============================================================================================
    def generar_ganador(self):

        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo_1

        elif self.goles_equipo2 > self.goles_equipo1:
            return self.equipo_2

        else:
            if "grupos" not in self.fase.lower():
                return None  # en fase de grupos, el empate es un resultado válido
            else:
                return None  # si es otra fase, quiere decir que aún no hay ganador, entonces se debe ir a penales

    # =================================== Funcion mostrarresultado ==================================
    # Nombre: mostrar_resultado
    # Entradas: ninguna.
    # Salidas: un diccionario con los resultados del partido.
    # Restricciones:
    # ==============================================================================================
    def mostrar_resultado(self):
        return {"equipo_1": self.equipo_1, "equipo_2": self.equipo_2}
