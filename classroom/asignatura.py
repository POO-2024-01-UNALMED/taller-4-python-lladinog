class Asignatura:

    def __init__(self, nombre, salon=None):
        self._nombre = nombre
        self._salon = salon if salon else "Remoto"

    def __str__(self):
         return f"{self._nombre} {self._salon}" if self._salon else f"{self._nombre}"