from persona import Persona


class Estudiantes(Persona):
    def __init__(self):
        super().__init__()
        self._matricula = ""
        self._carrera = ""

    # Getter y Setter

    def get_carrera(self):
        return self._carrera

    def set_carrera(self, carrera):
        self._carrera = carrera

    def get_matricula(self):
        return self._matricula

    def set_matricula(self, matricula):
        self._matricula = matricula

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Matrícula: {self._matricula}"
