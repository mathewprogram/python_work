from abc import ABC, abstractmethod
from tabulate import tabulate 

class SeleccionFutbol:

    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    @abstractmethod
    def Concentrarse(self):
        pass

    @abstractmethod
    def Viajar(self):
        pass


class Futbolista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, dorsal, posicion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.posicion = posicion

class Entrenador(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacion = idFederacion

class Masajista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, titulacion, anios_experiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.anios_experiencia = anios_experiencia