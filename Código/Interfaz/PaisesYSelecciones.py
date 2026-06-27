import customtkinter as ctk
from Persistencia import cargar_pais, guardar_pais

class VentanaAdministracion(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Administración de Países y Selecciones")
        self.geometry("700x500")
        self.resizable(False, False)

        #se crea la ventana con pestañas
        self.pestanas = ctk.CTkTabview(self)
        self.pestanas.pack(padx=20, pady=20, fill="both", expand=True)

        self.pestanas.add("Registrar País")
        self.pestanas.add("Registrar Selección")
        self.pestanas.add("Listado de Registros")

        #configurar cada pestaña
        self.registro_pais()

    def registro_pais(self):

        pestana = self.pestanas.tab("Registrar País")

        #titulo de la sección
        titulo = ctk.CTkLabel(pestana, text="Registrar Nuevo País", font=("Arial", 18, "bold"))
        titulo.pack(pady=20)

        #campos del formulario
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
    
    def guardar_pais(self):
        codigo_fifa = self.codigo_fifa.get().strip()
        nombre_pais = self.nombre_pais.get().strip()
        continente = self.continente_pais.get().strip()
        ranking_fifa = self.ranking_fifa.get().strip()

        print(f"DEBUG INTERFAZ -> Código: '{codigo_fifa}', Nombre: '{nombre_pais}', Continente: '{continente}', Rank: '{ranking_fifa}'")

        if codigo_fifa == "" or nombre_pais == "" or continente == "" or ranking_fifa == "":
            print("Error: Todos los campos son obligatorios") # Reemplazar luego por un modal de alerta
            return
        
        guardar_pais(codigo_fifa, nombre_pais, continente, int(ranking_fifa))
        print(f"Éxito: {nombre_pais} guardado correctamente") #cambiar esto, solo es por probar
        
        #se borra las entradas para el siguiente registro
        self.codigo_fifa.delete(0, "end")
        self.nombre_pais.delete(0, "end")
        self.continente_pais.delete(0, "end")
        self.ranking_fifa.delete(0, "end")
        

if __name__ == "__main__":
    app = VentanaAdministracion()
    app.mainloop()