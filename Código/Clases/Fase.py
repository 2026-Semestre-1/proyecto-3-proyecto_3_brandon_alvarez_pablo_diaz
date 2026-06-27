import random

from Clases.Partido import Partido

class Fase:

    def __init__(self, nombre_fase):

        if not isinstance(nombre_fase, str):
            print("Error: el nombre de la fase no es válida")
            return
        
        self.nombre_fase = nombre_fase
        self.partidos = []
        self.penales = []

    
    def registrar_juego(self, equipo1, equipo2):

        nuevo_partido = Partido(equipo1, equipo2, self.nombre_fase, "")

        self.partidos += [nuevo_partido]

    def jugar_fase(self):
        self.penales = [] #por si se recorre dos veces, entonces se reinicia

        for partido in self.partidos:
            partido.simular()

            if partido.goles_equipo1 == partido.goles_equipo2:

                penales_equipo1 = 0
                penales_equipo2 = 0 

                while penales_equipo1 == penales_equipo2:
                    penales_equipo1 = random.randint(2, 5)
                    penales_equipo2 = random.randint(2, 5)

            self.penales += [[partido, penales_equipo1, penales_equipo2]]

    

