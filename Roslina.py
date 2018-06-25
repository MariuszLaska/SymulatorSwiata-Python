import random
from src import Organizm
class Roslina(Organizm.Organizm):
    def __init__(self,pole):
        self.pole=pole
        self.inicjatywa=0
        pole.mieszkaniec=self
        self.urodzil=False



    def akcja(self):
        if self.urodzil==False:
            random.seed()
            if(random.randrange(5)==1):
                sasiedzi=self._szukaj_sasiadow(self.pole)
                for i in range(len(sasiedzi)):
                    wybrane_pole=random.randrange(len(sasiedzi))
                    if (sasiedzi[wybrane_pole].mieszkaniec == 0):
                        sadzonka=type(self.pole.mieszkaniec)
                        nowy=sadzonka(sasiedzi[wybrane_pole])
                        nowy.urodzil=True
                        self.urodzil=True
                        break


