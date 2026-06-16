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

    def actualizar_datos(self, n_codigo_fifa, n_nombre, n_continente, n_ranking_fifa):

        if not isinstance(n_codigo_fifa, str):
            return "El codigo de fifa debe de ser un string."

        if not isinstance(n_nombre, str):
            return "El nombre debe de ser un string."

        if not isinstance(n_continente, str):
            return "El continente debe de ser un string."

        if not isinstance(n_ranking_fifa, int):
            return "El ranking de la fifa debe de ser un número entero."

        self.codigo = n_codigo_fifa
        self.nombre = n_nombre
        self.continente = n_continente
        self.ranking = n_ranking_fifa

        return True
