import pygame
import abc
from pygame.locals import *
class Swiat(metaclass=abc.ABCMeta):

    _pola=[]

    @abc.abstractmethod
    def _szukaj_sasiada(self,x,y):
        for i in range(len(self.pola)):
            if self.pola[i].x==x and self.pola[i].y==y:
                pole=self.pola[i]
                return self.pola[i]

    @abc.abstractmethod
    def _load_images(self):
        self._img_hex = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex.png')
        self._img_zolw = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_zolw.png')
        self._img_roslina = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_roslina.png')
        self._img_antylopa = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_antylopa.png')
        self._img_wilk = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_wilk.png')
        self._img_owca = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_owca.png')
        self._img_cyberowca = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_cyberowca.png')
        self._img_lis = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_lis.png')
        self._img_czlowiek = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_czlowiek.png')
        self._img_trawa = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_trawa.png')
        self._img_barszcz = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_barszcz.png')
        self._img_mlecz = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_mlecz.png')
        self._img_guarana = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/Hex_guaranna.png')

        self._img_square = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square.png')
        self._img_zolw_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_zolw.png')
        self._img_antylopa_S = pygame.image.load( '/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_antylopa.png')
        self._img_wilk_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_wilk.png')
        self._img_owca_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_owca.png')
        self._img_cyberowca_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_cyberowca.png')
        self._img_lis_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_lis.png')
        self._img_czlowiek_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_czlowiek.png')
        self._img_trawa_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_trawa.png')
        self._img_barszcz_S = pygame.image.load('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/images/square_barszcz.png')

    @abc.abstractmethod
    def inicjuj_ture(self):
        for i in range(len(self._pola)):
            if self._pola[i].mieszkaniec!=0:
                self._pola[i].mieszkaniec.czy_sie_ruszyl=0
                self._pola[i].mieszkaniec.urodzil=False
        self._sortuj()
        self.rysuj()

    @abc.abstractmethod
    def wykonaj_ture(self):
        pass

    @abc.abstractmethod
    def _sortuj(self):
        n=0
        for i in range(len(self._pola)):
            if self._pola[i].mieszkaniec == 0:
                l=i+1
                while(l<len(self._pola)):
                    if self._pola[l].mieszkaniec!=0:
                        tmp=self._pola[i]
                        self._pola[i]=self._pola[l]
                        self._pola[l]=tmp
                        n+=1
                        break
                    l+=1

        for i in range(n):
            for j in range(0, n - i - 1):
                if self._pola[j].mieszkaniec.inicjatywa < self._pola[j + 1].mieszkaniec.inicjatywa:
                    self._pola[j], self._pola[j + 1] = self._pola[j + 1], self._pola[j]



    def _klikniecie(self):
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self._dodaj(pos[0],pos[1])==1:
                        print("halo")


    class pole:
        x=0
        y=0
        mieszkaniec=0
        sasiad=[]
        def __init__(self,x,y):
            self.sasiad = []
            self.x=x
            self.y=y
