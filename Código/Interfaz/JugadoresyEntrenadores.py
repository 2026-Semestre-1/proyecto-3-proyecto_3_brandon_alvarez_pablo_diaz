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
import random


class VentanaPlantilla(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Administración de Jugadores y Entrenadores")
        self.geometry("700x500")
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

        scroll = ctk.CTkScrollableFrame(pestana_entrenador)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        # titulo de la sección
        titulo = ctk.CTkLabel(
            scroll,
            text="Registrar Nuevo Entrenador",
            font=("Arial", 18, "bold"),
        )
        titulo.pack(pady=20)

        # campos del formulario

        ctk.CTkLabel(scroll, text="Nombre:").pack(pady=(10, 0))
        self.nombre_entrenador = ctk.CTkEntry(scroll, placeholder_text=" ", width=320)
        self.nombre_entrenador.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Apellido:").pack(pady=(10, 0))
        self.apellido_entrenador = ctk.CTkEntry(scroll, placeholder_text=" ", width=320)
        self.apellido_entrenador.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Fecha de nacimiento en formato DD/MM/AAAA:").pack(
            pady=(10, 0)
        )
        self.fecha_nacimiento_entrenador = ctk.CTkEntry(
            scroll,
            placeholder_text=" ",
            width=320,
        )
        self.fecha_nacimiento_entrenador.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Nacionalidad:").pack(pady=(10, 0))
        self.nacionalidad_entrenador = ctk.CTkEntry(
            scroll,
            placeholder_text=" ",
            width=320,
        )
        self.nacionalidad_entrenador.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Licencia:").pack(pady=(10, 0))
        self.licencia_entrenador = ctk.CTkEntry(
            scroll,
            placeholder_text="Ejemplo: Pro, UEFA A",
            width=320,
        )
        self.licencia_entrenador.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Años de experiencia:").pack(pady=(10, 0))
        self.experiencia_anio_entrenador = ctk.CTkEntry(
            scroll,
            placeholder_text="Ejemplo: 10",
            width=320,
        )
        self.experiencia_anio_entrenador.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Sistema táctico preferido:").pack(pady=(10, 0))
        self.sistema_juego_entrenador = ctk.CTkEntry(
            scroll,
            placeholder_text="Ejemplo: 4-3-3, 4-4-2",
            width=320,
        )
        self.sistema_juego_entrenador.pack(pady=(0, 5))

        btn_guardar = ctk.CTkButton(
            scroll,
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

        try:
            experiencia_anios = int(experiencia_anios)

        except:
            print("Error: La experiencia debe ser un número entero")
            return False

        guardar_entrenador(
            nombre,
            apellido,
            fecha_nacimiento,
            nacionalidad,
            licencia,
            experiencia_anios,
            sistema_juego,
        )
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

    def registro_futbolista(self):

        pestana_futbolista = self.pestanas.tab("Registrar Futbolista")

        scroll = ctk.CTkScrollableFrame(pestana_futbolista)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        # titulo de la sección
        titulo = ctk.CTkLabel(
            scroll,
            text="Registrar Nuevo Futbolista",
            font=("Arial", 18, "bold"),
        )
        titulo.pack(pady=20)

        # campos del formulario
        ctk.CTkLabel(scroll, text="Nombre:").pack(pady=(10, 0))
        self.nombre_futbolista = ctk.CTkEntry(scroll, placeholder_text=" ", width=320)
        self.nombre_futbolista.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Apellido:").pack(pady=(10, 0))
        self.apellido_futbolista = ctk.CTkEntry(scroll, placeholder_text=" ", width=320)
        self.apellido_futbolista.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Fecha de Nacimiento en formato DD/MM/AAAA:").pack(
            pady=(10, 0)
        )
        self.fecha_nacimiento_futbolista = ctk.CTkEntry(
            scroll,
            placeholder_text=" ",
            width=320,
        )
        self.fecha_nacimiento_futbolista.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Nacionalidad:").pack(pady=(10, 0))
        self.nacionalidad_futbolista = ctk.CTkEntry(
            scroll,
            placeholder_text=" ",
            width=320,
        )
        self.nacionalidad_futbolista.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Dorsal:").pack(pady=(10, 0))
        self.dorsal_futbolista = ctk.CTkEntry(
            scroll,
            placeholder_text="Ejemplo: 10, 7, 1",
            width=320,
        )
        self.dorsal_futbolista.pack(pady=(0, 5))

        ctk.CTkLabel(scroll, text="Posición:").pack(pady=(10, 0))
        self.posicion_futbolista = ctk.CTkEntry(
            scroll,
            placeholder_text="Posición del futbolista (ej. Delantero, Medio, Defensa).",
            width=320,
        )
        self.posicion_futbolista.pack(pady=(0, 5))

        # Menu desplegable (ComboBox) que contendrá los países del TXT
        ctk.CTkLabel(scroll, text="Seleccione un equipo de la lista:").pack(
            pady=(10, 0)
        )
        self.combo_codigo_equipo = ctk.CTkComboBox(scroll, values=[], width=300)
        self.combo_codigo_equipo.pack(pady=(0, 5))

        label_estadisticas = ctk.CTkLabel(
            scroll,
            text="Las estadísticas se generarán automáticamente.",
            fg_color="transparent",
        )
        label_estadisticas.pack(pady=20)

        btn_guardar = ctk.CTkButton(
            scroll,
            text="Guardar futbolista",
            command=self.guardar_futbolista,
            fg_color="green",
        )
        btn_guardar.pack(pady=20)

        self.actualizar_combo_selecciones()

    def generar_random(self):

        velocidad = random.randint(1, 25)

        estratega = random.randint(1, 25)

        dominio_balon = random.randint(1, 25)

        fuerza = random.randint(1, 25)

        return velocidad + estratega + dominio_balon + fuerza

    def actualizar_combo_selecciones(self):

        lista_paises = cargar_pais()

        lista_entrenadores = cargar_entrenadores()

        lista_jugadores = cargar_futbolista()

        lista_selecciones = cargar_seleccion(
            lista_paises, lista_entrenadores, lista_jugadores
        )

        nombres = []

        for seleccion in lista_selecciones:

            nombres += [seleccion.codigo_equipo]

        if nombres != []:

            self.combo_codigo_equipo.configure(values=nombres)
            self.combo_codigo_equipo.set(nombres[0])

        else:
            self.combo_codigo_equipo.configure(values=["No hay selecciones"])
            self.combo_codigo_equipo.set("No hay selecciones")

    def guardar_futbolista(self):

        nombre = self.nombre_futbolista.get().strip()

        apellido = self.apellido_futbolista.get().strip()

        fecha_nacimiento = self.fecha_nacimiento_futbolista.get().strip()

        nacionalidad = self.nacionalidad_futbolista.get().strip()

        dorsal = self.dorsal_futbolista.get().strip()

        posicion = self.posicion_futbolista.get().strip()

        codigo_equipo = self.combo_codigo_equipo.get()

        if (
            nombre == ""
            or apellido == ""
            or fecha_nacimiento == ""
            or nacionalidad == ""
            or dorsal == ""
            or posicion == ""
        ):
            print(
                "Error: Todos los campos son obligatorios"
            )  # Reemplazar luego por un modal de alerta
            return False

        try:
            dorsal = int(dorsal)

        except:
            print("Error: El dorsal debe ser un número entero")
            return False

        # Generar estadísticas aleatorias
        total_tarjetas_amarillas = 0
        total_tarjetas_rojas = 0
        goles = 0
        asistencias = 0
        puntaje_individual = self.generar_random()

        guardar_Futbolista(
            nombre,
            apellido,
            fecha_nacimiento,
            nacionalidad,
            dorsal,
            posicion,
            total_tarjetas_amarillas,
            total_tarjetas_rojas,
            goles,
            asistencias,
            puntaje_individual,
            codigo_equipo,
        )

        self.nombre_futbolista.delete(0, "end")
        self.apellido_futbolista.delete(0, "end")
        self.fecha_nacimiento_futbolista.delete(0, "end")
        self.nacionalidad_futbolista.delete(0, "end")
        self.dorsal_futbolista.delete(0, "end")
        self.posicion_futbolista.delete(0, "end")

        self.actualizar_combo_selecciones()

    def pestana_listado(self):
        pass


if __name__ == "__main__":
    app = VentanaPlantilla()
    app.mainloop()
