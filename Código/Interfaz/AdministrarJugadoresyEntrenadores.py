import os
import sys

# 1. Obtenemos la ruta de la carpeta "Interfaz" donde está este archivo
carpeta_interfaz = os.path.dirname(os.path.abspath(__file__))

# 2. Subimos un nivel para obtener la ruta de la carpeta "Código"
carpeta_codigo = os.path.dirname(carpeta_interfaz)

# 3. Le decimos a Python: "¡Ey! También busque archivos para importar aquí"
sys.path.append(carpeta_codigo)

from Clases.Futbolista import Futbolista
from Clases.Entrenador import Entrenador
from Persistencia import *
import customtkinter as ctk


class VentanaAdministracionJugadoresyEntrenadores(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Administración de Jugadores y Entrenadores")
        self.geometry("700x700")
        self.resizable(False, False)

        # se crea la ventana con pestañas
        self.pestanas = ctk.CTkTabview(self)
        self.pestanas.pack(padx=20, pady=20, fill="both", expand=True)

        self.pestanas.add("Registrar Entrenador")
        self.pestanas.add("Registrar Futbolista")
        self.pestanas.add("Listado de Jugadores")

        # configurar cada pestaña
        self.registro_entrenador()
        self.registro_futbolista()
        self.pestana_listado()

    def registro_entrenador(self):

        pestana_entrenador = self.pestanas.tab("Registrar Entrenador")

        # titulo de la sección
        titulo = ctk.CTkLabel(
            pestana_entrenador,
            text="Registrar Nuevo Entrenador",
            font=("Arial", 18, "bold"),
        )
        titulo.pack(pady=20)

        # campos del formulario
        self.nombre_entrenador = ctk.CTkEntry(
            pestana_entrenador, placeholder_text="Nombre del entrenador", width=320
        )
        self.nombre_entrenador.pack(pady=20)

        self.apellido_entrenador = ctk.CTkEntry(
            pestana_entrenador, placeholder_text="Apellido del entrenador.", width=320
        )
        self.apellido_entrenador.pack(pady=20)

        self.fecha_nacimiento_entrenador = ctk.CTkEntry(
            pestana_entrenador,
            placeholder_text="Fecha de nacimiento del entrenador.",
            width=320,
        )
        self.fecha_nacimiento_entrenador.pack(pady=20)

        self.nacionalidad_entrenador = ctk.CTkEntry(
            pestana_entrenador,
            placeholder_text="Nacionalidad del entrenador.",
            width=320,
        )
        self.nacionalidad_entrenador.pack(pady=20)

        self.licencia_entrenador = ctk.CTkEntry(
            pestana_entrenador,
            placeholder_text="Tipo de licencia de entrenador (ej. Pro, UEFA A)",
            width=320,
        )
        self.licencia_entrenador.pack(pady=20)

        self.experiencia_anio_entrenador = ctk.CTkEntry(
            pestana_entrenador,
            placeholder_text="Experencia en años del entrenador.",
            width=320,
        )
        self.experiencia_anio_entrenador.pack(pady=20)

        self.sistema_juego_entrenador = ctk.CTkEntry(
            pestana_entrenador,
            placeholder_text="Sistema táctico preferido (ej. 4-3-3, 4-4-2).",
            width=320,
        )
        self.sistema_juego_entrenador.pack(pady=20)

        btn_guardar = ctk.CTkButton(
            pestana_entrenador,
            text="Guardar Entrenador",
            command=self.guardar_entrenador,
            fg_color="green",
        )
        btn_guardar.pack(pady=20)

    def guardar_entrenador(self):

        nombre = self.nombre_entrenador.get().strip()

        apellido = self.apellido_entrenador.get().strip()

        fecha_nacimiento = self.fecha_nacimiento_entrenador.get().strip()

        nacionalidad = self.nacionalidad_entrenador.get().strip()

        licencia = self.licencia_entrenador.get().strip()

        experiencia_anios = self.experiencia_anio_entrenador.get().strip()

        sistema_juego = self.sistema_juego_entrenador.get().strip()

        if (
            nombre == ""
            or apellido == ""
            or fecha_nacimiento == ""
            or nacionalidad == ""
            or licencia == ""
            or experiencia_anios == ""
            or sistema_juego == ""
        ):
            print(
                "Error: Todos los campos son obligatorios"
            )  # Reemplazar luego por un modal de alerta
            return False

        # Lógica para guardar el entrenador (puede ser una llamada a una función de base de datos)
        print(
            f"Éxito: {nombre} {apellido} guardado correctamente"
        )  # cambiar esto, solo es por probar

        # se borra las entradas para el siguiente registro
        self.nombre_entrenador.delete(0, "end")

        self.apellido_entrenador.delete(0, "end")

        self.fecha_nacimiento_entrenador.delete(0, "end")

        self.nacionalidad_entrenador.delete(0, "end")

        self.licencia_entrenador.delete(0, "end")

        self.experiencia_anio_entrenador.delete(0, "end")

        self.sistema_juego_entrenador.delete(0, "end")

        # refrescar los componentes que dependen de los entrenadores
        self.actualizar_combo_entrenadores()

    def actualizar_combo_entrenadores(self):
        # Se jala los entrenadores
        lista_entrenadores = cargar_entrenadores()

        nombres_entrenadores = []
        for entrenador in lista_entrenadores:
            # Creamos un string descriptivo para mostrar en el menú
            nombres_entrenadores += [f"{entrenador.nombre} {entrenador.apellido}"]

        # Actualizamos las opciones del componente gráfico
        if nombres_entrenadores != []:
            self.combo_entrenadores.configure(values=nombres_entrenadores)
            self.combo_entrenadores.set(nombres_entrenadores[0])

        else:
            self.combo_entrenadores.configure(
                values=["No hay entrenadores registrados"]
            )
            self.combo_entrenadores.set("No hay entrenadores registrados")
