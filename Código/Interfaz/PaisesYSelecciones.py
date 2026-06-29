# ========================================== Librerias =============================================
import tkinter as tk
from Clases.Seleccion import Seleccion
import customtkinter as ctk
from Persistencia import *
from Utilidades import *
# ==================================================================================================

# ========================================= Clase Administracion ===================================
# Nombre: VentanaAdministracion
# Entradas: ninguna.
# Salidas: Ventana de administración de países y selecciones.
# Restricciones:
# ==================================================================================================
class VentanaAdministracion(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("Administración de Países y Selecciones")
        self.geometry("700x500")
        self.resizable(False, False)
        self.attributes('-topmost', True)

        # se crea la ventana con pestañas
        self.pestanas = ctk.CTkTabview(self)
        self.pestanas.pack(padx=20, pady=20, fill="both", expand=True)

        self.pestanas.add("Registrar País")
        self.pestanas.add("Registrar Selección")
        self.pestanas.add("Listado de Registros")

        # configurar cada pestaña
        self.registro_pais()
        self.registro_seleccion()
        self.pestana_listado()

    # =================================== Funcion registro pais ====================================
    # Nombre: registro_pais
    # Entradas: Ninguna.
    # Salidas: Formulario para registrar un país en el sistema.
    # Restricciones:
    # ==============================================================================================
    def registro_pais(self):

        pestana = self.pestanas.tab("Registrar País")

        # titulo de la sección
        titulo = ctk.CTkLabel(pestana, text="Registrar Nuevo País", font=("Arial", 18, "bold"))
        titulo.pack(pady=20)

        # campos del formulario
        self.codigo_fifa = ctk.CTkEntry(pestana, placeholder_text="Codigo FIFA (Ej. CRC)", width=320)
        self.codigo_fifa.pack(pady=20)

        self.nombre_pais = ctk.CTkEntry(pestana, placeholder_text="Nombre del país", width=320)
        self.nombre_pais.pack(pady=20)

        self.continente_pais = ctk.CTkEntry(pestana, placeholder_text="Continente del país", width=320)
        self.continente_pais.pack(pady=20)

        self.ranking_fifa = ctk.CTkEntry(pestana, placeholder_text="Ranking FIFA (Número)", width=320)
        self.ranking_fifa.pack(pady=20)

        btn_guardar = ctk.CTkButton(pestana, text="Guardar país", command=self.guardar_pais, fg_color="green")
        btn_guardar.pack(pady=20)

    # =================================== Funcion guardar pais =====================================
    # Nombre: guardar_pais
    # Entradas: Ninguna.
    # Salidas: Guarda un país en el sistema y actualiza los componentes dependientes.
    # Restricciones:
    # ==============================================================================================
    def guardar_pais(self):
        codigo_fifa = self.codigo_fifa.get().strip()
        nombre_pais = self.nombre_pais.get().strip()
        continente = self.continente_pais.get().strip()
        ranking_fifa = self.ranking_fifa.get().strip()

        if (codigo_fifa == "" or nombre_pais == "" or continente == "" or ranking_fifa == ""):
            tk.messagebox.showerror("Datos inválidos", "Error: Todos los campos son obligatorios")
            return
        
        if not (isinstance(codigo_fifa, str) or isinstance(nombre_pais, str) or isinstance(continente, str)):
            tk.messagebox.showerror("Datos Inválidos", "Error: El nombre y el continente deben ser texto válido")
            return
        
        if largoLista(codigo_fifa) != 3:
            tk.messagebox.showerror("Código Inválido", "Error: El código FIFA debe tener exactamente 3 caracteres (ej: CRC)")
            return
        
        try:
            ranking_fifa_entero = int(ranking_fifa)
            if ranking_fifa_entero < 0:
                tk.messagebox.showerror("Ranking Erróneo", "Error: El ranking FIFA debe ser un número positivo mayor a 0")
                return
        except Exception:
            tk.messagebox.showerror("Tipo de Dato Erróneo", "Error: El ranking debe ser un número entero válido (sin letras ni puntos)")
            return
        
        try:
            int(nombre_pais)
            # Si llega a esta linea, es porque el nombre era un número puro
            tk.messagebox.showerror("Nombre Inválido", "Error: El nombre del país no puede ser un número numérico")
            return
        except Exception:
            # Si explota el int(), significa que sí es un texto con letras
            pass

        try:
            int(continente)
            tk.messagebox.showerror("Continente Inválido", "Error: El continente no puede ser un número numérico")
            return
        except Exception:
            pass

        guardar_pais(codigo_fifa, nombre_pais, continente, int(ranking_fifa))
        tk.messagebox.showinfo("Notificación", f"Éxito: {nombre_pais} guardado correctamente")  

        # se borra las entradas para el siguiente registro
        self.codigo_fifa.delete(0, "end")
        self.nombre_pais.delete(0, "end")
        self.continente_pais.delete(0, "end")
        self.ranking_fifa.delete(0, "end")

        # refrescar los componentes que dependen de los paises
        self.actualizar_combo_paises()

    # =================================== Funcion registro seleccion ===============================
    # Nombre: registro_seleccion
    # Entradas: Ninguna.
    # Salidas: Formulario para registrar una selección asociada a un país en el sistema.
    # Restricciones:
    # ==============================================================================================
    def registro_seleccion(self):
        pestana = self.pestanas.tab("Registrar Selección")

        titulo = ctk.CTkLabel(pestana, text="Asociar Selección a un País", font=("Arial", 18, "bold"))
        titulo.pack(pady=15)

        # menu desplegable que contendrá los países del txf
        ctk.CTkLabel(pestana, text="Seleccione un país de la lista:").pack(pady=2)
        self.combo_paises = ctk.CTkComboBox(pestana, values=[], width=300)
        self.combo_paises.pack(pady=10)

        ctk.CTkLabel(pestana, text="Digite el código de la selección:").pack(pady=2)
        self.codigo_equipo = ctk.CTkEntry(pestana, placeholder_text="Ej: SEL-CRC", width=320)
        self.codigo_equipo.pack(pady=10)

        # Rellenar el combo con los países que ya existen en el .txt
        self.actualizar_combo_paises()

        btn_crear = ctk.CTkButton(pestana, text="Hacer Selección", command=self.crear_seleccion)
        btn_crear.pack(pady=20)

    # =================================== Funcion actualizar combo paises ==========================
    # Nombre: actualizar_combo_paises
    # Entradas: Ninguna.
    # Salidas: Actualiza el menú desplegable de países con los registros existentes en el sistema.
    # Restricciones:
    # ==============================================================================================
    def actualizar_combo_paises(self):
        # Se jala los países
        lista_paises = cargar_pais()

        nombres_paises = []
        for pais in lista_paises:
            # Creamos un string descriptivo para mostrar en el menú
            nombres_paises += [pais.nombre]

        # Actualizamos las opciones del componente gráfico
        if nombres_paises != []:
            self.combo_paises.configure(values=nombres_paises)
            self.combo_paises.set(nombres_paises[0])
        else:
            self.combo_paises.configure(values=["No hay países registrados"])
            self.combo_paises.set("No hay países registrados")

    # =================================== Funcion crear seleccion ==================================
    # Nombre: crear_seleccion
    # Entradas: Ninguna.
    # Salidas: Crea una nueva selección asociada a un país en el sistema.
    # Restricciones:
    # ==============================================================================================
    def crear_seleccion(self):

        nombre_pais = self.combo_paises.get()
        codigo_equipo = self.codigo_equipo.get().strip()

        if nombre_pais == "No hay países registrados" or codigo_equipo == "":
            tk.messagebox.showerror("Datos faltantes", "Error: Debe seleccionar un país y asignar un código de equipo")
            return

        print(nombre_pais)
        print(codigo_equipo)

        # se jala los países
        lista_paises = cargar_pais()
        pais_encontrado = None

        for pais in lista_paises:
            if pais.nombre == nombre_pais:
                pais_encontrado = pais
                break

        if pais_encontrado != None:
            
            lista_selecciones = cargar_seleccion(lista_paises, [], [])

            for seleccion in lista_selecciones:
                if seleccion.pais.nombre == nombre_pais:
                    tk.messagebox.showerror("País Duplicado", f"Error: {nombre_pais} ya está registrado como una Selección Oficial\n"
                        f"Cada país solo puede tener una única selección en el torneo")
                    return

            nueva_seleccion = Seleccion(codigo_equipo, pais_encontrado)

            guardar_seleccion(nueva_seleccion)

            tk.messagebox.showinfo("Dato ingresado", f"Éxito: {nueva_seleccion.pais.nombre} ahora es una Selección Oficial")

            self.codigo_equipo.delete(0, "end")

    # =================================== Funcion pestana listado ==================================
    # Nombre: pestana_listado
    # Entradas: Ninguna.
    # Salidas: Pestaña de listado de países registrados en el sistema.
    # Restricciones:
    # ==============================================================================================
    def pestana_listado(self):

        pestana = self.pestanas.tab("Listado de Registros")

        titulo = ctk.CTkLabel(
            pestana, text="Países Registrados", font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.scroll_lista = ctk.CTkScrollableFrame(pestana, width=60, height=100)
        self.scroll_lista.pack(pady=10, fill="both", expand=True)

        btn_actualizar = ctk.CTkButton(
            pestana, text="Actualizar lista", command=self.cargar_paises_lista
        )
        btn_actualizar.pack(pady=10)

        self.cargar_paises_lista()

    # =================================== Funcion cargar lista de paises ===========================
    # Nombre: cargar_paises_lista
    # Entradas: Ninguna.
    # Salidas: Lista de países registrados en el sistema.
    # Restricciones:
    # ==============================================================================================
    def cargar_paises_lista(self):

        for componentes in self.scroll_lista.winfo_children():
            componentes.destroy()

        lista_paises = cargar_pais()

        for pais in lista_paises:

            fila = ctk.CTkFrame(self.scroll_lista)
            fila.pack(pady=5, fill="x", padx=5)

            informacion = f"{pais.codigo_fifa} | {pais.nombre} | {pais.continente} | {pais.ranking_fifa}"
            lbl_informacion = ctk.CTkLabel(fila, text=informacion, font=("Arial", 14))
            lbl_informacion.pack(side="left", padx=10, pady=10)

            btn_editar = ctk.CTkButton(fila,text="Editar",width=80, command=lambda pais_objeto=pais: self.ventana_edicion(pais_objeto))
            btn_editar.pack(side="right", padx=10, pady=10)

    # =================================== Funcion ventana de edicion ===============================
    # Nombre: ventana_edicion
    # Entradas: Ninguna.
    # Salidas: Ventana para editar los datos de un país registrado en el sistema.
    # Restricciones:
    # ==============================================================================================
    def ventana_edicion(self, pais_buscado):

        ventana_editar = ctk.CTkToplevel(self)
        ventana_editar.attributes('-topmost', True)
        ventana_editar.title(f"Modificar: {pais_buscado.nombre}")
        ventana_editar.geometry("400x400")
        ventana_editar.grab_set()  # bloquea la principal hasta que esta se cierre

        ctk.CTkLabel(ventana_editar,text=f"Editando: {pais_buscado.codigo_fifa}",font=("Arial", 16, "bold"),).pack(pady=15)

        nuevo_nombre = ctk.CTkEntry(ventana_editar, width=250)
        nuevo_nombre.insert(0, pais_buscado.nombre)
        nuevo_nombre.pack(pady=10)

        nuevo_continente = ctk.CTkEntry(ventana_editar, width=250)
        nuevo_continente.insert(0, pais_buscado.continente)
        nuevo_continente.pack(pady=10)

        nuevo_ranking = ctk.CTkEntry(ventana_editar, width=250)
        nuevo_ranking.insert(0, str(pais_buscado.ranking_fifa))
        nuevo_ranking.pack(pady=10)

        def guardar_cambios():

            nuevo_nombre_obtenido = nuevo_nombre.get().strip()
            nuevo_continente_obtenido = nuevo_continente.get().strip()
            nuevo_ranking_obtenido = nuevo_ranking.get().strip()

            if nuevo_nombre_obtenido == "" or nuevo_continente_obtenido or nuevo_ranking_obtenido == "":
                tk.messagebox.showerror("Campos Vacíos", "Error: Todos los campos son obligatorios para modificar el país")
                return
            
            if not (isinstance(nuevo_nombre_obtenido, str) and isinstance(nuevo_continente_obtenido, str)):
                tk.messagebox.showerror("Datos Inválidos", "Error: El nombre y el continente deben ser texto válido")
                return
            
            try:
                ranking_entero = int(nuevo_ranking_obtenido)
                if ranking_entero <= 0:
                    tk.messagebox.showerror("Ranking Erróneo", "Error: El ranking FIFA debe ser un número positivo mayor a 0")
                    return
            except Exception:
                tk.messagebox.showerror("Tipo de Dato Erróneo", "Error: El ranking debe ser un número entero válido (sin letras ni puntos)")
                return
            
            try:
                int(nuevo_nombre_obtenido)
                # Si llega a esta línea, es porque el nombre era un número puro
                tk.messagebox.showerror("Nombre Inválido", "Error: El nombre del país no puede ser un número numérico")
                return
            except Exception:
                # Si explota el int(), significa que sí es un texto con letras
                pass

            try:
                int(nuevo_continente_obtenido)
                tk.messagebox.showerror("Continente Inválido", "Error: El continente no puede ser un número numérico")
                return
            except Exception:
                pass

            lista_paises = cargar_pais()
            pais_modificado = None

            for pais in lista_paises:
                if pais.codigo_fifa == pais_buscado.codigo_fifa:
                    pais.nombre = nuevo_nombre_obtenido
                    pais.continente = nuevo_continente_obtenido
                    pais.ranking_fifa = nuevo_ranking_obtenido
                    pais_modificado = pais
                    break


            if pais_buscado != None:
                modificar_pais(lista_paises, pais_modificado.codigo_fifa, pais_modificado.nombre, pais_buscado.continente, pais_modificado.ranking_fifa)
                tk.messagebox.showinfo("Cambios Guardados", f"Éxito: Los datos de {pais_modificado.nombre} han sido actualizados")

            self.cargar_paises_lista()
            self.actualizar_combo_paises()
            ventana_editar.destroy()

        btn_confirmar = ctk.CTkButton(ventana_editar, text="Guardar cambios", command=guardar_cambios)
        btn_confirmar.pack(pady=20)