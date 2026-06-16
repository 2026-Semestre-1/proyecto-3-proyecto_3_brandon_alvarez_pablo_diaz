class Pais:
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):

        if not isinstance(codigo_fifa, str):
            return "El codigo de fifa debe de ser un string."

        if not isinstance(nombre, str):
            return "El nombre debe de ser un string."

        if not isinstance(continente, str):
            return "El continente debe de ser un string."

        if not isinstance(ranking_fifa, int):
            return "El ranking de la fifa debe de ser un número entero."

        self.codigo = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking = ranking_fifa

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
        self.ranking = nuevoRanking_fifa

        return True

    def mostrar_datos(self):
        return {
            "codigo_fifa": self.codigo,
            "nombre": self.nombre,
            "continente": self.continente,
            "ranking_fifa": self.ranking,
        }
