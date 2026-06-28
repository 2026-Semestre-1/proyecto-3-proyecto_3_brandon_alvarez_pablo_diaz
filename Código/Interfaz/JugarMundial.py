import os
import sys

carpeta_interfaz = os.path.dirname(os.path.abspath(__file__))
carpeta_codigo = os.path.dirname(carpeta_interfaz)
if carpeta_codigo not in sys.path:
    sys.path.append(carpeta_codigo)


import customtkinter as ctk
from Persistencia import *
from Clases.Mundial import Mundial

class VentanaJugarMundial(ctk.CTkFrame):

    def __init__(self, parent, mundial_instancia=False):
        super().__init__(parent)

        self.mundial = mundial_instancia
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
        self.btn_siguiente_ronda = ctk.CTkButton(self.controles, text="Simular siguiente ronda", command=self.avanzar_ronda, state="disabled") #falta poner cosas
        self.btn_siguiente_ronda.pack(side="right", padx=15, pady=10)

        #pantalla de los resultados
        self.scroll_resultados = ctk.CTkScrollableFrame(self, width=700, height=400)
        self.scroll_resultados.pack(padx=20, pady=15, fill="both", expand=True)

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
                    #fila[0] = nombre de la seleccion, fila[1] = puntos
                    texto_grupo += f" - {fila[0]} : {fila[1]} Pts\n"

                self.imprimir_en_pantalla(texto_grupo + "\n")


            self.clasificados_actuales = []
            for grupo in self.mundial.grupos:
                self.clasificados_actuales += grupo.obtener_clasificados()

            self.btn_grupos.configure(state="disabled")
            self.btn_siguiente_ronda.configure(state="normal")
            self.imprimir_en_pantalla("Fase de grupos finalizada. Clasificados listos para las eliminatorias\n\n")

    def avanzar_ronda(self):

        cantidad_equipos = largoLista(self.clasificados_actuales)

        #si hay uno, ya hay un campeon
        if cantidad_equipos == 1:
            self.mostrar_campeon_destacado(self.clasificados_actuales[0])
        
        nombre_fase = self.mundial.nombre_final(cantidad_equipos)

        self.imprimir_en_pantalla(f"Simulación de: {nombre_fase}")

        #se arma la fase de eliminatorias
        fase_objeto = self.mundial.armar_fase_eliminatoria(nombre_fase, self.clasificados_actuales)

        #se juega la fase y se recibe los ganadores
        self.clasificados_actuales = self.mundial.jugar_fase_eliminatoria(fase_objeto)

        textos_partidos = fase_objeto.mostrar_juegos()

        for texto in textos_partidos:
            self.imprimir_en_pantalla(texto + "\n")

        self.imprimir_en_pantalla(f"Fin de {nombre_fase}. Avanzan {largoLista(self.clasificados_actuales)} selecciones\n\n")

        if largoLista(self.clasificados_actuales) == 1:
            self.mundial.campeon = self.clasificados_actuales[0]
            self.btn_siguiente_ronda.configure(text="Ver campeón")

    def mostrar_campeon_destacado(self, campeon_seleccion):

        for componenetes in self.scroll_resultados.winfo_children():
            componenetes.destroy()

        self.mundial.generar_reporte()

        tarjeta_oro = ctk.CTkFrame(self.scroll_resultados, fg_color="#d4af37", border_width=3)
        tarjeta_oro.pack(pady=30, padx=20, fill="both", expand=True)

        lbl_copa = ctk.CTkLabel(tarjeta_oro, text="🏆 ¡HABEMUS CAMPEÓN! 🏆", font=("Arial", 24, "bold"), text_color="#d4af37")
        lbl_copa.pack(pady=20)

        lbl_campeon = ctk.CTkLabel(tarjeta_oro, text=f"{campeon_seleccion.pais.nombre.upper()}", font=("Arial", 36, "bold"), text_color="white")
        lbl_campeon.pack(pady=15)

        self.btn_siguiente_ronda.configure(state="disabled", text="Torneo concluido")


    def imprimir_en_pantalla(self, texto):
        lbl = ctk.CTkLabel(self.scroll_resultados, text=texto, justify="left", font=("Courier New", 13), anchor="w")
        lbl.pack(fill="x", padx=10, anchor="w")


if __name__ == "__main__":
    from Clases.Pais import Pais
    from Clases.Seleccion import Seleccion

    # 1. Inicializamos entorno básico de prueba
    app = ctk.CTk()
    app.title("Prueba de Campo - Jugar Mundial")
    app.geometry("780x580")

    # 2. Creamos datos falsos simulando que vienen de la persistencia
    mundial_test = Mundial("Mundial de Prueba", 2026)
    
    p1 = Pais("CRC", "Costa Rica", "América", 30)
    p2 = Pais("GER", "Alemania", "Europa", 10)
    p3 = Pais("BRA", "Brasil", "América", 5)
    p4 = Pais("JPN", "Japón", "Asia", 15)

    s1 = Seleccion("SEL-CRC", p1)
    s2 = Seleccion("SEL-GER", p2)
    s3 = Seleccion("SEL-BRA", p3)
    s4 = Seleccion("SEL-JPN", p4)

    mundial_test.registrar_seleccion(s1)
    mundial_test.registrar_seleccion(s2)
    mundial_test.registrar_seleccion(s3)
    mundial_test.registrar_seleccion(s4)

    # Ejecutamos el creador de grupos oficial para poblar el backend
    mundial_test.crear_grupos(2)

    # 3. Cargamos tu componente pasándole el mundial ya configurado
    contenedor_juego = VentanaJugarMundial(app, mundial_instancia=mundial_test)
    contenedor_juego.pack(fill="both", expand=True, padx=10, pady=10)

    app.mainloop()