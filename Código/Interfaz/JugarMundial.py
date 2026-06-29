# ========================================== Librerias =============================================
import customtkinter as ctk
from Persistencia import *
from Clases.Mundial import Mundial
# ==================================================================================================

# ========================================= Clase Jugar Mundial ====================================
# Nombre: VentanaJugarMundial
# Entradas: ninguna.
# Salidas: Ventana de juego del mundial.
# Restricciones:
# ==================================================================================================
class VentanaJugarMundial(ctk.CTkToplevel):

    def __init__(self, parent, mundial_instancia):
        super().__init__(parent)
        self.attributes('-topmost', True)
        self.mundial = mundial_instancia

        self.mundial = mundial_instancia
        self.clasificados_actuales = []  # para llevar el control de la ronda

        self.titulo = ctk.CTkLabel(self, text="TORNEO", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=15)

        # panel de controles
        self.controles = ctk.CTkFrame(self)
        self.controles.pack(pady=10, fill="x", padx=20)

        # boton para fase de grupos
        self.btn_grupos = ctk.CTkButton(
            self.controles,
            text="Simular fase de grupos",
            command=self.simular_fase_grupos)  # falta poner color
        self.btn_grupos.pack(side="left", padx=15, pady=10)

        # boton para la siguiente ronda
        self.btn_siguiente_ronda = ctk.CTkButton(
            self.controles,
            text="Simular siguiente ronda",
            command=self.avanzar_ronda,
            state="disabled") 
        self.btn_siguiente_ronda.pack(side="right", padx=15, pady=10)

        # pantalla de los resultados
        self.scroll_resultados = ctk.CTkScrollableFrame(self, width=750, height=400)
        self.scroll_resultados.pack(padx=20, pady=15, fill="both", expand=True)

    # =================================== Funcion simular fase grupos ==============================
    # Nombre: simular_fase_grupos
    # Entradas: Ninguna.
    # Salidas: Simulación de la fase de grupos del mundial y muestra de los resultados.
    # Restricciones:
    # ==============================================================================================
    def simular_fase_grupos(self):
        if self.mundial == None or self.mundial.grupos == []:
            self.imprimir_en_pantalla("Error: no se ha configurado los grupos del Mundial aún\n")
            return

        self.imprimir_en_pantalla("Iniciando fase de grupos...")
        exito = self.mundial.jugar_fase_grupos()

        if exito == True:

            for grupo in self.mundial.grupos:
                texto_grupo = f"{grupo.nombre_grupo} - POSICIONES FINALES\n"

                for fila in grupo.tabla:
                    # fila[0] = nombre de la seleccion, fila[1] = puntos
                    seleccion_objeto = fila[0]

                    nombre_pais = seleccion_objeto.pais.nombre
                
                    texto_grupo += f" - {nombre_pais} : {fila[1]} Pts\n"

                self.imprimir_en_pantalla(texto_grupo + "\n")

            self.clasificados_actuales = []
            for grupo in self.mundial.grupos:
                self.clasificados_actuales += grupo.obtener_clasificados()

            self.btn_grupos.configure(state="disabled")
            self.btn_siguiente_ronda.configure(state="normal")
            self.imprimir_en_pantalla(
                "Fase de grupos finalizada. Clasificados listos para las eliminatorias\n\n"
            )

    # =================================== Funcion avanzar ronda ====================================
    # Nombre: avanzar_ronda
    # Entradas: Ninguna.
    # Salidas: Simulación de la siguiente ronda del mundial y muestra de los resultados.
    # Restricciones:
    # ==============================================================================================
    def avanzar_ronda(self):

        cantidad_equipos = largoLista(self.clasificados_actuales)

        # si hay uno, ya hay un campeon
        if cantidad_equipos == 1:
            self.mostrar_campeon_destacado(self.clasificados_actuales[0])
            return

        nombre_fase = self.mundial.nombre_final(cantidad_equipos)

        self.imprimir_en_pantalla(f"Simulación de: {nombre_fase}")

        # se arma la fase de eliminatorias
        fase_objeto = self.mundial.armar_fase_eliminatoria(
            nombre_fase, self.clasificados_actuales
        )

        # se juega la fase y se recibe los ganadores
        self.clasificados_actuales = self.mundial.jugar_fase_eliminatoria(fase_objeto)

        textos_partidos = fase_objeto.mostrar_juegos()

        for texto in textos_partidos:
            self.imprimir_en_pantalla(texto + "\n")

        self.imprimir_en_pantalla(
            f"Fin de {nombre_fase}. Avanzan {largoLista(self.clasificados_actuales)} selecciones\n\n"
        )

        if largoLista(self.clasificados_actuales) == 1:
            self.mundial.campeon = self.clasificados_actuales[0]
            self.btn_siguiente_ronda.configure(text="Ver campeón")

    # =================================== Funcion mostrar campeon destacado ========================
    # Nombre: mostrar_campeon_destacado
    # Entradas: campeon_seleccion (objeto de tipo Seleccion).
    # Salidas: Muestra en pantalla al campeón del mundial.
    # Restricciones:
    # ==============================================================================================
    def mostrar_campeon_destacado(self, campeon_seleccion):

        for componenetes in self.scroll_resultados.winfo_children():
            componenetes.destroy()

        self.mundial.generar_reporte()

        tarjeta_oro = ctk.CTkFrame(self.scroll_resultados, fg_color="#d4af37", border_width=3)
        tarjeta_oro.pack(pady=30, padx=20, fill="both", expand=True)

        lbl_copa = ctk.CTkLabel(
            tarjeta_oro,
            text="🏆 ¡HABEMUS CAMPEÓN! 🏆",
            font=("Arial", 24, "bold"),
            text_color="#ffffff")
        lbl_copa.pack(pady=20)

        lbl_campeon = ctk.CTkLabel(
            tarjeta_oro,
            text=f"{campeon_seleccion.pais.nombre.upper()}",
            font=("Arial", 36, "bold"),
            text_color="white")
        lbl_campeon.pack(pady=15)

        lbl_detalles = ctk.CTkLabel(tarjeta_oro, 
            text=f"Ganador oficial de la Copa Mundial FIFA {self.mundial.anio}\nCódigo de equipo: {campeon_seleccion.codigo_equipo}\n\n",
            font=("Arial", 13, "italic"))
        lbl_detalles.pack(pady=15)

        self.btn_siguiente_ronda.configure(state="disabled", text="Torneo concluido")

    # =================================== Funcion imprimir en pantalla =============================
    # Nombre: imprimir_en_pantalla
    # Entradas: texto (string).
    # Salidas: Muestra el texto recibido en la pantalla de resultados del juego.
    # Restricciones:
    # ==============================================================================================
    def imprimir_en_pantalla(self, texto):
        lbl = ctk.CTkLabel(
            self.scroll_resultados,
            text=texto,
            justify="left",
            font=("Courier New", 16),
            anchor="w")
        lbl.pack(fill="x", padx=10, anchor="w")