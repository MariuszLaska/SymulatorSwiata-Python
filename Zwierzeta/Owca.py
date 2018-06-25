from src.Zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self,pole,swiat):
        super().__init__(pole,swiat)
        self.zasieg=1
        self.inicjatywa=4
        self.sila=3