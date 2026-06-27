# ========================================== Librerias =============================================
from Clases.Persona import Persona

# ==================================================================================================


# ======================================= Clase Entrenador =========================================
# Nombre: Entrenador
# Entradas: Clase Persona,  nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios                              y sistema_juego.
# Salidas: nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios y sistema_juego.
# Restricciones:
# ==================================================================================================
class Entrenador(Persona):

    def __init__(
        self,
        nombre,
        apellido,
        fecha_nacimiento,
        nacionalidad,
        licencia,
        experiencia_anios,
        sistema_juego,
    ):
        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)
        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego

    # ================================= Función mostrar datos ==========================================
    # Nombre: mostrar_datos
    # Entradas: ninguna
    # Salidas: Datos de la Clase Persona, Licencia, experiencia en anios(años) y sistema de juego.
    # Restricciones:
    # ==================================================================================================

    def mostrar_datos(self):
        return {
            **super().mostrar_datos(),
            "licencia": self.licencia,
            "experiencia_anios": self.experiencia_anios,
            "sistema_juego": self.sistema_juego,
        }

    # ================================= Función actualizar datos =======================================
    # Nombre: actualizar_datos
    # Entradas: nuevoNombre, nuevoApellido, nuevaFecha_nacimiento, nuevaNacionalidad, nuevaLicencia,                                 nuevaExperiencia_anios y nuevoSistema_juego.
    # Salidas: No retorna nada pero actualiza los datos del entrenador.
    # Restricciones:
    # ==================================================================================================

    def actualizar_datos(
        self,
        nuevoNombre,
        nuevoApellido,
        nuevaFecha_nacimiento,
        nuevaNacionalidad,
        nuevaLicencia,
        nuevaExperiencia_anios,
        nuevoSistema_juego,
    ):

        self.nombre = nuevoNombre
        self.apellido = nuevoApellido
        self.fecha_nacimiento = nuevaFecha_nacimiento
        self.nacionalidad = nuevaNacionalidad
        self.licencia = nuevaLicencia
        self.experiencia_anios = nuevaExperiencia_anios
        self.sistema_juego = nuevoSistema_juego
