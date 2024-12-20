from abc import ABC, abstractmethod

class Trabajador:
    
    def __init__(self, id_trabajador, nombre, apellido):
        self.id_trabajador = id_trabajador
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def sueldo(self):  #Polimorfismo: Cada hijo lo implementa de forma diferente
        pass
    def horario(self):    
        pass
    

class Conserje(Trabajador):
    def __init__(self, horas_trabajadas):
        self.horas_trabajadas = horas_trabajadas

    def sueldo(self):
        return self.horas_trabajadas * 10

class Secretaria(Trabajador):
    def __init__(self, horas_trabajadas, incentivos):
        self.horas_trabajadas = horas_trabajadas
        self.incentivos = incentivos

    def sueldo(self):
        return self.horas_trabajadas * 12 + self.incentivos

class Directivo(Trabajador):
    def __init__(self,base,dietas,metas):
        self.base = base
        self.dietas = dietas
        self.metas = metas
    
    def sueldo(self):
        return self.base + self.dietas + self.metas