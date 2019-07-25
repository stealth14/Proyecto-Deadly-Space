import pygame
from pygame.locals import *
import sys
import os
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
win = pygame.display.set_mode((1000,700))
pygame.display.set_caption("First Game")
pygame.font.init()


pygame.mixer.music.set_volume(0.9) #Configuracion del Volumen
pygame.mixer.music.load("fondo.mp3") #Carga de mp3 sonido de fondo
pygame.mixer.music.play(0, 0.0) #Bucle infinito de reproduccion del sonido, se detiene al momento de un evento

run = True

puntos=50


#player 1
x = 500
y = 600
width = 50
height = 50
vel = 15

#bala

velb=10

disparo=False

#target coordinates

xPos = 50
yPos = 100

xVel = 1
yVel = -1.5

bala = pygame.image.load('mega_man.png').convert_alpha()
bala_mask = pygame.mask.from_surface(bala)
bala_rect = bala.get_rect()

nave = pygame.image.load('nave.png').convert_alpha()
nave_mask = pygame.mask.from_surface(nave)
nave_rect = nave.get_rect()

myfont = pygame.font.SysFont(None,50) #Se define el font

#Funcion para puntaje 
def Puntaje(marcador):
    if marcador<=0:
        puntaje=0
        vidaEnemigo = myfont.render('ENEMY DEAD',True,(255,255,255))
        nave = pygame.image.load('Fondo_Negro.png').convert_alpha()
        puntaje=puntaje+1
        puntajes = myfont.render('PUNTOS '+str(puntaje),True,(255,255,0))
        win.blit(nave,(xPos+30,yPos-50))
        win.blit(puntajes,(800,600))

    else:
        vidaEnemigo = myfont.render('ENEMI LIVE ',True,(255,255,0))
    win.blit(vidaEnemigo,(10,10))

#Funcion del tiempo de juego
def Tiempo():
    Time=int(pygame.time.get_ticks()/1000) #Obtenemos 
    mensaje = myfont.render('Tiempo: '+str(Time),True,(0,255,255))
    win.blit(mensaje,(480,10))



while run:
    #pausa el programa por una cantidad de tiempo 
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x -= vel
        
    if keys[pygame.K_d]:
        x += vel
        
    if keys[pygame.K_w]:
        y -= vel
        
    if keys[pygame.K_s]:    
        y += vel
        
    if keys[pygame.K_SPACE]:
        disparo=True
        yb=y
        xb=x

    win.fill((0,0,0))


    #target incremento

    xPos += xVel
    #yPos += yVel
 
    if xPos > 800 or xPos <10:
        xVel *= -1
    
    #if yPos >290 or yPos <10:
        #yVel *= -1

    #target
        
    #nave1 =  pygame.draw.circle(win, pygame.Color('GREEN') ,(xPos+30,yPos-50),60 ) 
    win.blit(nave,(xPos+30,yPos-50))


    #jugador1
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))


    #disparo
    if disparo and yb>0:
        yb-=velb        
        #bala = pygame.draw.circle(win, (255,255,255 ),(xb+30,yb),10)
        win.blit(bala,(xb+30,yb))
        offset=(xb-xPos,yb-yPos)
        colision = nave_mask.overlap(bala_mask,offset)
        #print(offset)
        
        if colision:
            puntos=puntos-1
            pygame.mixer.music.set_volume(0.9) 
            pygame.mixer.music.load("evento.mp3") 
            pygame.mixer.music.play() 

    Puntaje(puntos)     
    Tiempo()   
    pygame.display.update() 
    pygame.display.flip()

pygame.quit()
