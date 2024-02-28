from musicos import *
from random import choice, randint


class banda:

    def __init__(self):
        self.musicos = []
        self.instrumentos = [Guitarra(), Cuatro(), Saxo(), Flauta(), Triple(), Piano()]
        self.amigos = ["juan", "miguel", "maria", "ana", "juana", "pedro"]
    
    def crear_banda(self, cantidad_musicos):
        for i in range(cantidad_musicos):
            self.musicos.append(Musico(choice(self.amigos)))
            self.musicos[-1].asignar_instrumentos(choice(self.instrumentos))

    def mostrar_banda(self):
        for m in self.musicos:
            print(m.nombre)
            print(m.instrumento())


if __name__ == "__main__":
    b = banda()
    b.crear_banda(3)
    b.mostrar_banda()
    print("afinamos la banda: ")
    b.afinar_banda()
    print("a tocar")
    b.tocar_banda()