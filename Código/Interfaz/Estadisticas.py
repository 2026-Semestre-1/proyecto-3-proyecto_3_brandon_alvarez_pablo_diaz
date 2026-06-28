import os
import sys

# 1. Obtenemos la ruta de la carpeta "Interfaz" donde está este archivo
carpeta_interfaz = os.path.dirname(os.path.abspath(__file__))

# 2. Subimos un nivel para obtener la ruta de la carpeta "Código"
carpeta_codigo = os.path.dirname(carpeta_interfaz)

# 3. Le decimos a Python: "¡Ey! También busque archivos para importar aquí"
sys.path.append(carpeta_codigo)


from Persistencia import *
import customtkinter as ctk


class VentanaEstadisticas(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Estadísticas / Rankings")
        self.geometry("700x500")
        self.resizable(False, False)

        self.pestanas = ctk.CTkTabview(self)
        self.pestanas.pack(padx=20, pady=20, fill="both", expand=True)

        self.pestanas.add("Ranking Goleadores")
        self.pestanas.add("Ranking Selecciones")
        # self.pestanas.add("Estadísticas Generales")

        self.pestaña_goleadores()
        self.pestana_selecciones()
        # self.pestana_generales()

    def pestaña_goleadores(self):
        pestana = self.pestanas.tab("Ranking Goleadores")

        # ComboBox para elegir selección
        ctk.CTkLabel(
            pestana, text="Ranking Goleadores", font=("Arial", 18, "bold")
        ).pack(pady=(10, 0))

        # ScrollableFrame para mostrar jugadores
        self.scroll_goleadores = ctk.CTkScrollableFrame(pestana)
        self.scroll_goleadores.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_goleadores_lista()

    def cargar_goleadores_lista(self):

        for componentes in self.scroll_goleadores.winfo_children():
            componentes.destroy()

        ranking_goleadores = cargar_ranking_goleadores()

        for jugador in ranking_goleadores:

            nombre = jugador[0]
            goles = jugador[1]

            label = ctk.CTkLabel(
                self.scroll_goleadores,
                text=f"{nombre} | Goles: {goles}",
                font=("Arial", 12),
            )
            label.pack(pady=5)

    def pestana_selecciones(self):
        pestana = self.pestanas.tab("Ranking Selecciones")

        # ComboBox para elegir selección
        ctk.CTkLabel(
            pestana, text="Ranking Selecciones", font=("Arial", 18, "bold")
        ).pack(pady=(10, 0))

        # ScrollableFrame para mostrar jugadores
        self.scroll_selecciones = ctk.CTkScrollableFrame(pestana)
        self.scroll_selecciones.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_selecciones_lista()

    def cargar_selecciones_lista(self):

        for componentes in self.scroll_selecciones.winfo_children():
            componentes.destroy()

        ranking_selecciones = cargar_ranking_selecciones()

        for seleccion in ranking_selecciones:

            nombre = seleccion[0]
            puntos = seleccion[1]
            diferencia_goles = seleccion[2]

            label = ctk.CTkLabel(
                self.scroll_selecciones,
                text=f"{nombre} | Puntos: {puntos} | DG: {diferencia_goles}",
                font=("Arial", 12),
            )
            label.pack(pady=5)


if __name__ == "__main__":
    app = VentanaEstadisticas()
    app.mainloop()
