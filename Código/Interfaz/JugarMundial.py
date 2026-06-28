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
        self.btn_grupos = ctk.CTkButton(self.controles, text="Simular fase de grupos", command=self.simular_fase_grupos) #falta poner color
        self.btn_grupos.pack(side="left", padx=15, pady=10)

        #boton para la siguiente ronda
        self.btn_siguiente_ronda = ctk.CTkButton(self.controles, text="Simular siguiente ronda", state="disabled") #falta poner cosas
        self.btn_siguiente_ronda.pack(side="right", padx=15, pady=10)

        #pantalla de los resultados
        self.scroll_resultados = ctk.CTkScrollableFrame(self, width=700, height=400)
        self.scroll_resultados.pack(padx=20, pady=15, fill="both", expand=True)

    def simular_fase_grupos(self):
        if self.mi_mundial == None or self.mi_mundial.grupos == []:
            self.imprimir_en_pantalla("Error: no se ha configurado los grupos del Mundial aún\n")
            return
        
        self.imprimir_en_pantalla("Iniciando fase de grupos...")
        exito = self.mi_mundial.jugar_fase_grupos()

        if exito == True:

            for grupo in self.mi_mundial.grupos:
                texto_grupo = f"{grupo.nombre_grupo} - POSICIONES FINALES\n"

                for fila in grupo.tabla:
                    #fila[0] = nombre de la seleccion, fila[1] = puntos
                    texto_grupo += f" - {fila[0]} : {fila[1]} Pts\n"

                self.imprimir_en_pantalla(texto_grupo + "\n")


            self.clasificados_actuales = []
            for grupo in self.mi_mundial.grupos:
                self.clasificados_actuales += grupo.obtener_clasificados()

            self.btn_grupos.configure(state="disabled")
            self.btn_siguiente_ronda.configure(state="normal")
            self.imprimir_en_pantalla("Fase de grupos finalizada. Clasificados listos para las eliminatorias\n\n")


    




    def imprimir_en_pantalla(self, texto):
        lbl = ctk.CTkLabel(self.scroll_resultados, text=texto, justify="left", font=("Courier New", 13), anchor="w")
        lbl.pack(fill="x", padx=10, anchor="w")


