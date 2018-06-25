from src.Zwierze import Zwierze
import random

class Lis(Zwierze):
    def __init__(self,pole,swiat):
        super().__init__(pole,swiat)
        self.zasieg=1
        self.inicjatywa=7
        self.sila=3

    def _szukaj_sasiadow(self, pole, sila):
        sasiedzi = []
        for i in range(len(pole.sasiad)):
             if pole.sasiad[i] != 0 :
                if pole.sasiad[i].mieszkaniec!=0:
                    if pole.sasiad[i].mieszkaniec.sila<=sila:
                        sasiedzi.append(pole.sasiad[i])
                else:
                    sasiedzi.append(pole.sasiad[i])
        return sasiedzi

    def akcja(self):
        if self.czy_sie_ruszyl==0:
            __sasiedzi = self._szukaj_sasiadow(self.pole, self.sila)
            random.seed
            wybrane_pole=random.randrange(len(__sasiedzi))
            for i in range(self.zasieg):
                if len(__sasiedzi)<=wybrane_pole:
                    break;
                #warunek czy mmozna sie ruszyc
                self.pole.mieszkaniec=0
                self.pole=__sasiedzi[wybrane_pole]
                __sasiedzi[wybrane_pole].mieszkaniec=self
                __sasiedzi=[]
            self.czy_sie_ruszyl=1
        else:
            pass
