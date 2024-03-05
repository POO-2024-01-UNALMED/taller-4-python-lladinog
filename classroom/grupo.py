from classroom.asignatura import Asignatura
class Grupo:
    grado = "Grado 6"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], listadoAlumnos=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = listadoAlumnos if listadoAlumnos is not None else []

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    def agregarAlumno(self, alumno, alumnos=None):
        if alumnos is not None:
            self.listadoAlumnos.extend(alumnos)
        self.listadoAlumnos.append(alumno)

    def listadoAsignaturas(self, **kwargs):
        for key, value in kwargs.items():
            self._asignaturas.append(Asignatura(value))

    @staticmethod
    def asignarNombre(nombre="Grado 6"):
        Grupo.grado = nombre

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], listadoAlumnos=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = listadoAlumnos

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    def agregarAlumno(self, alumno, alumnos=[]):
        self.listadoAlumnos.append(alumno)
        self.listadoAlumnos.extend(alumnos)

    def listadoAsignaturas(self, **kwargs):
        for key, value in kwargs.items():
            self._asignaturas.append(Asignatura(value))

    @staticmethod
    def asignarNombre(nombre="Grado 6"):
        Grupo.grado = nombre
