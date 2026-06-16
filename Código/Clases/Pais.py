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
