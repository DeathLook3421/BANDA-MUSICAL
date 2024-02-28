import random


class Instrumento:
    
    def afinar(self):
        pass

    def tocar(self):
         pass
    
    def mostrar(self):
         return "instrumento: " + str(type(self)).split("-")[-1][:-2]


class Guitarra(Instrumento):
    
    def afinar(self):
        print("Afinando guitarra")
        
    def tocar(self):
        print("tocando guitarra")
        

class Saxo(Instrumento):
    
    def afinar(self):
        print("Afinando saxo")
        
    def tocar(self):
        print("tocando saxo")


class Cuatro(Instrumento):
    
    def afinar(self):
        print("Afinando cuatro")
        
    def tocar(self):
        print("tocando cuatro")


class Flauta(Instrumento):
    
    def afinar(self):
        print("Afinando flauta")
        
    def tocar(self):
        print("tocando flauta")


class Triple(Instrumento):
    
    def afinar(self):
        print("Afinando triple")
        
    def tocar(self):
        print("tocando triple")


class Piano(Instrumento):
    
    def afinar(self):
        print("Afinando Piano")
        
    def tocar(self):
        print("tocando Piano")