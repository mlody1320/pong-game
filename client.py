import pygame, sys, os
from siec import Siec
pygame.font.init()
czcionka = pygame.font.SysFont('Sans Serif', 40)
szerokosc=1200
wysokosc=700

pygame.init()
ekran=pygame.display.set_mode((szerokosc,wysokosc))
pygame.display.set_caption("PONG Game - Kacprzyk")
dirname = os.path.dirname(__file__)
bg = pygame.image.load(os.path.join(dirname, "start.png"))

def Menu(okno):
    okno.fill((255,255,255))
    okno.blit(bg, (0, 0))
    pygame.display.update()

def Rysuj(okno, gra, gracz): 
    okno.fill((0,0,0))
    
    pos1=gra.pozycje[0]
    pos2=gra.pozycje[1]
    gracz1=pygame.Rect(pos1[0],pos1[1], 10,100)
    gracz2=pygame.Rect(pos2[0],pos2[1], 10,100)
    pilka=pygame.Rect(gra.poz_pilki_x,gra.poz_pilki_y, gra.pilka_rozmiar,gra.pilka_rozmiar)
    pygame.draw.ellipse(okno, (255,255,255), pilka)
    pygame.draw.line(okno, (255,255,255), (597, 0), (597, 700),6)
    pygame.draw.rect(okno, (255,0,0), gracz1)
    pygame.draw.rect(okno, (0,255,0), gracz2)

    wynik_g1=czcionka.render('WYNIK: ' + str(gra.punkty[0]), False, (255,255,255))
    wynik_g2=czcionka.render('WYNIK: ' + str(gra.punkty[1]), False, (255,255,255))
    okno.blit(wynik_g1, (szerokosc/4 - wynik_g1.get_width()/2,0))
    okno.blit(wynik_g2, (3*szerokosc/4 - wynik_g2.get_width()/2,0))

    if gra.koniec:
        font = pygame.font.SysFont("comicsans", 80)
        if(gra.punkty[gracz]>=9):
            text = font.render("WYGRAŁEŚ!", 1, (0,255,0), True)
        else:
            text = font.render("PRZEGRAŁEŚ!", 1, (255,0,0), True)
        okno.blit(text, (szerokosc/2 - text.get_width()/2, wysokosc/2 - text.get_height()/2))
    if not(gra.gotowa):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Oczekiwanie na gracza...", 1, (255,0,0), True)
        okno.blit(text, (szerokosc/2 - text.get_width()/2, wysokosc/2 - text.get_height()/2))


    pygame.display.update()
def start():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
                pygame.quit()
        k=pygame.key.get_pressed()
        if k[pygame.K_RETURN]:
            main()
        Menu(ekran)
        
def main():
    run=True
    clock=pygame.time.Clock()
    siec=Siec()
    gracz=int(siec.getP())
    print("Jesteś graczem ", gracz)

    while run:
        clock.tick(60)
        try:
            gra=siec.send("get")
        except: 
            run=False
            print("Nie można pobrać danych gry")
            break

        
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
                pygame.quit()
                
        if gra.gotowa and not(gra.koniec):
            k=pygame.key.get_pressed()
            if k[pygame.K_UP]:
                siec.send("w")
            elif k[pygame.K_DOWN]:
                siec.send("s")
                
                
        Rysuj(ekran,gra, gracz)
        if(gra.koniec):
            pygame.time.delay(2000)
            gra.koniec=False
            start()
        
    
    
    

start()