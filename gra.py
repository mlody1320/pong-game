import pygame, os
dirname = os.path.dirname(__file__)
class Gra:
    pygame.mixer.init()
    
    
    def __init__(self, id):
        self.gotowa=False
        self.id=id
        self.punkty=[0,0]
        self.pozycje=[[0,300],[1190,300]]
        self.poz_pilki_x=588
        self.poz_pilki_y=340
        self.pilka_rozmiar=20
        self.ppx=3
        self.ppy=3
        self.wys_okna=700
        self.szer_okna=1200
        self.punkt=0
        self.koniec=False
        
    def Reset(self):
        self.poz_pilki_x=588
        self.poz_pilki_y=340
        self.ppx*=-1
        if self.punkty[0]==9 or self.punkty[1]==9:
            self.koniec=True


    def polaczeni(self):
        return self.gotowa

    def wsp_pilki(self):
        return (self.poz_pilki_x, self.poz_pilki_y)
    
    def Ruch_pilki(self):
        hit=pygame.mixer.Sound(os.path.join(dirname,"hit.wav"))
        blok=pygame.mixer.Sound(os.path.join(dirname,"block_hit.wav"))
        punkt_sound=pygame.mixer.Sound(os.path.join(dirname,"punkt.wav"))
        self.poz_pilki_x += self.ppx
        self.poz_pilki_y += self.ppy
        if self.poz_pilki_y<=0 or self.poz_pilki_y+self.pilka_rozmiar>=self.wys_okna:
            self.ppy*=-1
            hit.play()
        if ((self.pozycje[0][1]-self.pilka_rozmiar<=self.poz_pilki_y  and self.poz_pilki_y<=self.pozycje[0][1]+100) and (self.poz_pilki_x<=10)) or ((self.pozycje[1][1]-self.pilka_rozmiar<=self.poz_pilki_y  and self.poz_pilki_y<=self.pozycje[1][1]+100) and (self.poz_pilki_x+self.pilka_rozmiar>=self.szer_okna-10)):
            self.ppx*=-1
            blok.play()

        if self.poz_pilki_x<=0:
            self.PunktP2()
            punkt_sound.play()

        elif self.poz_pilki_x+self.pilka_rozmiar>=self.szer_okna:
            self.PunktP1()
            punkt_sound.play()

            
        
    def PunktP1(self):
        self.punkty[0]+=1
        self.Reset()

    def PunktP2(self):
        self.punkty[1]+=1
        self.Reset()
        
        


    def rozgrywka(self, gracz, ruch):

        if ruch=="w":
            if self.pozycje[gracz][1]>=0:
                self.pozycje[gracz][1]-=15
        if ruch=="s":
            if (self.pozycje[gracz][1]+100)<=self.wys_okna:
                self.pozycje[gracz][1]+=15


    