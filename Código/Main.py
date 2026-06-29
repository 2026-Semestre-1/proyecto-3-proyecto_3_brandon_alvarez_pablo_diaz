# ========================================== Librerias =============================================
import customtkinter as ctk
from Clases.Mundial import Mundial
from Persistencia import *
from Interfaz.ConfiguracionMundial import VentanaConfiguracion
from Interfaz.Estadisticas import VentanaEstadisticas
from Interfaz.JugadoresyEntrenadores import VentanaPlantilla
from Interfaz.JugarMundial import VentanaJugarMundial
from Interfaz.PaisesYSelecciones import VentanaAdministracion

# ==================================================================================================

# ========================================== Variables =============================================
mundial = Mundial("Mundial FIFA 2026", 2026)
# ==================================================================================================


# =================================== Funcion abrir paises =====================================
# Nombre: abrir_paises
# Entradas: Ninguna.
# Salidas: Ventana de administración de países y selecciones.
# Restricciones:
# ==============================================================================================
def abrir_paises():
    VentanaAdministracion()


# =================================== Funcion abrir plantilla ==================================
# Nombre: abrir_plantilla
# Entradas: Ninguna.
# Salidas: Ventana de administración de entrenadores y jugadores.
# Restricciones:
# ==============================================================================================
def abrir_plantilla():
    VentanaPlantilla()


# =================================== Funcion abrir configuracion ==============================
# Nombre: abrir_configuracion
# Entradas: Ninguna.
# Salidas: ventana de configuración del mundial.
# Restricciones:
# ==============================================================================================
def abrir_configuracion():
    VentanaConfiguracion(ventana, mundial)


# =================================== Funcion abrir jugar ======================================
# Nombre: abrir_jugar
# Entradas: Ninguna.
# Salidas: ventana de juego del mundial.
# Restricciones:
# ==============================================================================================
def abrir_jugar():
    VentanaJugarMundial(ventana, mundial)


# =================================== Funcion abrir estadisticas ===============================
# Nombre: abrir_estadisticas
# Entradas: Ninguna.
# Salidas: ventana de estadísticas del mundial.
# Restricciones:
# ==============================================================================================
def abrir_estadisticas():
    VentanaEstadisticas(ventana)


# =================================== Ventana Principal ========================================
# Nombre: ventana principal
# Entradas: Ninguna.
# Salidas: Ventana principal del sistema.
# Restricciones:
# ==============================================================================================
ventana = ctk.CTk()
ventana.title("🏆 Copa Mundial 🏆")
ventana.geometry("700x500")
ventana.resizable(False, False)

# titulo de la sección
titulo = ctk.CTkLabel(
    ventana, text="Bienvenido a la Copa Mundial", font=("Arial", 18, "bold")
)
titulo.pack(pady=20)


# =================================== Botones de la ventana principal ==========================

btn_paises = ctk.CTkButton(
    ventana,
    text="Administrar Países y Selecciones",
    command=abrir_paises,
    fg_color="green",
)
btn_paises.pack(pady=20)

btn_plantilla = ctk.CTkButton(
    ventana,
    text="Administrar Entrenadores y Jugadores",
    command=abrir_plantilla,
    fg_color="green",
)
btn_plantilla.pack(pady=20)

btn_configuracion = ctk.CTkButton(
    ventana,
    text="Configurar Mundial (grupos)",
    command=abrir_configuracion,
    fg_color="green",
)
btn_configuracion.pack(pady=20)

btn_jugar = ctk.CTkButton(
    ventana,
    text="Jugar Mundial",
    command=abrir_jugar,
    fg_color="green",
)
btn_jugar.pack(pady=20)

btn_estadisticas = ctk.CTkButton(
    ventana,
    text="Ver Estadísticas / Rankings",
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

# ==============================================================================================

ventana.mainloop()
