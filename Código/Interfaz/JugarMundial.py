import customtkinter as ctk
from Persistencia import *
from Clases.Mundial import Mundial

class VentanaJugarMundial(ctk.CtkFrame):

    def __init__(self, parent, mundial_instancia=False):
        super().__init__(parent)

        self.mi_mundial = mundial_instancia
        self.clasificados_actuales = [] #para llevar el control de la ronda

        self.titulo = ctk.CTkLabel(self, text="TORNEO", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=15)

        #panel de controles
        self.controles = ctk.CTkFrame(self)
        self.controles.pack(pady=10, fill="x", padx=20)

        #boton para fase de grupos
        self.btn_grupos = ctk.CTkButton(self.controles, text="Simular fase de grupos") #falta poner cosas
        self.btn_grupos.pack(side="left", padx=15, pady=10)

        #boton para la siguiente ronda
        self.btn_siguiente_ronda = ctk.CTkButton(self.controles, text="Simular siguiente ronda", state="disabled") #falta poner cosas
        self.btn_siguiente_ronda.pack(side="right", padx=15, pady=10)

        #pantalla de los resultados
        self.scroll_resultados = ctk.CTkScrollableFrame(self, width=700, height=400)
        self.scroll_resultados.pack(padx=20, pady=15, fill="both", expand=True)

        