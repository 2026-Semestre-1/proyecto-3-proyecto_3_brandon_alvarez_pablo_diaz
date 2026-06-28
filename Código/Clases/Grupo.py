# ========================================== Librerias =============================================
from Clases.Seleccion import Seleccion
from Clases.Partido import Partido

# ==================================================================================================


# ================================= Función largo seleccion ========================================
# Nombre: largo_seleccion
# Entradas: lista_equipos
# Salidas: Largo de la lista de equipos
# Restricciones:
# ==================================================================================================
def largo_seleccion(lista_equipos):

    largo = 0

    for i in lista_equipos:
        largo += 1

    return largo


# ================================= Función largoLista =============================================
# Nombre: largoLista
# Entradas: lista
# Salidas: Largo de la lista
# Restricciones:
# ==================================================================================================
def largoLista(lista):

    largo = 0

    for i in lista:
        largo += 1

    return largo


# ======================================= Clase Grupo =========================================
# Nombre: Grupo
# Entradas: nombre_grupo
# Salidas: nombre_grupo, equipos, partidos, tabla y fechas_temporales.
# Restricciones:
# ==================================================================================================
class Grupo:

    def __init__(self, nombre_grupo):

        self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []
        self.tabla = []
        self.fechas_temporales = [
            "01/01/2026",
            "01/01/2026",
            "01/01/2026",
            "01/01/2026",
            "01/01/2026",
            "01/01/2026",
        ]

    # ================================= Función agregar equipo ==========================================
    # Nombre: agregar_equipo
    # Entradas: seleccion
    # Salidas: Agrega una selección al grupo
    # Restricciones:
    # ==================================================================================================
    def agregar_equipo(self, seleccion):

        if not isinstance(seleccion, Seleccion):
            return print("Error: la selección es inválida")

        if largo_seleccion(self.equipos) < 4:
            self.equipos += [seleccion]
        else:
            print(f"No se puede agregar a {seleccion.pais.nombre}. El {self.nombre_grupo} ya está lleno.")
            return

    # ================================= Función jugar partidos =========================================
    # Nombre: jugar_partidos
    # Entradas: ninguna
    # Salidas: Crea los partidos del grupo
    # Restricciones:
    # ==================================================================================================
    def jugar_partidos(self):

        self.partidos = []

        indice_fecha = 0

        for i in range(largo_seleccion(self.equipos)):
            for j in range(i + 1, largo_seleccion(self.equipos)):

                fecha_actual = self.fechas_temporales[indice_fecha]

                partido = Partido(
                    self.equipos[i],
                    self.equipos[j],
                    "Fase de Grupos",
                    self.nombre_grupo,
                    fecha_actual,
                )

                partido.simular()

                self.partidos += [partido]

                indice_fecha += 1

    # ================================= Función calcular tabla =========================================
    # Nombre: calcular_tabla
    # Entradas: ninguna
    # Salidas: Calcula la tabla del grupo
    # Restricciones:
    # ==================================================================================================
    def calcular_tabla(self):

        # [objeto Seleccion, puntos, goles_favor, goles_contra]
        self.tabla = []
        for equipo in self.equipos:
            self.tabla += [[equipo, 0, 0, 0]]

        # recorrer los partidos y actualizar la matriz
        for partido in self.partidos:
            equipo1 = partido.equipo_1
            equipo2 = partido.equipo_2
            goles_equipo_uno = partido.goles_equipo1
            goles_equipo_dos = partido.goles_equipo2
            ganador = partido.generar_ganador()

            # se buscan los equipos para actualizarlos
            for fila in self.tabla:
                if fila[0] == equipo1:  # si es el equipo 1 del partido
                    fila[2] = goles_equipo_uno
                    fila[3] = goles_equipo_dos
                    if ganador == equipo1:
                        fila[1] += 3  # se le suman los puntos si ganó el partido
                    elif ganador is None:
                        fila[1] += 1  # un punto por empatar el partido

                if fila[0] == equipo2:  # si es el equipo 2 del partido
                    fila[2] = goles_equipo_dos
                    fila[3] = goles_equipo_uno
                    if ganador == equipo2:
                        fila[1] += 3  # se le suman los puntos si ganó el partido
                    elif ganador is None:
                        fila[1] += 1  # un punto por empatar el partido

        # se ordena la tabla de mayor a menor utilizando Bubble Sort
        tamanno = largoLista(self.tabla)

        for i in range(tamanno):
            for j in range(0, tamanno - i - 1):

                fila_actual = self.tabla[j]
                fila_siguiente = self.tabla[j + 1]

                diferencia_goles_actual = fila_actual[2] - fila_siguiente[3]
                diferencia_goles_siguiente = fila_siguiente[2] - fila_siguiente[3]

                # bandera
                intercambiar = False

                # se ordena según 3 criterios: por puntos, diferencia de goles y mas goles a favor
                if fila_actual[1] < fila_siguiente[1]:
                    intercambiar = True
                elif fila_actual[1] == fila_siguiente[1]:
                    if diferencia_goles_actual < diferencia_goles_siguiente:
                        intercambiar = True
                    elif diferencia_goles_actual == diferencia_goles_siguiente:
                        if fila_actual[2] < fila_siguiente[2]:
                            intercambiar = True

                if intercambiar == True:
                    temporal = self.tabla[j]
                    self.tabla[j] = self.tabla[j + 1]
                    self.tabla[j + 1] = temporal

    # ================================= Función obtener clasificados ===================================
    # Nombre: obtener_clasificados
    # Entradas: ninguna
    # Salidas: Obtiene los equipos clasificados del grupo
    # Restricciones:
    # ==================================================================================================
    def obtener_clasificados(self):
        primer_lugar = self.tabla[0][0]
        segundo_lugar = self.tabla[1][0]

        return [primer_lugar, segundo_lugar]

    # ================================= Función mostrar tabla ===================================
    # Nombre: mostrar_tabla
    # Entradas: ninguna
    # Salidas: Muestra la tabla de posiciones del grupo
    # Restricciones:
    # ==================================================================================================
    def mostrar_tabla(self):
        return self.tabla
