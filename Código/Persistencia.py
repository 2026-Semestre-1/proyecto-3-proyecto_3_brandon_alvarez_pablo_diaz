# ========================================== Librerias =============================================
from Clases.Pais import Pais
from Clases.Futbolista import Futbolista
from Clases.Seleccion import Seleccion
from Clases.Entrenador import Entrenador
from Utilidades import *

# ==================================================================================================


# =================================== Funcion guardar entrenador ===================================
# Nombre: guardar_entrenador
# Entradas: nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego, codigo_equipo.
# Salidas: None.
# Restricciones:
# ==============================================================================================
def guardar_entrenador(
    nombre,
    apellido,
    fecha_nacimiento,
    nacionalidad,
    licencia,
    experiencia_anios,
    sistema_juego,
    codigo_equipo,
):

    archivo = open("Código/Archivos_txt/entrenadores.txt", "a")
    archivo.write(
        str(nombre)
        + "|"
        + str(apellido)
        + "|"
        + str(fecha_nacimiento)
        + "|"
        + str(nacionalidad)
        + "|"
        + str(licencia)
        + "|"
        + str(experiencia_anios)
        + "|"
        + str(sistema_juego)
        + "|"
        + str(codigo_equipo)
        + "\n"
    )
    archivo.close()


# =================================== Funcion modificar_entrenadores =====================================
# Nombre: modificar_entrenadores
# Entradas: lista_entrenadores.
# Salidas: None.
# Restricciones:
# ==============================================================================================
def modificar_entrenadores(lista_entrenadores):

    archivo = open("Código/Archivos_txt/entrenadores.txt", "w")
    for entrenador in lista_entrenadores:
        archivo.write(
            str(entrenador.nombre)
            + "|"
            + str(entrenador.apellido)
            + "|"
            + str(entrenador.fecha_nacimiento)
            + "|"
            + str(entrenador.nacionalidad)
            + "|"
            + str(entrenador.licencia)
            + "|"
            + str(entrenador.experiencia_anios)
            + "|"
            + str(entrenador.sistema_juego)
            + "|"
            + str(entrenador.codigo_equipo)
            + "\n"
        )
    archivo.close()


