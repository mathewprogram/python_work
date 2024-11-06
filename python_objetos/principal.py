#!/usr/bin/env python
# -*- coding: utf8 -*-
import os, random
from clases import Circulo

def ejemplo1():
    c = Circulo(random.randint(1,10))
    print(f"Radio: {c.radio}")
    c.radio = 20
    print("Radio", c.radio)

def ejempl2():
    pass

def main():
    ejemplo1()
          
if __name__ == "__main__":
   main()


