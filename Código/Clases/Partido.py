class Partido:

    contador_id = 0

    def __init__(self, equipo_1, equipo_2, fase, grupo):

        Partido.contador_id += 1

        self.id_partido = Partido.contador_id
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.fase = fase
        self.grupo = grupo
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0


    def simular(): #TODO falta que se termine el metodo para esta función

    
    def generar_ganador(self):

        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo_1
        
        elif self.goles_equipo2 > self.goles_equipo1:
            return self.equipo_2

        else: 
            if "grupos" not in self.fase.lower():
                return None #en fase de grupos, el empate es un resultado válido
            else:
                return None #si es otra fase, quiere decir que aún no hay ganador, entonces se debe ir a penales
            
    def mostrar_resultado(self):
        return {
            "equipo_1": self.equipo_1,
            "equipo_2": self.equipo_2
        }




