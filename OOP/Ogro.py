from Enemigo import *

class Ogro(Enemigo):
    def _init_(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo= 'Ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplasta todo!!*")