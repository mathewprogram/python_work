import math
class Circulo:
    #Constructor (Inicializar los atributos objeto)
    def __init__(self, radio):
        #self.radio = radio #publico
        self.__radio = radio #privado (por raya_) esto se puede modificar 
                            #solo atraves de un metodo
        
    def set_radio(self, radio):
            self.__radio = radio
        
    def get_radio(self):
            return self.__radio
    
    def area(self):
            return math.pi * (self.__radio**2)
            #return math.pi() * self.radio * self.radio
            #return math.pi() * self.radio**2
            #return math.pi() * math.pow(self.radio,2)
    
    def __str__(self):
            return f"Radio: {self.__radio} Area: {self.area()}"

def area(radio):
    return math.pi * (radio**2)