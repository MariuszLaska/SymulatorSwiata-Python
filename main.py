from src import Swiat
import pygame
from src.Swiat import Swiat
from src.Swiat_hex import Swiat_hex
from src.Swiat_square import Swiat_square
from src.Zwierze import Zwierze
from src.Roslina import Roslina
from src.Zwierzeta import Antylopa
from src.Zwierzeta import Cyberowca
from src.Zwierzeta import Czlowiek
from src.Zwierzeta import Owca
from src.Zwierzeta import Wilk
from src.Zwierzeta import Zolw
from src.Zwierzeta import Lis
from src.Rosliny import Trawa
from src.Rosliny import Barszcz
from src import Organizm
import time

swiat = Swiat_hex(10,10)
zwierze=Lis.Lis(swiat._pola[32],swiat)
zwierze2=Owca.Owca(swiat._pola[4],swiat)
zwierze1=Trawa.Trawa(swiat._pola[57])
zwierze1=Barszcz.Barszcz(swiat._pola[67])
zwierze1=Cyberowca.Cyberowca(swiat._pola[87],swiat)
zwierze1=Czlowiek.Czlowiek(swiat._pola[92],swiat)
zwierze1=Antylopa.Antylopa(swiat._pola[23],swiat)
zwierze1=Wilk.Wilk(swiat._pola[22],swiat)


while True:
    swiat.wykonaj_ture()
    time.sleep(0.9)