import pygame
from datetime import datetime
import sys
import os

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

#captura del tiempo inicial
tiempo_inicial=datetime.now()

#----------------Inicializacion Joystick

# Evita que el programa se detega si no hay un mando conectado
conectado = False
try:
    j = pygame.joystick.Joystick(0) # Crear instancia del Joystick
    j.init() # Inicia el Joystick para usarlo
    print ("Se detecto un mando: {0}".format(j.get_name()))
    conectado = True
except pygame.error:
    print ("No hay un mando conectado.")

win = pygame.display.set_mode((1000,700))
pygame.display.set_caption("First Game")

#----------------------sonidos
laser=pygame.mixer.Sound('laser.wav')
acierta = pygame.mixer.Sound('evento.wav')
fondo=pygame.mixer.music.load('Song Of Storms Dubstep Remix - Ephixa.mp3')
pygame.mixer.music.play(-1)

run = True

puntos=50

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


width = 50 #para creacion de rectangulo
height = 50 #para creacion de rectangulo
vel = 25 #para movimiento 

#player 1
xj1 = 200
yj1 = 500

#player 2
xj2 = 600
yj2 = 500

#bala

velb=20

disparo1=False
disparo2=False

#target coordinates

xPos = 50
yPos = 100

xVel = 6
yVel = -1.5

bala = pygame.image.load('mega_man.png').convert_alpha()
bala_mask = pygame.mask.from_surface(bala)
bala_rect = bala.get_rect()

bala2 = pygame.image.load('mega_man.png').convert_alpha()
bala_mask2 = pygame.mask.from_surface(bala2)
bala_rect2 = bala2.get_rect()

nave = pygame.image.load('nave.png').convert_alpha()
nave_mask = pygame.mask.from_surface(nave)
nave_rect = nave.get_rect()

myfont = pygame.font.SysFont(None,50) #Se define el font

#Funcion para puntaje 
def Puntaje(life):
    global cont
    global enemilive
    cont=0
    if life<=0:
        #puntaje=0
        vidaEnemigo = myfont.render('ENEMY DEAD',True,(255,255,255))
        #nave = pygame.image.load('Fondo_Negro.png').convert_alpha()
        #puntaje=puntaje+1
        #puntajes = myfont.render('PUNTOS '+str(puntaje),True,(255,255,0))
        #win.blit(nave,(xPos+30,yPos-50))
        #win.blit(puntajes,(800,600))
        cont=cont+1
        enemilive=False
        Puntos(cont)
        
    else:
        vidaEnemigo = myfont.render('ENEMI LIVE ',True,(255,255,0))
    win.blit(vidaEnemigo,(10,10))

#Funcion del tiempo de juego
def Tiempo():
    Time=int(pygame.time.get_ticks()/1000) #Obtenemos 
    mensaje = myfont.render('Tiempo: '+str(Time),True,(0,255,255))
    win.blit(mensaje,(480,10))

#Funcion que controla la puntuacion
def Puntos(punts):
    mensaje = myfont.render('PUNTOS '+str(punts),True,(255,255,0))
    win.blit(mensaje,(700,600))
    puntos=50


while run:
    #pausa el programa por una cantidad de tiempo 
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#________________MOVIMIENTO JUGADOR 1________________#
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        xj1 -= vel
    if keys[pygame.K_d]:
        xj1 += vel
    if keys[pygame.K_w]:
        yj1 -= vel
    if keys[pygame.K_s]:
        yj1 += vel
    if keys[pygame.K_SPACE]:
        laser.play()
        disparo1=True
        yb1=yj1
        xb1=xj1-32


#________________MOVIMIENTO JUGADOR 2________________#

    if event.type == pygame.JOYAXISMOTION:  # Joystick
        if j.get_axis(0) >= 0.5:
            xj2 += vel            
        if j.get_axis(0) <= -1:
            xj2 -= vel
        if j.get_axis(1) >= 0.5:
            yj2 += vel
        if j.get_axis(1) <= -1:
            yj2 -= vel

    '''if event.type == pygame.JOYBUTTONDOWN:  # Joystick
        if event.button == 0:
            xj2 += vel            
        if event.button == 1:
            xj2 -= vel
        if event.button == 2:
            yj2 += vel
        if event.button == 3:
            yj2 -= vel'''
    if conectado:
	    if event.type == pygame.JOYHATMOTION:  # Joystick
	        if j.get_hat(0) == (1,0):
	            xj2 += vel            
	        if j.get_hat(0) == (-1,0):
	            xj2 -= vel
	        if j.get_hat(0) == (0,-1):
	            yj2 += vel
	        if j.get_hat(0) == (0,1):
	            yj2 -= vel
	    if event.type == pygame.JOYBUTTONDOWN:
	        if event.button == 1:
	            laser.play()
	            disparo2=True
	            yb2=yj2
	            xb2=xj2-32
    else:

	    if keys[pygame.K_j]:
	        xj2 -= vel
	    if keys[pygame.K_l]:
	        xj2 += vel
	    if keys[pygame.K_i]:
	        yj2 -= vel
	    if keys[pygame.K_k]:
	        yj2 += vel
	    if keys[pygame.K_p]:
	        laser.play()
	        disparo2=True
	        yb2=yj2
	        xb2=xj2-32


    win.fill([255, 255, 255])
    
    #repintado del fondo
    BackGround = Background('fondo.jpg', [0,0])
    win.blit(BackGround.image, BackGround.rect)

    

    #incremento posicion del target

    xPos += xVel
    #yPos += yVel
 
    if xPos > 800 or xPos <10:
        xVel *= -1
    
    #if yPos >290 or yPos <10:
        #yVel *= -1

    #target
        
    #nave1 =  pygame.draw.circle(win, pygame.Color('GREEN') ,(xPos+30,yPos-50),60 ) 
        win.blit(nave,(xPos+30,yPos-50))
        vid = myfont.render('ANOTHER',True,(255,255,0))
        win.blit(vid,(10,10))
        #enemilive=True
        #puntos=puntos+50
    if puntos>=0:
        win.blit(nave,(xPos+30,yPos-50))
    else:
        vidaEnemigo = myfont.render('ANOTHER',True,(255,255,0))
        win.blit(vidaEnemigo,(10,10))
        puntos=puntos+50
        



    #Dibujado jugador1
    pygame.draw.rect(win, (255,0,0), (xj1, yj1, width, height))
    #Dibujado jugador2
    pygame.draw.rect(win, (0,0,255), (xj2, yj2, width, height))

    #disparo1
    if disparo1 and yb1>0:
        yb1-=velb        
        #bala = pygame.draw.circle(win, (255,255,255 ),(xb+30,yb),10)
        win.blit(bala,(xb1+30,yb1))
        if puntos >= 0:
            offset=(xb1-xPos,yb1-yPos)
            colision = nave_mask.overlap(bala_mask,offset)
        #print(offset)
    
            if colision:
                print('La bala del jugador 1 le dio')
                puntos=puntos-50
                print(puntos)
                acierta.play()


    if disparo2 and yb2>0:
        yb2-=velb        
        #bala = pygame.draw.circle(win, (255,255,255 ),(xb+30,yb),10)
        win.blit(bala2,(xb2+30,yb2))
        if puntos >= 0:
            offset2=(xb2-xPos,yb2-yPos)
            colision2 = nave_mask.overlap(bala_mask2,offset2)
        #print(offset2)
    
            if colision2:
                print('La bala del jugador 2 le dio')
                puntos=puntos-1
                print(puntos)
                acierta.play()

    Puntaje(puntos)     
    Tiempo()   
    pygame.display.update() 
    pygame.display.flip()

pygame.quit()
