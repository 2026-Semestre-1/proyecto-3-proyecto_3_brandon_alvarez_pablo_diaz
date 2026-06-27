from Clases.Pais import Pais
from Clases.Persona import Persona
from Clases.Futbolista import Futbolista
from Clases.Entrenador import Entrenador
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
