from src.Zwierze import Zwierze

class Zolw(Zwierze):
    def __init__(self,pole,swiat):
        super().__init__(pole,swiat)
        self.zasieg=1
        self.inicjatywa=1
        self.sila=2

    def _odbicie_ataku(self):
        import random
        random.seed
        odbicie = random.randrange(2)
        if odbicie==1:
            return True
        else:
            return False