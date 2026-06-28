# ========================================= Clase Pais =============================================
# Nombre: Pais
# Entradas: codigo_fifa, nombre, continente, ranking_fifa.
# Salidas: codigo_fifa, nombre, continente, ranking_fifa.
# Restricciones:
# ==================================================================================================
class Pais:
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not isinstance(codigo_fifa, str):
            raise TypeError("El codigo de fifa debe de ser un string.")

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe de ser un string.")

        if not isinstance(continente, str):
            raise TypeError("El continente debe de ser un string.")

        if not isinstance(ranking_fifa, int):
            raise TypeError("El ranking de la fifa debe de ser un número entero.")

        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa

    # =================================== Funcion actualizar_datos ===================================
    # Nombre: actualizar_datos
    # Entradas: nuevoCodigo_fifa, nuevoNombre, nuevoContinente, nuevoRanking_fifa.
    # Salidas: True si los datos del país fueron actualizados con éxito.
    # Restricciones:
    # ==============================================================================================
    def actualizar_datos(
        self, nuevoCodigo_fifa, nuevoNombre, nuevoContinente, nuevoRanking_fifa
    ):

        if not isinstance(nuevoCodigo_fifa, str):
            return "El codigo de fifa debe de ser un string."

        if not isinstance(nuevoNombre, str):
            return "El nombre debe de ser un string."

        if not isinstance(nuevoContinente, str):
            return "El continente debe de ser un string."

        if not isinstance(nuevoRanking_fifa, int):
            return "El ranking de la fifa debe de ser un número entero."

        self.codigo = nuevoCodigo_fifa
        self.nombre = nuevoNombre
        self.continente = nuevoContinente
        self.ranking_fifa = nuevoRanking_fifa

        return True

    # =================================== Funcion mostrar_datos ===================================
    # Nombre: mostrar_datos
    # Entradas: ninguna.
    # Salidas: Un diccionario con los datos del país.
    # Restricciones:
    # ==============================================================================================
    def mostrar_datos(self):
        return {
            "codigo_fifa": self.codigo,
            "nombre": self.nombre,
            "continente": self.continente,
            "ranking_fifa": self.ranking_fifa,
        }
