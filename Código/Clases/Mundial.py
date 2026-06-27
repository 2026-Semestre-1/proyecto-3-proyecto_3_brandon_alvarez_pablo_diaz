from Clases.Entrenador import Entrenador
from Clases.Fase import Fase
from Clases.Futbolista import Futbolista
from Clases.Grupo import Grupo
from Clases.Pais import Pais
from Clases.Partido import Partido
from Clases.Seleccion import Seleccion
from Utilidades import largoLista


class Mundial:
    def __init__(self, nombre, anio):

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe de ser un string.")

        if not isinstance(anio, int):
            raise TypeError("El año debe de ser un número entero.")

        self.nombre = nombre
        self.anio = anio
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        self.campeon = None

    def registrar_pais(self, pais):

        if not isinstance(pais, Pais):
            return "El país debe de ser un objeto de la clase Pais."

        self.paises += [pais]

        return True

    def registrar_seleccion(self, seleccion):

        if not isinstance(seleccion, Seleccion):
            return "La seleccion debe de ser un objeto de la clase Seleccion."

        self.selecciones += [seleccion]

        return True

    def crear_grupos(self, cantidad_grupos):

        total_selecciones = largoLista(self.selecciones)

        if total_selecciones < cantidad_grupos:
            print(
                f"Error: No se puede crear grupos con la cantidad actual de selecciones. \nSelecciones totales: {total_selecciones}"
            )
            return False

        indice = 0

        while indice < cantidad_grupos:

            nombre = "Grupo " + chr(65 + indice)
            self.grupos += [Grupo(nombre)]

            indice += 1

        indice_seleccion = 0

        while indice_seleccion < total_selecciones:

            numero_grupo = indice_seleccion % cantidad_grupos
            self.grupos[numero_grupo].agregar_equipo(self.selecciones[indice_seleccion])

            indice_seleccion += 1

        return True

    def jugar_fase_grupos(self):

        if self.grupos == []:
            print("No hay grupos, por favor crear grupos para poder jugar.")
            return False

        for grupo in self.grupos:

            grupo.jugar_partidos()
            grupo.calcular_tabla()

        return True

    def armar_fase_eliminatoria(self, nombre_fase, clasificados):

        largo_clasificados = largoLista(clasificados)

        indice = 0

        fase = Fase(nombre_fase)

        while indice < largo_clasificados:

            fase.registrar_juego(clasificados[indice], clasificados[indice + 1])

            indice += 2

        self.fases += [fase]

        return fase

    def jugar_fase_eliminatoria(self, fase):

        fase.jugar_fase()

        return fase.obtener_clasificados()

    def determinar_campeon(self):

        clasificados = []

        for grupo in self.grupos:

            clasificados += grupo.obtener_clasificados()

        largo_clasificados = largoLista(clasificados)

        while largo_clasificados != 1:

            nombre = self.nombre_final(largo_clasificados)

            if nombre == None:

                print(
                    f"Error: cantidad de clasificados inválida ({largo_clasificados})"
                )
                return False

            fase = self.armar_fase_eliminatoria(nombre, clasificados)

            clasificados = self.jugar_fase_eliminatoria(fase)

            largo_clasificados = largoLista(clasificados)

        self.campeon = clasificados[0]

        return

    def nombre_final(self, largo_clasificados):

        if largo_clasificados == 32:
            return "Dieciseisavos de Final"

        if largo_clasificados == 16:
            return "Octavos de Final"

        if largo_clasificados == 8:
            return "Cuartos de Final"

        if largo_clasificados == 4:
            return "Semifinal"

        if largo_clasificados == 2:
            return "Final"

        return None  # número de clasificados no reconocido

    def mostrar_tabla_general(self):

        for grupo in self.grupos:

            grupo.mostrar_tabla()

        return True
