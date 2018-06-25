from src.Zwierze import Zwierze

class Wilk(Zwierze):
    def __init__(self,pole,swiat):
        super().__init__(pole,swiat)
        self.zasieg=1
        self.inicjatywa=5
        self.sila=9