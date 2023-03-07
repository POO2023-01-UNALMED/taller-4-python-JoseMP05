from classroom.asignatura import Asignatura


class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas is None:
            self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if self.listadoAlumnos is None:
            self.listadoAlumnos = []
        if lista is not None:
            lista.append(alumno)
            for item in lista:
                self.listadoAlumnos.append(item)
        else:
            self.listadoAlumnos.append(alumno)

    def __str__(self):
        cadena = "Grupo de estudiantes" + ': ' + self._grupo
        return cadena

    @ staticmethod
    def asignarNombre(cls, nombre="Grado 12"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
