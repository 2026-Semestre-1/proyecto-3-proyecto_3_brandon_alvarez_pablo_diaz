# ========================================== Librerias =============================================
import customtkinter as ctk
from Persistencia import *
# ==================================================================================================

# ========================================= Clase Ventana Configuracion ============================
# Nombre: VentanaConfiguracion
# Entradas: ninguna.
# Salidas: Ventana de configuración de grupos del mundial. 
# Restricciones:
# ==================================================================================================
class VentanaConfiguracion(ctk.CTkToplevel):
    def __init__(self, parent, mundial_instancia):
        super().__init__(parent)
        self.attributes('-topmost', True)
        self.mundial = mundial_instancia

        self.titulo = ctk.CTkLabel(
            self, text="Configurar Grupos del Torneo", font=("Arial", 20, "bold")
        )
        self.titulo.pack(pady=15)

        self.controles = ctk.CTkFrame(self)
        self.controles.pack(pady=10, fill="x", padx=20)

        self.lbl_controles = ctk.CTkLabel(
            self.controles, text="Cantidad de Grupo (Mínimo 2)", font=("Arial", 13)
        )
        self.lbl_controles.pack(side="left", padx=15, pady=10)

        self.cantidad_grupos = ctk.CTkEntry(
            self.controles, placeholder_text="Ej: 4", width=100
        )
        self.cantidad_grupos.pack(side="left", padx=10, pady=10)

        self.btn_generar = ctk.CTkButton(
            self.controles, text="Distribuir equipos", command=self.generar_grupos
        )  # luego se pone bello
        self.btn_generar.pack(side="right", padx=15, pady=10)

        self.scroll_grupos = ctk.CTkScrollableFrame(self, width=700, height=350)
        self.scroll_grupos.pack(padx=20, pady=15, fill="both", expand=True)

    # =================================== Funcion generar grupos ===================================
    # Nombre: generar_grupos
    # Entradas: Ninguna.
    # Salidas: Distribución de selecciones en grupos según la cantidad ingresada.
    # Restricciones:
    # ==============================================================================================
    def generar_grupos(self):
        entrada = self.cantidad_grupos.get().strip()

        if entrada == "":
            print("Error: Ingrese un número")  # esto se cambia
            return

        try:
            cantidad_grupos = int(entrada)
        except ValueError:
            print("Error: Ingrese un número válido")
            return

        if cantidad_grupos < 2:
            print("Error: cantidad mínima es de 2")  # esto se cambia
            return

        lista_paises = cargar_pais()
        lista_selecciones = cargar_seleccion(lista_paises, [], [])

        if largoLista(lista_selecciones) < 8:
            print(f"Error: Se requieren al menos 8 selecciones registradas para jugar el Mundial. "
                    f"Actuales: {largoLista(lista_selecciones)}")
            return

        if (largoLista(lista_selecciones) // cantidad_grupos):
            print(f"Error: Distribución inválida. Con {largoLista(lista_selecciones)} selecciones y "
                  f"{cantidad_grupos} grupos, quedarían menos de 4 equipos por grupo.\n"
                  f"¡Reduzca la cantidad de grupos o registre más selecciones!")
            return

        self.mundial.selecciones = []

        for seleccion in lista_selecciones:
            self.mundial.registrar_seleccion(seleccion)

        creado = self.mundial.crear_grupos(cantidad_grupos)

        if creado == True:
            self.mostrar_grupos(self.mundial.grupos)
        else:
            print("Error: no se pudieron crear los grupos")

    # =================================== Funcion mostrar grupos ===================================
    # Nombre: mostrar_grupos
    # Entradas: Ninguna.
    # Salidas: Muestra los grupos generados en la ventana de configuración.
    # Restricciones:
    # ==============================================================================================
    def mostrar_grupos(self, lista_grupos):

        for componentes in self.scroll_grupos.winfo_children():
            componentes.destroy()

        for grupo in lista_grupos:

            tarjeta = ctk.CTkFrame(self.scroll_grupos)
            tarjeta.pack(pady=8, fill="x", padx=10)

            lbl_grupo = ctk.CTkLabel(tarjeta, text=str(grupo.nombre_grupo), font=("Arial", 20, "bold"))  # hay que cambiar cosas aqui
            lbl_grupo.pack(anchor="w", padx=15, pady=6)

            texto_equipos = ""

            for seleccion in grupo.equipos:
                texto_equipos += f"{seleccion.pais.nombre} ({seleccion.codigo_equipo})\n"

            if texto_equipos == "":
                texto_equipos = "Sin selecciones asignadas\n"

            lbl_equipo = ctk.CTkLabel(tarjeta, text=texto_equipos, justify="left", font=("Arial", 20))
            lbl_equipo.pack(anchor="w", padx=20, pady=4)
