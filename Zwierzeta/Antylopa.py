from src.Zwierze import Zwierze

class Antylopa(Zwierze):
    def __init__(self,pole,swiat):
        super().__init__(pole,swiat)
        self.zasieg=2
        self.inicjatywa=4
        self.sila=4