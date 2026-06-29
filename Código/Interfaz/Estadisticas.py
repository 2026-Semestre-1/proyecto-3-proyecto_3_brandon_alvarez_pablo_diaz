# ========================================== Librerias =============================================
from Persistencia import *
import customtkinter as ctk
# ==================================================================================================

# ========================================= Clase Ventana Estadisticas =============================
# Nombre: VentanaEstadisticas
# Entradas: ninguna.
# Salidas: Ventana de estadísticas y rankings del mundial.
# Restricciones:
# ==================================================================================================
class VentanaEstadisticas(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Estadísticas / Rankings")
        self.geometry("700x500")
        self.resizable(False, False)
        
        self.attributes('-topmost', True)


        self.pestanas = ctk.CTkTabview(self)
        self.pestanas.pack(padx=20, pady=20, fill="both", expand=True)

        self.pestanas.add("Ranking Goleadores")
        self.pestanas.add("Ranking Selecciones")
        self.pestanas.add("Estadísticas Generales")

        self.pestana_goleadores()
        self.pestana_selecciones()
        self.pestana_generales()

    # =================================== Funcion pestaña goleadores ===============================
    # Nombre: pestana_goleadores
    # Entradas: Ninguna.
    # Salidas: Pestaña de ranking de goleadores.
    # Restricciones:
    # ==============================================================================================
    def pestana_goleadores(self):
        pestana = self.pestanas.tab("Ranking Goleadores")

        # ComboBox para elegir selección
        ctk.CTkLabel(
            pestana, text="Ranking Goleadores", font=("Arial", 18, "bold")
        ).pack(pady=(10, 0))

        # ScrollableFrame para mostrar jugadores
        self.scroll_goleadores = ctk.CTkScrollableFrame(pestana)
        self.scroll_goleadores.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkButton(
            pestana, text="Refrescar", command=self.cargar_goleadores_lista
        ).pack(pady=5)

        self.cargar_goleadores_lista()

    # =================================== Funcion cargar goleadores lista ===============================
    # Nombre: cargar_goleadores_lista
    # Entradas: Ninguna.
    # Salidas: Lista de goleadores en la pestaña correspondiente.
    # Restricciones:
    # ==============================================================================================
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

    # =================================== Funcion pestana selecciones ===============================
    # Nombre: pestana_selecciones
    # Entradas: Ninguna.
    # Salidas: Pestaña de ranking de selecciones.
    # Restricciones:
    # ==============================================================================================
    def pestana_selecciones(self):
        pestana = self.pestanas.tab("Ranking Selecciones")

        # ComboBox para elegir selección
        ctk.CTkLabel(
            pestana, text="Ranking Selecciones", font=("Arial", 18, "bold")
        ).pack(pady=(10, 0))

        # ScrollableFrame para mostrar selecciones
        self.scroll_selecciones = ctk.CTkScrollableFrame(pestana)
        self.scroll_selecciones.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkButton(
            pestana, text="Refrescar", command=self.cargar_selecciones_lista
        ).pack(pady=5)

        self.cargar_selecciones_lista()

    # =================================== Funcion cargar selecciones lista ===============================
    # Nombre: cargar_selecciones_lista
    # Entradas: Ninguna.
    # Salidas: Lista de selecciones en la pestaña correspondiente.
    # Restricciones:
    # ==============================================================================================
    def cargar_selecciones_lista(self):

        for componentes in self.scroll_selecciones.winfo_children():
            componentes.destroy()

        ranking_selecciones = cargar_ranking_selecciones()

        for seleccion in ranking_selecciones:

            nombre = seleccion[0]
            puntos = seleccion[1]
            diferencia_goles = seleccion[2]
            fase_alcanzada = seleccion[3]

            label = ctk.CTkLabel(
                self.scroll_selecciones,
                text=f"{nombre} | Puntos: {puntos} | DG: {diferencia_goles} | Fase alcanzada: {fase_alcanzada}",
                font=("Arial", 12),
            )
            label.pack(pady=5)

    # =================================== Funcion pestana generales ===============================
    # Nombre: pestana_generales
    # Entradas: Ninguna.
    # Salidas: Pestaña de estadísticas generales.
    # Restricciones:
    # ==============================================================================================
    def pestana_generales(self):
        pestana = self.pestanas.tab("Estadísticas Generales")

        ctk.CTkLabel(
            pestana, text="Estadísticas Generales", font=("Arial", 18, "bold")
        ).pack(pady=15)

        self.frame_generales = ctk.CTkFrame(pestana)
        self.frame_generales.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkButton(
            pestana, text="Refrescar", command=self.cargar_selecciones_general_lista
        ).pack(pady=5)

        self.cargar_selecciones_general_lista()

    # =================================== Funcion cargar selecciones general lista =================
    # Nombre: cargar_selecciones_general_lista
    # Entradas: Ninguna.
    # Salidas: Lista de selecciones con estadísticas generales en la pestaña correspondiente.
    # Restricciones:
    # ==============================================================================================
    def cargar_selecciones_general_lista(self):
        for componentes in self.frame_generales.winfo_children():
            componentes.destroy()

        lista_paises = cargar_pais()

        lista_entrenadores = cargar_entrenadores()

        lista_jugadores = cargar_futbolista()

        lista_selecciones = cargar_seleccion(
            lista_paises, lista_entrenadores, lista_jugadores
        )

        max_goles = None
        max_amarillas = None
        max_rojas = None

        for seleccion in lista_selecciones:

            if (
                max_goles == None
                or seleccion.total_goles_favor > max_goles.total_goles_favor
            ):
                max_goles = seleccion

            if (
                max_amarillas == None
                or seleccion.total_tarjetas_amarillas
                > max_amarillas.total_tarjetas_amarillas
            ):
                max_amarillas = seleccion

            if (
                max_rojas == None
                or seleccion.total_tarjetas_rojas > max_rojas.total_tarjetas_rojas
            ):
                max_rojas = seleccion

        if max_goles != None:
            ctk.CTkLabel(
                self.frame_generales,
                text=f"⚽ Selección con más goles: {max_goles.pais.nombre} ({max_goles.total_goles_favor} goles)",
                font=("Arial", 14),
            ).pack(pady=10)

        if max_amarillas != None:
            ctk.CTkLabel(
                self.frame_generales,
                text=f"🟨 Más tarjetas amarillas: {max_amarillas.pais.nombre} ({max_amarillas.total_tarjetas_amarillas})",
                font=("Arial", 14),
            ).pack(pady=10)

        if max_rojas != None:
            ctk.CTkLabel(
                self.frame_generales,
                text=f"🟥 Más tarjetas rojas: {max_rojas.pais.nombre} ({max_rojas.total_tarjetas_rojas})",
                font=("Arial", 14),
            ).pack(pady=10)