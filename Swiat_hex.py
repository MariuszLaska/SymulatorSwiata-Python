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
from src.Rosliny import Mlecz
from src.Rosliny import Jagody
from src.Rosliny import Guarana
import sys
import math


class Swiat_hex(Swiat.Swiat):
    def __init__(self,x,y):
        self._load_images()
        self.__wielkosc_x=x
        self.__wielkosc_y=y
        for i in range(y):
            for j in range(x):
                if i%2==0:
                    pole = self.pole(j*2, i)
                else:
                    pole = self.pole((j*2)+1, i)
                self._pola.append(pole)


        for i in range(len(self._pola)):
            __obecne_x = self._pola[i].x
            __obecne_y = self._pola[i].y
            if __obecne_x-2>=0:
                self._pola[i].sasiad.append(self._szukaj_sasiada(__obecne_x-2,__obecne_y))
            else:
                self._pola[i].sasiad.append(0)
            if  __obecne_x-1>=0 and __obecne_y-1>=0:
                self._pola[i].sasiad.append(self._szukaj_sasiada(__obecne_x-1, __obecne_y-1))
            else:
                self._pola[i].sasiad.append(0)
            if __obecne_x+1 <= (2 * x) - 1 and __obecne_y - 1 >= 0:
                self._pola[i].sasiad.append(self._szukaj_sasiada(__obecne_x + 1, __obecne_y - 1))
            else:
                self._pola[i].sasiad.append(0)
            if __obecne_x+2 <= (2 * x) - 1:
                self._pola[i].sasiad.append(self._szukaj_sasiada(__obecne_x + 2, __obecne_y))
            else:
                self._pola[i].sasiad.append(0)
            if __obecne_x+1<=(2*x)-1 and __obecne_y+1<y:
                self._pola[i].sasiad.append(self._szukaj_sasiada(__obecne_x + 1, __obecne_y + 1))
            else:
                self._pola[i].sasiad.append(0)
            if __obecne_x-1>=0 and __obecne_y+1<y:
                self._pola[i].sasiad.append(self._szukaj_sasiada(__obecne_x - 1, __obecne_y + 1))
            else:
                self._pola[i].sasiad.append(0)

    def _sortuj(self):
        super()._sortuj()

    def _load_images(self):
        super()._load_images()
    def _wybierz_zdjecie(self,mieszkaniec):
        if isinstance(mieszkaniec, Antylopa.Antylopa):
             zdjecie=self._img_antylopa
        if isinstance(mieszkaniec, Cyberowca.Cyberowca):
            zdjecie = self._img_cyberowca
        if isinstance(mieszkaniec, Czlowiek.Czlowiek):
            zdjecie = self._img_czlowiek
        if isinstance(mieszkaniec, Wilk.Wilk):
            zdjecie = self._img_wilk
        if isinstance(mieszkaniec, Zolw.Zolw):
            zdjecie = self._img_zolw
        if isinstance(mieszkaniec, Owca.Owca):
            zdjecie = self._img_owca
        if isinstance(mieszkaniec, Lis.Lis):
            zdjecie = self._img_lis
        if isinstance(mieszkaniec, Trawa.Trawa):
            zdjecie = self._img_trawa
        if isinstance(mieszkaniec, Barszcz.Barszcz):
            zdjecie = self._img_barszcz
        if isinstance(mieszkaniec, Mlecz.Mlecz):
            zdjecie = self._img_mlecz
        if isinstance(mieszkaniec, Guarana.Guarana):
            zdjecie = self._img_guarana
        if isinstance(mieszkaniec, Jagody.Jagody):
            zdjecie = self._img_jagody
        if mieszkaniec == 0:
            zdjecie = self._img_hex

        return zdjecie

    def _szukaj_sasiada(self,x,y):
        #super()._szukaj_sasiada(x,y)
        for i in range(len(self._pola)):
            if self._pola[i].x==x and self._pola[i].y==y:
                pole=self._pola[i]
                return self._pola[i]

    def inicjuj_ture(self):
        super().inicjuj_ture()

    def wykonaj_ture(self):
        self.inicjuj_ture()
        for i in range(len(self._pola)):
            if self._pola[i].mieszkaniec!=0:
                self._pola[i].mieszkaniec.akcja()


    def rysuj(self):

        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('moj pytjhon')
        window.fill((145, 205, 25))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for i in range(len(self._pola)):
            window.blit(self._wybierz_zdjecie(self._pola[i].mieszkaniec),
                        (22 * math.sqrt(3) / 2 * self._pola[i].x, 22 * 3 / 2 * self._pola[i].y))
        pygame.display.update()

    def _zapis(self):
        file = open('/Users/mariuszlaska/Desktop/Projekty/ProjektPO3/src/zapis.txt',"w")

        file.write("hex")
        file.write('\n')
        file.write(str(self.__wielkosc_x))
        file.write('\n')
        file.write(str(self.__wielkosc_y))
        file.write('\n')
        for i in range(len(self._pola)):
            if self._pola[i].mieszkaniec!=0:
                file.write(str(type(self._pola[i].mieszkaniec)))
                file.write('\n')
                file.write(str(self._pola[i].x))
                file.write('\n')
                file.write(str(self._pola[i].y))
                file.write('\n')
                if isinstance(self._pola[i].mieszkaniec, Czlowiek.Czlowiek):
                    file.write(str(self._pola[i].mieszkaniec.cooldown))
                    file.write('\n')

        file.close()


