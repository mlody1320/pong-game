import socket
from _thread import *
import pickle
from gra import Gra
import pygame

server="localhost"
port=5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #gniazdo IPv4

try:
    s.bind((server,port)) #podpina port
except socket.error as e:
    str(e)

s.listen(2) #2 użytkowników
print("Oczekiwanie na połączenie, Serwer został uruchomiony")

connected=set()
gry={}
licznik_id=0

def podlaczony_klient(conn, gracz, id_gry): #podłączony klient
    print("ID GRY",id_gry)
    global licznik_id
    conn.send(str.encode(str(gracz)))
    #conn.sendall(str.encode(str(gracz)))
    
    clock=pygame.time.Clock()
    while True:
        clock.tick(60)
        try:
            dane=conn.recv(4096).decode()
            
            if id_gry in gry: 
                gra=gry[id_gry]
                if not dane:
                    print("Rozłączono")
                    break
                else:
                    
                    if gra.gotowa and not(gra.koniec):
                        gra.Ruch_pilki()
                    
                    if dane!="get":
                        gra.rozgrywka(gracz, dane)
                    conn.sendall(pickle.dumps(gra))
            else:
                break
        except:
            break
    print("Połączenie zostało zerwane")
    try:
        del gry[id_gry]
        print("Zamykanie gry ", id_gry)
    except:
        pass
    licznik_id-=1

    conn.close()


while True:
    conn, addr=s.accept() #odebranie połączenia
    print("Połączono z: ", addr)
    licznik_id+=1
    gracz=0
    id_gry=(licznik_id-1)//2
    if licznik_id % 2==1:
        gry[id_gry]=Gra(id_gry)
        print("Tworzenie nowej gry...")
    else:
        gry[id_gry].gotowa=True
        gracz=1

    start_new_thread(podlaczony_klient, (conn,gracz, id_gry))

