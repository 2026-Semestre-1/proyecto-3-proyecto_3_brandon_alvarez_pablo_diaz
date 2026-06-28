import customtkinter as ctk
from Clases.Mundial import Mundial
from Persistencia import *
from Interfaz.ConfiguracionMundial import VentanaConfiguracion
from Interfaz.Estadisticas import VentanaEstadisticas
from Interfaz.JugadoresyEntrenadores import VentanaPlantilla
from Interfaz.JugarMundial import VentanaJugarMundial
from Interfaz.PaisesYSelecciones import VentanaAdministracion

# instancia compartida
mundial = Mundial("Mundial FIFA 2026", 2026)

lista_paises = cargar_pais()
lista_entrenadores = cargar_entrenadores()
lista_jugadores = cargar_futbolista()
lista_selecciones = cargar_seleccion(lista_paises, lista_entrenadores, lista_jugadores)

for seleccion in lista_selecciones:
    mundial.registrar_seleccion(seleccion)


def abrir_paises():
    VentanaAdministracion()


def abrir_plantilla():
    VentanaPlantilla()


def abrir_configuracion():
    VentanaConfiguracion(ventana, mundial)


def abrir_jugar():
    VentanaJugarMundial(ventana, mundial)


def abrir_estadisticas():
    VentanaEstadisticas()


ventana = ctk.CTk()
ventana.title("🏆 Copa Mundial 🏆")
ventana.geometry("700x500")
ventana.resizable(False, False)

btn_paises = ctk.CTkButton(
    ventana,
    text="Administrar Países y Selecciones.",
    command=abrir_paises,
    fg_color="green",
)
btn_paises.pack(pady=20)

btn_plantilla = ctk.CTkButton(
    ventana,
    text="Administrar Entrenadores y Jugadores.",
    command=abrir_plantilla,
    fg_color="green",
)
btn_plantilla.pack(pady=20)

btn_configuracion = ctk.CTkButton(
    ventana,
    text="Configurar Mundial (grupos).",
    command=abrir_configuracion,
    fg_color="green",
)
btn_configuracion.pack(pady=20)

btn_jugar = ctk.CTkButton(
    ventana,
    text="Jugar Mundial.",
    command=abrir_jugar,
    fg_color="green",
)
btn_jugar.pack(pady=20)

btn_estadisticas = ctk.CTkButton(
    ventana,
    text="Ver Estadísticas / Rankings.",
    command=abrir_estadisticas,
    fg_color="green",
)
btn_estadisticas.pack(pady=20)

btn_salir = ctk.CTkButton(
    ventana,
    text="Salir del sistema",
    command=ventana.destroy,
    fg_color="green",
)
btn_salir.pack(pady=20)


ventana.mainloop()
