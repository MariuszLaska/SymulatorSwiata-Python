from src.Zwierze import Zwierze
import pygame
from pygame.locals import *
import sys
import random

class Czlowiek(Zwierze):
    def __init__(self,pole,swiat):
        super().__init__(pole,swiat)
        self.zasieg=1
        self.inicjatywa=4
        self.sila=5
        self.cooldown=-5
    def akcja(self):
        if self.czy_sie_ruszyl==0:

            __przycisk=False
            while __przycisk == False:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.QUIT:
                            pygame.quit();
                        if event.key == pygame.K_a:
                            wybrane_pole=0
                            __przycisk=True
                        if event.key == pygame.K_q:
                            wybrane_pole=1
                            __przycisk=True
                        if event.key == pygame.K_e:
                            wybrane_pole=2
                            __przycisk=True
                        if event.key == pygame.K_d:
                            wybrane_pole=3
                            __przycisk=True
                        if event.key == pygame.K_c:
                            wybrane_pole=4
                            __przycisk=True
                        if event.key == pygame.K_z:
                            wybrane_pole=5
                            print("prawo")
                            __przycisk=True
                        if event.key == pygame.K_m:
                           self.__aktywuj_moc()
                        if event.key == pygame.K_p:
                            self.swiat._zapis()

            self.__moc()
            for i in range(self.zasieg):
                if self.pole.sasiad[wybrane_pole]==0:
                    break
                walka = True
                if self.pole.sasiad[wybrane_pole].mieszkaniec != 0:
                    walka=self._kolizja(self.pole,self.pole.sasiad[wybrane_pole])
                if self.pole.sasiad[wybrane_pole].mieszkaniec == 0 or \
                        (self.pole.sasiad[wybrane_pole].mieszkaniec != 0 and walka==True) :
                    self.pole.mieszkaniec=0
                    self.pole=self.pole.sasiad[wybrane_pole]
                    self.pole.mieszkaniec=self
                    self.czy_sie_ruszyl=1
                if walka == False:
                    break
        else:
            pass

    def __aktywuj_moc(self):
        if self.cooldown<=-5:
            self.cooldown=5

    def __moc(self):
        if self.cooldown >= 2:
            self.zasieg=2
        if self.cooldown>0 and self.cooldown<2:
            random.seed()
            __szansa=random.randrange(2)
            if __szansa == 1:
                self.zasieg=2
            else:
                self.zasieg=1
        if self.cooldown <= 0:
            self.zasieg=1

        self.cooldown-=1



