import pygame
from datetime import datetime

pygame.init()
#captura del tiempo inicial
tiempo_inicial=datetime.now()

#Inicializacion Joystick

# Evita que el programa se detega sij no hay un mando conectado
try:
    j = pygame.joystick.Joystick(0) # Crear instancia del Joystick
    j.init() # Inicia el Joystick para usarlo
    print ("Se detecto un mando: {0}".format(j.get_name()))
except pygame.error:
    print ("No hay un mando conectado.")

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("First Game")

#sonidos
laser=pygame.mixer.Sound('laser.wav')
fondo=pygame.mixer.music.load('Song Of Storms Dubstep Remix - Ephixa.mp3')
pygame.mixer.music.play(-1)

run = True


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

disparo=False

#target coordinates

xPos = 50
yPos = 100

xVel = 6
yVel = -1.5

bala = pygame.image.load('mega_man.png').convert_alpha()
bala_mask = pygame.mask.from_surface(bala)
bala_rect = bala.get_rect()

nave = pygame.image.load('nave.png').convert_alpha()
nave_mask = pygame.mask.from_surface(nave)
nave_rect = nave.get_rect()

while run:
    #pausa el programa por una cantidad de tiempo 
    #pygame.time.delay(1)

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
        disparo=True
        yb=yj1
        xb=xj1


#________________MOVIMIENTO JUGADOR 2________________#

    '''if event.type == pygame.JOYAXISMOTION:  # Joystick
        if j.get_axis(0) >= 0.5:
            xj2 += vel            
        if j.get_axis(0) <= -1:
            xj2 -= vel
        if j.get_axis(1) >= 0.5:
            yj2 += vel
        if j.get_axis(1) <= -1:
            yj2 -= vel'''

    '''if event.type == pygame.JOYBUTTONDOWN:  # Joystick
        if event.button == 0:
            xj2 += vel            
        if event.button == 1:
            xj2 -= vel
        if event.button == 2:
            yj2 += vel
        if event.button == 3:
            yj2 -= vel'''

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
            disparo=True
            yb=yj1
            xb=xj1

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


    #Dibujado jugador1
    pygame.draw.rect(win, (255,0,0), (xj1, yj1, width, height))
    #Dibujado jugador2
    pygame.draw.rect(win, (0,0,255), (xj2, yj2, width, height))

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

    pygame.display.update() 
pygame.quit()