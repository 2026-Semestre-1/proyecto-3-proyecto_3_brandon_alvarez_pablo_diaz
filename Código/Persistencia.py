from Clases.Pais import Pais
from Clases.Futbolista import Futbolista
from Clases.Seleccion import Seleccion
from Utilidades import *


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


def cargar_seleccion(lista_paises, lista_entrenadores, lista_jugadores):

    lista = []

    try:

        archivo = open("Código/Archivos_txt/selecciones.txt", "r")

        for linea in archivo:
            partes = linea.strip().split("|")

            for pais in lista_paises:

                if pais.codigo_fifa == partes[0]:

                    pais_encontrado = pais

                    break

            seleccion_uso = Seleccion(partes[1], pais_encontrado)

            if partes[2] != "None":

                for entrenador in lista_entrenadores:

                    if (
                        entrenador.nombre == partes[2]
                        and entrenador.apellido == partes[3]
                    ):

                        entrenador_encontrado = entrenador

                        break

                seleccion_uso.asignar_entrenador(entrenador_encontrado)

            for jugador in lista_jugadores:

                if jugador.codigo_equipo == partes[1]:

                    seleccion_uso.agregar_jugador(jugador)

            lista += [seleccion_uso]

        archivo.close()

    except FileNotFoundError:
        pass  # si el archivo no existe, arranca vacío

    return lista


def guardar_partidos_grupo(grupo):

    archivo = open("Código/Archivos_txt/partidos.txt", "a")

    for partido in grupo.partidos:
        linea = ( str(grupo.nombre_grupo) + "|" 
                 + str(partido.equipo_1.pais.nombre) + "|"
                 + str(partido.equipo_2.pais.nombre) + "|"
                 + str(partido.goles_equipo1) + "|"
                 + str(partido.goles_equipo2) + "|"
                 + str(partido.fecha) + "\n")
        archivo.write(linea)

    archivo.close()


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

        linea = ( str(fase.nombre_fase) + "|" 
                 + str(partido.equipo_1.pais.nombre) + "|"
                 + str(partido.equipo_2.pais.nombre) + "|"
                 + str(partido.goles_equipo1) + "|"
                 + str(partido.goles_equipo2) + "|"
                 + str(partido.fecha) + "\n")
        
        if tiene_penales == True:
            linea += str(penales_equipo1) + "|" + str(penales_equipo2) + "\n"
        else:
            linea += "0|0\n"

        archivo.write(linea)

    archivo.close()


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

                datos_partido = [fase_o_grupo, nombre_equipo1, nombre_equipo2, goles_equipo1, goles_equipo2, fecha, penales_equipo1, penales_equipo2] 

                partidos += [datos_partido]

            archivo.close()
        
        except FileNotFoundError:
            pass # si el archivo no existe, arranca vacío

        return partidos
    
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

        nombre_completo = str(jugador.nombre) + " " + str(jugador.apellido) + " " + " (#" + str(jugador.dorsal) + ")"

        linea = nombre_completo + "|" + str(jugador.goles) + "\n"
        archivo.write(linea)

    archivo.close()
