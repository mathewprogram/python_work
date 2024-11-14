#!/usr/bin/env python
# -*- coding: utf8 -*-
import os, random
from clases import Circulo, area

def ejemplo1():
    c = Circulo(random.randint(1,10))
    print(f"Radio: {c.radio}")
    c.radio = 20
    print("Radio", c.radio)

def ejemplo2():
    lista_objetos = []
    for i in range(100):
        c = Circulo(random.randint(1,10))
        lista_objetos.append(c)
    
    nr = 1
    for objeto in lista_objetos:
        print(f"Objeto: {nr}- Radio: {objeto.radio}")
        nr += 1

def ejemplo3():
    c = Circulo(random.randint(1,10))
    print(c.get_radio())
    c.set_radio(20)
    print(c.get_radio())

def ejemplo4():
    radio = int(input("Ingresa el radio: "))
    c = Circulo(radio)
    print(f"Radio: {c.get_radio()}")
    print(f"Area: {c.area()}")
    print(c)

    print("Area: (llamar la funcion)", area(radio))

def main():
    os.system("clear")
    #ejemplo1()
    #ejemplo2()
    #ejemplo3() 
    ejemplo4()     
if __name__ == "__main__":
   main()


