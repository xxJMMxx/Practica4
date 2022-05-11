
from Herencia.Herencia_Poligono import Hexagono,  Pentagono, Heptagono


def main():
    pentakill = Pentagono(5)
    print(pentakill.getPerimetro())
    print(pentakill.getApotema())
    print(pentakill.getArea())
    print(" ")

    hex = Hexagono(6)
    print(hex.getPerimetro())
    print(hex.getApotema())
    print(hex.getArea())
    print(" ")

    hpt = Heptagono(7)
    print(hpt.getPerimetro())
    print(hpt.getApotema())
    print(hpt.getArea())


if __name__ == "__main__":
    main()
