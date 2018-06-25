# from src.Zwierzeta import Antylopa
# from src.Zwierzeta import Cyberowca
# from src.Zwierzeta import Czlowiek
# from src.Zwierzeta import Owca
# from src.Zwierzeta import Wilk
# from src.Zwierzeta import Zolw
import abc
class Organizm(metaclass=abc.ABCMeta):
    def __init__(self, pole):
        pass

    def _szukaj_sasiadow(self, pole):
        sasiedzi = []
        for i in range(len(pole.sasiad)):
             if pole.sasiad[i] != 0:
                sasiedzi.append(pole.sasiad[i])
        return sasiedzi

    def _odbicie_ataku(self):
        return False