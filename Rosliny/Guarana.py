from src.Roslina import Roslina
import random

class Guarana(Roslina):
    def __init__(self,pole):
        super().__init__(pole)
        self.sila=0

    def akcja(self):
        sasiedzi = self._szukaj_sasiadow(self.pole)
        for i in range(len(sasiedzi)):
            sasiedzi[i].mieszkaniec=0
        if self.urodzil==False:
            random.seed()
            if(random.randrange(2)):
                wybrane_pole=random.randrange(len(sasiedzi))
                sadzonka=type(self.pole.mieszkaniec)
                nowy=sadzonka(sasiedzi[wybrane_pole])
                nowy.urodzil=True
                self.urodzil=True