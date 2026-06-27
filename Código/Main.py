from tkinter import *
from Clases.Entrenador import Entrenador
from Clases.Fase import Fase
from Clases.Futbolista import Futbolista
from Clases.Grupo import Grupo
from Clases.Mundial import Mundial
from Clases.Pais import Pais
from Clases.Partido import Partido
from Clases.Seleccion import Seleccion
from Utilidades import largoLista
from Persistencia import *
from tkinter import simpledialog, messagebox
from tkinter import ttk

lista_paises = []
lista_selecciones = []
lista_jugadores = []

# =================================== Ventana Principal ============================================
ventana = Tk()
ventana.title("Copa Mundial FIFA 2026")

# Definir tamaño
ventana.geometry("800x550")
ventana.resizable(False, False)
ventana.update_idletasks()

# Colocar fondo
fondo_label = Label(ventana, bg="#2d2d2d")
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Estilo de los botones
style = ttk.Style()
style.theme_use("clam")  # permite personalización de colores

# Estilo general para todos los botones del menú
style.configure(
    "Menu.TButton",
    font=("Verdana", 8, "bold"),
    background="#5D648C",
    foreground="white",
    padding=8,
    borderwidth=0,
)

# Efectos de hover y click
style.map(
    "Menu.TButton", background=[("active", "#433859")], foreground=[("active", "white")]
)

# ============================ Botones de la ventana Principal =====================================

# Posición X fija para centrar horizontalmente
pos_x = 250

# -------- Fila 1 --------
Button_paises = ttk.Button(
    ventana,
    text="Administrar Países y Selecciones",
    command="",
    style="Menu.TButton",
)
Button_paises.place(x=pos_x, y=87, width=325, height=50)
Button_paises.configure(cursor="hand2")

# -------- Fila 2 --------
Button_jugadores = ttk.Button(
    ventana,
    text="Administrar Entrenadores y Jugadores",
    command="",
    style="Menu.TButton",
)
Button_jugadores.place(x=pos_x, y=152, width=325, height=50)
Button_jugadores.configure(cursor="hand2")

# -------- Fila 3 --------
Button_configurar = ttk.Button(
    ventana,
    text="Configurar Mundial",
    command="",
    style="Menu.TButton",
)
Button_configurar.place(x=pos_x, y=217, width=325, height=50)
Button_configurar.configure(cursor="hand2")

# -------- Fila 4 --------
Button_jugar = ttk.Button(
    ventana,
    text="Jugar Mundial",
    command="",
    style="Menu.TButton",
)
Button_jugar.place(x=pos_x, y=282, width=325, height=50)
Button_jugar.configure(cursor="hand2")

# -------- Fila 5 --------
Button_estadisticas = ttk.Button(
    ventana,
    text="Ver Estadísticas / Rankings",
    command="",
    style="Menu.TButton",
)
Button_estadisticas.place(x=pos_x, y=347, width=325, height=50)
Button_estadisticas.configure(cursor="hand2")

# -------- Fila 6 --------
Button_salir = ttk.Button(
    ventana,
    text="Salir del sistema",
    command=ventana.destroy,  # Cierra la ventana
    style="Menu.TButton",
)
Button_salir.place(x=pos_x, y=412, width=325, height=50)
Button_salir.configure(cursor="hand2")

ventana.mainloop()
# ==================================================================================================