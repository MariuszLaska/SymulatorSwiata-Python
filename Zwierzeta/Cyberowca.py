from src.Zwierze import Zwierze
from src.Rosliny import Barszcz
class Cyberowca(Zwierze):
    def __init__(self,pole,swiat):
        super().__init__(pole,swiat)
        self.zasieg=1
        self.inicjatywa=4
        self.sila=11

    def __szukaj_barszczu(self):
        odleglosc=99999999
        barszcz=0
        for i in range(len(self.swiat._pola)):
            if isinstance(self.swiat._pola[i].mieszkaniec, Barszcz.Barszcz):
                dx = abs(self.pole.x - self.swiat._pola[i].x)
                dy = abs(self.pole.y - self.swiat._pola[i].y)
                if (dy + max(0, (dx - dy) / 2))<odleglosc:
                    odleglosc = dy + max(0, (dx - dy) / 2)
                    barszcz=self.swiat._pola[i].mieszkaniec
        return barszcz
    def akcja(self):
        barszcz = self.__szukaj_barszczu()
        if barszcz != 0:
            if self.czy_sie_ruszyl == 0:
                wybrane_pole=0
                sasiedzi = self._szukaj_sasiadow(self.pole)


                if barszcz.pole.x<self.pole.x and barszcz.pole.y==self.pole.y:
                    wybrane_pole=0
                if barszcz.pole.x < self.pole.x and barszcz.pole.y > self.pole.y:
                    wybrane_pole = 1
                if barszcz.pole.x == self.pole.x and barszcz.pole.y < self.pole.y:
                    wybrane_pole = 1
                if barszcz.pole.x > self.pole.x and barszcz.pole.y < self.pole.y:
                    wybrane_pole = 2
                if barszcz.pole.x > self.pole.x and barszcz.pole.y == self.pole.y:
                    wybrane_pole = 3
                if barszcz.pole.x > self.pole.x and barszcz.pole.y > self.pole.y:
                    wybrane_pole = 4
                if barszcz.pole.x == self.pole.x and barszcz.pole.y > self.pole.y:
                    wybrane_pole = 4
                if barszcz.pole.x < self.pole.x and barszcz.pole.y < self.pole.y:
                    wybrane_pole = 5


                walka = True

                if sasiedzi[wybrane_pole].mieszkaniec != 0:
                    walka = self._kolizja(self.pole, sasiedzi[wybrane_pole])
                if sasiedzi[wybrane_pole].mieszkaniec == 0 or \
                        (sasiedzi[wybrane_pole].mieszkaniec != 0 and walka == True) or isinstance(sasiedzi[wybrane_pole].mieszkaniec, Barszcz.Barszcz):
                    self.pole.mieszkaniec = 0
                    self.pole = sasiedzi[wybrane_pole]
                    sasiedzi[wybrane_pole].mieszkaniec = self
                    sasiedzi = []
                    self.czy_sie_ruszyl = 1
        else:
            super().akcja()


