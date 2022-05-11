import math as raiz
from abc import ABC


class Poligono(ABC):
    _area = float(0)
    _perimetro = float(0)
    _apotema = float(0)

    @staticmethod
    def calcularArea():
        pass

    @staticmethod
    def calcularPerimetro():
        pass

    @staticmethod
    def calcularApotema():
        pass

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro

    def getApotema(self):
        return self._apotema


class Hexagono(Poligono):
    __cateto = float()

    def __init__(self, cateto):
        if cateto < 0:
            self.__cateto = 0
        else:
            self.__cateto = cateto
        self.calcularPerimetro()
        self.calcularApotema()
        self.calcularArea()

    def calcularArea(self):
        self._area = self._perimetro * self._apotema / 2

    def calcularPerimetro(self):
        self._perimetro = self.__cateto * 6

    def calcularApotema(self):
        self._apotema = (raiz.sqrt((self.__cateto * self.__cateto) - ((self.__cateto / 2) * (self.__cateto / 2))))


class Pentagono(Poligono):
    __lado = float(0)

    def __init__(self, lado):
        if lado < 0:
            self.__lado = 0
        else:
            self.__lado = lado

        self.calcularPerimetro()
        self.calcularApotema()
        self.calcularArea()

    def calcularArea(self):
        self._area = self._perimetro * self._apotema / 2

    def calcularPerimetro(self):
        self._perimetro = self.__lado * 5

    def calcularApotema(self):
        self._apotema = self.__lado / 1.4539


class Heptagono(Poligono):
    __lado = float(0)

    def __init__(self, lado):
        if lado < 0:
            self.__lado = 0
        else:
            self.__lado = lado

        self.calcularPerimetro()
        self.calcularApotema()
        self.calcularArea()

    def calcularArea(self):
        self._area = self._perimetro * self._apotema / 2

    def calcularPerimetro(self):
        self._perimetro = self.__lado * 7

    def calcularApotema(self):
        self._apotema = self.__lado / 0.9631
