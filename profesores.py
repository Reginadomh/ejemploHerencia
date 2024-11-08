from persona import Persona

class Profesores(Persona):
    def __init__(self):
        super().__init__()
        self._departamento = ""
        self._categoria = ""
        self._maximo_grado_estudios = ""

    # Getters y Setters
    def get_departamento(self):
        return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_maximo_grado_estudios(self):
        return self._maximo_grado_estudios

    def set_maximo_grado_estudios(self, maximo_grado_estudios):
        self._maximo_grado_estudios = maximo_grado_estudios

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}, Categoría: {self._categoria}, Máximo Grado de Estudios: {self._maximo_grado_estudios}"
