from src import Swiat
import pygame
from pygame.locals import *
from src.Zwierze import Zwierze
from src.Zwierzeta import Antylopa
from src.Zwierzeta import Cyberowca
from src.Zwierzeta import Czlowiek
from src.Zwierzeta import Owca
from src.Zwierzeta import Wilk
from src.Zwierzeta import Zolw
from src.Zwierzeta import Lis
from src.Rosliny import Trawa
from src.Rosliny import Barszcz
import sys
import math

class Swiat_square(Swiat.Swiat):

    def __init__(self, x, y):
        self._load_images()
        for i in range(y):
            for j in range(x):
                pole = self.pole(j, i)
                self._pola.append(pole)

        for i in range(len(self._pola)):
            obecne_x=self._pola[i].x
            obecne_y=self._pola[i].y
            if obecne_x-1>=0:
                self._pola[i].sasiad.append(self._szukaj_sasiada(obecne_x-1, obecne_y))
            if obecne_y-1>=0:
                self._pola[i].sasiad.append(self._szukaj_sasiada(obecne_x,obecne_y-1))
            if(obecne_x+1<=x-1):
                self._pola[i].sasiad.append(self._szukaj_sasiada(obecne_x+1, obecne_y))
            if (obecne_y + 1 <= y - 1):
                self._pola[i].sasiad.append(self._szukaj_sasiada(obecne_x, obecne_y+1))

    def _sortuj(self):
        super()._sortuj()

    def _load_images(self):
        super()._load_images()

    def _wybierz_zdjecie(self, mieszkaniec):
        if isinstance(mieszkaniec, Antylopa.Antylopa):
            zdjecie = self._img_antylopa_S
        if isinstance(mieszkaniec, Cyberowca.Cyberowca):
            zdjecie = self._img_cyberowca_S
        if isinstance(mieszkaniec, Czlowiek.Czlowiek):
            zdjecie = self._img_czlowiek_S
        if isinstance(mieszkaniec, Wilk.Wilk):
            zdjecie = self._img_wilk_S
        if isinstance(mieszkaniec, Zolw.Zolw):
            zdjecie = self._img_zolw_S
        if isinstance(mieszkaniec, Owca.Owca):
            zdjecie = self._img_owca_S
        if isinstance(mieszkaniec, Lis.Lis):
            zdjecie = self._img_lis_S
        if isinstance(mieszkaniec, Trawa.Trawa):
            zdjecie = self._img_trawa_S
        if isinstance(mieszkaniec, Barszcz.Barszcz):
            zdjecie = self._img_barszcz_S
        if mieszkaniec == 0:
            zdjecie = self._img_square

        return zdjecie

    def rysuj(self):

        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('moj pytjhon')
        window.fill((145, 205, 25))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for i in range(len(self._pola)):
            window.blit(self._wybierz_zdjecie(self._pola[i].mieszkaniec),
                        (40 * self._pola[i].x, 40 * self._pola[i].y))
        pygame.display.update()

    def inicjuj_ture(self):
        super().inicjuj_ture()

    def wykonaj_ture(self):
        self.inicjuj_ture()
        for i in range(len(self._pola)):
            if self._pola[i].mieszkaniec!=0:
                self._pola[i].mieszkaniec.akcja()

    def _szukaj_sasiada(self,x,y):
        #super()._szukaj_sasiada(x,y)
        for i in range(len(self._pola)):
            if self._pola[i].x==x and self._pola[i].y==y:
                pole=self._pola[i]
                return self._pola[i]

