from Clases.Pais import Pais
from Clases.Futbolista import Futbolista
from Clases.Entrenador import Entrenador


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
        str(seleccion.codigo_equipo)
        + "|"
        + str(seleccion.pais.codigo_fifa)
        + "|"
        + str(nombre_e)
        + "|"
        + str(apellido_e)
        + "\n"
    )
    archivo.close()


def cargar_seleccion(lista_paises, lista_entrenadores, lista_jugadores):

    pass