# =================================== Funcion cargar entrenadores ======================================
# Nombre: cargar_entrenadores
# Entradas: ninguna.
# Salidas: Lista de entrenadores cargada desde el archivo.
# Restricciones:
# ==============================================================================================
def cargar_entrenadores():

    lista = []

    try:

        archivo = open("Código/Archivos_txt/entrenadores.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            partes[5] = int(partes[5])

            entrenador = Entrenador(
                partes[0],
                partes[1],
                partes[2],
                partes[3],
                partes[4],
                partes[5],
                partes[6],
            )

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return lista


# =================================== Funcion guardar pais =====================================
# Nombre: guardar_pais
# Entradas: codigo_fifa, nombre, continente, ranking_fifa.
# Salidas: None.
# Restricciones:
# ==============================================================================================
def guardar_pais(codigo_fifa, nombre, continente, ranking_fifa):

    archivo = open("Código/Archivos_txt/paises.txt", "a")
    archivo.write(
        str(codigo_fifa)
        + "|"
        + str(nombre)
        + "|"
        + str(continente)
        + "|"
        + str(ranking_fifa)
        + "\n"
    )
    archivo.close()


# =================================== Funcion modificar_pais =====================================
# Nombre: modificar_pais
# Entradas: lista_paises, codigo_fifa, nuevo_nombre, nuevo_continente, nuevo_ranking_fifa.
# Salidas: None.
# Restricciones:
# ==============================================================================================
def modificar_pais(
    lista_paises, codigo_fifa, nuevo_nombre, nuevo_continente, nuevo_ranking_fifa
):

    for pais in lista_paises:

        if pais.codigo_fifa == codigo_fifa:

            pais.nombre = nuevo_nombre
            pais.continente = nuevo_continente
            pais.ranking_fifa = nuevo_ranking_fifa
            break

    archivo = open("Código/Archivos_txt/paises.txt", "w")

    for pais in lista_paises:

        archivo.write(
            str(pais.codigo_fifa)
            + "|"
            + str(pais.nombre)
            + "|"
            + str(pais.continente)
            + "|"
            + str(pais.ranking_fifa)
            + "\n"
        )
    archivo.close()


# =================================== Funcion cargar pais ======================================
# Nombre: cargar_pais
# Entradas: ninguna.
# Salidas: Lista de países cargada desde el archivo.
# Restricciones:
# ==============================================================================================
def cargar_pais():

    lista = []

    try:

        archivo = open("Código/Archivos_txt/paises.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            partes[3] = int(partes[3])

            lista += [Pais(partes[0], partes[1], partes[2], partes[3])]

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return lista


# =================================== Funcion guardar Futbolista ======================================
# Nombre: guardar_Futbolista
# Entradas: nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual, codigo_equipo.
# Salidas: None.
# Restricciones:
# ==============================================================================================
def guardar_Futbolista(
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
    codigo_equipo,
):

    archivo = open("Código/Archivos_txt/jugadores.txt", "a")
    archivo.write(
        str(nombre)
        + "|"
        + str(apellido)
        + "|"
        + str(fecha_nacimiento)
        + "|"
        + str(nacionalidad)
        + "|"
        + str(dorsal)
        + "|"
        + str(posicion)
        + "|"
        + str(total_tarjetas_amarillas)
        + "|"
        + str(total_tarjetas_rojas)
        + "|"
        + str(goles)
        + "|"
        + str(asistencias)
        + "|"
        + str(puntaje_individual)
        + "|"
        + str(codigo_equipo)
        + "\n"
    )
    archivo.close()


# =================================== Funcion modificar_futbolistas =====================================
# Nombre: modificar_futbolistas
# Entradas: lista_futbolistas.
# Salidas: None.
# Restricciones:
# ==============================================================================================
def modificar_futbolistas(lista_futbolistas):

    archivo = open("Código/Archivos_txt/jugadores.txt", "w")
    for futbolista in lista_futbolistas:
        archivo.write(
            str(futbolista.nombre)
            + "|"
            + str(futbolista.apellido)
            + "|"
            + str(futbolista.fecha_nacimiento)
            + "|"
            + str(futbolista.nacionalidad)
            + "|"
            + str(futbolista.dorsal)
            + "|"
            + str(futbolista.posicion)
            + "|"
            + str(futbolista.total_tarjetas_amarillas)
            + "|"
            + str(futbolista.total_tarjetas_rojas)
            + "|"
            + str(futbolista.goles)
            + "|"
            + str(futbolista.asistencias)
            + "|"
            + str(futbolista.puntaje_individual)
            + "|"
            + str(futbolista.codigo_equipo)
            + "\n"
        )
    archivo.close()


# =================================== Funcion cargar futbolista ================================
# Nombre: cargar_futbolista
# Entradas: ninguna.
# Salidas: Lista de futbolistas cargada desde el archivo.
# Restricciones:
# ==============================================================================================
def cargar_futbolista():

    lista = []

    try:

        archivo = open("Código/Archivos_txt/jugadores.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            partes[4] = int(partes[4])
            partes[6] = int(partes[6])
            partes[7] = int(partes[7])
            partes[8] = int(partes[8])
            partes[9] = int(partes[9])
            partes[10] = int(partes[10])

            jugador = Futbolista(
                partes[0],
                partes[1],
                partes[2],
                partes[3],
                partes[4],
                partes[5],
                partes[6],
                partes[7],
                partes[8],
                partes[9],
                partes[10],
            )

            jugador.codigo_equipo = partes[11]
            lista += [jugador]

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return lista


# =================================== Funcion guardar seleccion ================================
# Nombre: guardar_seleccion
# Entradas: seleccion.
# Salidas: None.
# Restricciones:
# ==============================================================================================
def guardar_seleccion(seleccion):

    if seleccion.entrenador != None:
        nombre_e = seleccion.entrenador.nombre
        apellido_e = seleccion.entrenador.apellido

    else:
        nombre_e = "None"
        apellido_e = "None"

    archivo = open("Código/Archivos_txt/selecciones.txt", "a")
    archivo.write(
        str(seleccion.pais.codigo_fifa)
        + "|"
        + str(seleccion.codigo_equipo)
        + "|"
        + str(nombre_e)
        + "|"
        + str(apellido_e)
        + "\n"
    )
    archivo.close()


# =================================== Funcion asignar_entrenador_seleccion =================================
# Nombre: asignar_entrenador_seleccion
# Entradas: codigo_equipo, nombre_entrenador, apellido_entrenador
# Salidas: None
# Restricciones:
# ==============================================================================================
def asignar_entrenador_seleccion(codigo_equipo, nombre_entrenador, apellido_entrenador):

    try:
        archivo = open("Código/Archivos_txt/selecciones.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

    except FileNotFoundError:
        return

    lineas_actualizadas = []

    for linea in lineas:
        partes = linea.strip().split("|")

        if len(partes) >= 2 and partes[1] == codigo_equipo:

            partes[2] = nombre_entrenador
            partes[3] = apellido_entrenador

            linea_actualizada = "|".join(partes) + "\n"
            lineas_actualizadas += [linea_actualizada]

        else:
            lineas_actualizadas += [linea]

    archivo = open("Código/Archivos_txt/selecciones.txt", "w")
    archivo.writelines(lineas_actualizadas)
    archivo.close()


# =================================== Funcion cargar seleccion =================================
# Nombre: cargar_seleccion
# Entradas: ninguna.
# Salidas: Lista de selecciones cargada desde el archivo.
# Restricciones:
# ==============================================================================================
def cargar_seleccion(lista_paises, lista_entrenadores, lista_jugadores):

    lista = []

    try:

        archivo = open("Código/Archivos_txt/selecciones.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            pais_encontrado = None

            for pais in lista_paises:

                if pais.codigo_fifa == partes[0]:

                    pais_encontrado = pais

                    break

            if pais_encontrado == None:
                continue

            seleccion_uso = Seleccion(partes[1], pais_encontrado)

            if partes[2] != "None":

                entrenador_encontrado = None

                for entrenador in lista_entrenadores:

                    if (
                        entrenador.nombre == partes[2]
                        and entrenador.apellido == partes[3]
                    ):

                        entrenador_encontrado = entrenador

                        break

                if entrenador_encontrado != None:
                    seleccion_uso.asignar_entrenador(entrenador_encontrado)

            for jugador in lista_jugadores:

                if jugador.codigo_equipo == partes[1]:

                    seleccion_uso.agregar_jugador(jugador)

            lista += [seleccion_uso]

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return lista


# =================================== Funcion guardar partidos grupo ===========================
# Nombre: guardar_partidos_grupo
# Entradas: grupo (objeto de tipo Grupo)
# Salidas: Ninguna
# Restricciones:
# ==============================================================================================
def guardar_partidos_grupo(grupo):

    archivo = open("Código/Archivos_txt/partidos.txt", "a")

    for partido in grupo.partidos:
        linea = (
            str(grupo.nombre_grupo)
            + "|"
            + str(partido.equipo_1.pais.nombre)
            + "|"
            + str(partido.equipo_2.pais.nombre)
            + "|"
            + str(partido.goles_equipo1)
            + "|"
            + str(partido.goles_equipo2)
            + "|"
            + str(partido.fecha)
            + "\n"
        )
        archivo.write(linea)

    archivo.close()


# =================================== Funcion guardar partidos fase ============================
# Nombre: guardar_partidos_fase
# Entradas: fase (objeto de tipo Fase)
# Salidas: Ninguna
# Restricciones:
# ==============================================================================================
def guardar_partidos_fase(fase):

    archivo = open("Código/Archivos_txt/partidos.txt", "a")

    for partido in fase.partidos:
        tiene_penales = False
        penales_equipo1 = 0
        penales_equipo2 = 0

        for registro in fase.penales:
            if registro[0] == partido:
                tiene_penales = True
                penales_equipo1 = registro[1]
                penales_equipo2 = registro[2]

        linea = (
            str(fase.nombre_fase)
            + "|"
            + str(partido.equipo_1.pais.nombre)
            + "|"
            + str(partido.equipo_2.pais.nombre)
            + "|"
            + str(partido.goles_equipo1)
            + "|"
            + str(partido.goles_equipo2)
            + "|"
            + str(partido.fecha)
            + "\n"
        )

        if tiene_penales == True:
            linea += str(penales_equipo1) + "|" + str(penales_equipo2) + "\n"
        else:
            linea += "0|0\n"

        archivo.write(linea)

    archivo.close()


# =================================== Funcion cargar partidos ==================================
# Nombre: cargar_partidos
# Entradas: ninguna.
# Salidas: Lista de partidos cargada desde el archivo.
# Restricciones:
# ==============================================================================================
def cargar_partidos():

    partidos = []

    try:
        archivo = open("Código/Archivos_txt/partidos.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            fase_o_grupo = partes[0]
            nombre_equipo1 = partes[1]
            nombre_equipo2 = partes[2]
            goles_equipo1 = int(partes[3])
            goles_equipo2 = int(partes[4])
            fecha = partes[5]
            penales_equipo1 = int(partes[6])
            penales_equipo2 = int(partes[7])

            datos_partido = [
                fase_o_grupo,
                nombre_equipo1,
                nombre_equipo2,
                goles_equipo1,
                goles_equipo2,
                fecha,
                penales_equipo1,
                penales_equipo2,
            ]

            partidos += [datos_partido]

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return partidos


# =================================== Funcion guardar ranking goleadores =======================
# Nombre: guardar_ranking_goleadores
# Entradas: lista_futbolistas (lista de objetos de tipo Futbolista)
# Salidas: Ninguna
# Restricciones:
# ==============================================================================================
def guardar_ranking_goleadores(lista_futbolistas):

    tamanno = largoLista(lista_futbolistas)

    for i in range(tamanno):
        for j in range(0, tamanno - i - 1):

            if lista_futbolistas[j].goles < lista_futbolistas[j + 1].goles:
                temporal = lista_futbolistas[j]
                lista_futbolistas[j] = lista_futbolistas[j + 1]
                lista_futbolistas[j + 1] = temporal

    archivo = open("Código/Archivos_txt/ranking_goleadores.txt", "w")

    for jugador in lista_futbolistas:

        nombre_completo = (
            str(jugador.nombre)
            + " "
            + str(jugador.apellido)
            + " "
            + " (#"
            + str(jugador.dorsal)
            + ")"
        )

        linea = nombre_completo + "|" + str(jugador.goles) + "\n"
        archivo.write(linea)

    archivo.close()


# =================================== Funcion cargar ranking goleadores ========================
# Nombre: cargar_ranking_goleadores
# Entradas: ninguna.
# Salidas: Lista de goleadores cargada desde el archivo.
# Restricciones:
# ==============================================================================================
def cargar_ranking_goleadores():
    goleadores = []

    try:

        archivo = open("Código/Archivos_txt/ranking_goleadores.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            nombre_jugador = partes[0]
            goles = int(partes[1])

            datos_jugador = [nombre_jugador, goles]

            goleadores += [datos_jugador]

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return goleadores


# =================================== Funcion guardar ranking selecciones ======================
# Nombre: guardar_ranking_selecciones
# Entradas: lista_selecciones (lista de listas [seleccion, puntos])
# Salidas: Ninguna
# Restricciones:
# ==============================================================================================
def guardar_ranking_selecciones(lista_selecciones):

    # [seleccion, puntos]

    tamanno = largoLista(lista_selecciones)

    for i in range(tamanno):
        for j in range(0, tamanno - i - 1):

            seleccion_actual = lista_selecciones[j][0]
            puntos_actual = lista_selecciones[j][1]
            diferencia_goles_actual = (seleccion_actual.total_goles_favor - seleccion_actual.total_goles_contra)

            # datos de la siguiente seleccion
            seleccion_siguiente = lista_selecciones[j + 1][0]
            puntos_siguiente = lista_selecciones[j + 1][1]
            diferencia_goles_siguiente = (seleccion_siguiente.total_goles_favor - seleccion_siguiente.total_goles_contra)

            # bandera
            intercambiar = False

            if puntos_actual < puntos_siguiente:
                intercambiar = True
            # si se empatan de puntos, entonces por la diferencia de goles
            elif puntos_actual == puntos_siguiente:
                if diferencia_goles_actual < diferencia_goles_siguiente:
                    intercambiar = True

            if intercambiar == True:
                temporal = lista_selecciones[j]
                lista_selecciones[j] = lista_selecciones[j + 1]
                lista_selecciones[j + 1] = temporal

    archivo = open("Código/Archivos_txt/ranking_selecciones.txt", "w")

    for dato in lista_selecciones:
        seleccion = dato[0]
        puntos = dato[1]
        diferencia_goles = seleccion.total_goles_favor - seleccion.total_goles_contra

        linea = (
            str(seleccion.pais.nombre)
            + "|"
            + str(puntos)
            + "|"
            + str(diferencia_goles)
            + "|"
            + str(seleccion.fase_alcanzada)
            + "\n"
        )

        archivo.write(linea)

    archivo.close()


# =================================== Funcion cargar ranking selecciones =======================
# Nombre: cargar_ranking_selecciones
# Entradas: ninguna.
# Salidas: Lista de selecciones cargada desde el archivo.
# Restricciones:
# ==============================================================================================
def cargar_ranking_selecciones():

    selecciones = []

    try:

        archivo = open("Código/Archivos_txt/ranking_selecciones.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            nombre_seleccion = partes[0]
            puntos = int(partes[1])
            diferencia_goles = int(partes[2])
            fase_alcanzada = partes[3]

            datos_seleccion = [nombre_seleccion, puntos, diferencia_goles, fase_alcanzada]

            selecciones += [datos_seleccion]

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return selecciones
