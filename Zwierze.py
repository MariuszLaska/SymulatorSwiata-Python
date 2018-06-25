import time
import random
import abc
from src import Organizm


class Zwierze(Organizm.Organizm, metaclass=abc.ABCMeta):

    def __init__(self, pole, swiat):
        self.swiat=swiat
        self.zasieg=1
        self.czy_sie_ruszyl = 0
        self.pole = pole
        self.urodzil=False
        pole.mieszkaniec=self



    def _kolizja(self,pole1,pole2):
        if type(pole1.mieszkaniec) == type(pole2.mieszkaniec):
            if(pole1.mieszkaniec.urodzil==False and pole1.mieszkaniec.urodzil==False ):
                for i in range(len(pole2.sasiad)):
                    if pole2.sasiad[i]!= 0:
                        if pole2.sasiad[i].mieszkaniec == 0:
                            dziecko=type(pole1.mieszkaniec)
                            pole1.mieszkaniec.urodzil=True
                            pole2.mieszkaniec.urodzil = True
                            nowy = dziecko(pole2.sasiad[i],self.swiat)
                            nowy.urodzil=True
                            return False
        else:
            if pole2.mieszkaniec!=0:
                if pole1.mieszkaniec.sila>=pole2.mieszkaniec.sila:
                    if(pole2.mieszkaniec._odbicie_ataku()==True and pole1.mieszkaniec.sila<5):
                        return False
                    else:
                        pole2.mieszkaniec=0
                        return True
                else:
                    print("owca zabija")
                    pole1.mieszkaniec=0
                    return False
            else:
                return True

    def akcja(self):
        if self.czy_sie_ruszyl==0:
            sasiedzi = self._szukaj_sasiadow(self.pole)
            random.seed
            wybrane_pole=random.randrange(len(sasiedzi))
            for i in range(self.zasieg):
                sasiedzi = self._szukaj_sasiadow(self.pole)
                if len(sasiedzi)<=wybrane_pole:
                    break;
                walka = True
                if sasiedzi[wybrane_pole].mieszkaniec!= 0:
                    walka=self._kolizja(self.pole,sasiedzi[wybrane_pole])
                if sasiedzi[wybrane_pole].mieszkaniec == 0 or \
                        (sasiedzi[wybrane_pole].mieszkaniec!=0 and walka==True ):
                    self.pole.mieszkaniec=0
                    self.pole=sasiedzi[wybrane_pole]
                    sasiedzi[wybrane_pole].mieszkaniec=self
                    sasiedzi=[]
                    self.czy_sie_ruszyl=1
                if walka == False:
                    break
        else:
            pass






