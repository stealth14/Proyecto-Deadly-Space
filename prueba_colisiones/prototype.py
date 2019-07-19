import pygame
from pygame.locals import *
import sys
pygame.init()
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("First Game")
pygame.font.init()

run = True

puntos=50


#player 1
x = 400
y = 500
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
        win.blit(puntajes,(400,700))

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
            print('La bala le dio')
            puntos=puntos-1

    Puntaje(puntos)     
    Tiempo()   
    pygame.display.update() 
    pygame.display.flip()

pygame.quit()
