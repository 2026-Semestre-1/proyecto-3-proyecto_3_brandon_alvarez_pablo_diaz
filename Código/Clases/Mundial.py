# =========================================== Librerias ============================================
from Clases.Fase import Fase
from Clases.Grupo import Grupo
from Clases.Pais import Pais
from Clases.Seleccion import Seleccion
from Utilidades import largoLista
from Persistencia import *

# ==================================================================================================


# ========================================= Clase Mundial =========================================
# Nombre: Mundial
# Entradas: nombre y anio(año).
# Salidas: nombre, anio(año), paises, selecciones, grupos, fases, campeon.
# Restricciones:
# ==================================================================================================
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

    # =================================== Funcion registrar país ===================================
    # Nombre: registrar_pais
    # Entradas: pais.
    # Salidas: True si el país fue guardado con éxito.
    # Restricciones:
    # ==============================================================================================

    def registrar_pais(self, pais):

        if not isinstance(pais, Pais):
            return "El país debe de ser un objeto de la clase Pais."

        self.paises += [pais]

        return True

    # ================================ Funcion registrar seleccion =================================
    # Nombre: registrar_seleccion
    # Entradas: seleccion.
    # Salidas: True si la seleccion fue guardado con éxito.
    # Restricciones:
    # ==============================================================================================

    def registrar_seleccion(self, seleccion):

        if not isinstance(seleccion, Seleccion):
            return "La seleccion debe de ser un objeto de la clase Seleccion."

        self.selecciones += [seleccion]

        return True

    # ================================ Funcion crear grupos ========================================
    # Nombre: crear_grupos
    # Entradas: Cantidad_grupos.
    # Salidas: Grupos creados con las selecciones
    # Restricciones:
    # ==============================================================================================

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

    # ================================ Funcion jugar fase grupos ==================================
    # Nombre: jugar_fase_grupos
    # Entradas: Ninguna.
    # Salidas: Ejecuta jugar_partidos() de cada grupo y calcula sus tablas.
    # Restricciones:
    # ==============================================================================================

    def jugar_fase_grupos(self):

        if self.grupos == []:
            print("No hay grupos, por favor crear grupos para poder jugar.")
            return False

        for grupo in self.grupos:

            grupo.jugar_partidos()
            grupo.calcular_tabla()

        return True

    # ================================ Funcion armar fase eliminatoria =============================
    # Nombre: armar_fase_eliminatoria
    # Entradas: nombre_fase y clasificados.
    # Salidas: Crea los enfrentamientos de la fase eliminatoria a partir de los equipos clasificados.
    # Restricciones:
    # ==============================================================================================

    def armar_fase_eliminatoria(self, nombre_fase, clasificados):

        largo_clasificados = largoLista(clasificados)

        indice = 0

        fase = Fase(nombre_fase)

        while indice < largo_clasificados:

            fase.registrar_juego(clasificados[indice], clasificados[indice + 1])

            indice += 2

        self.fases += [fase]

        return fase

    # ================================ Funcion jugar fase eliminatoria =============================
    # Nombre: jugar_fase_eliminatoria
    # Entradas: fase
    # Salidas: ejecuta jugar_fase() de la fase indicada y retorna los clasificados a la siguiente ronda.
    # Restricciones:
    # ==============================================================================================

    def jugar_fase_eliminatoria(self, fase):

        fase.jugar_fase()

        return fase.obtener_clasificados()

    # ================================ Funcion determinar campeon ==================================
    # Nombre: determinar_campeon
    # Entradas: Ninguna.
    # Salidas: Ejecuta el flujo completo desde octavos (o dieciseisavos) hasta la final asigna el atributo campeon.
    # Restricciones:
    # ==============================================================================================

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

        return True

    # ================================ Funcion nombre final ========================================
    # Nombre: nombre_final
    # Entradas: largo_clasificados
    # Salidas: Determina el nombre de la fase que se esta jugando.
    # Restricciones:
    # ==============================================================================================

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

    # ================================ Funcion mostrar tabla general ===============================
    # Nombre: mostrar_tabla_general
    # Entradas: Ninguna.
    # Salidas: Muestra las tablas de posiciones de todos los grupos.
    # Restricciones:
    # ==============================================================================================

    def mostrar_tabla_general(self):

        for grupo in self.grupos:

            grupo.mostrar_tabla()

        return True

    # ================================ Funcion generar_reporte =====================================
    # Nombre: generar_reporte
    # Entradas: Ninguna.
    # Salidas: Genera el archivo de estadísticas generales del torneo.
    # Restricciones:
    # ==============================================================================================

    def generar_reporte(self):

        todos_jugadores = []

        for seleccion in self.selecciones:

            todos_jugadores += seleccion.jugadores

        selecciones_puntos = []

        for grupo in self.grupos:

            for fila in grupo.tabla:

                selecciones_puntos += [[fila[0], fila[1]]]

        guardar_ranking_goleadores(todos_jugadores)
        guardar_ranking_selecciones(selecciones_puntos)

        return
