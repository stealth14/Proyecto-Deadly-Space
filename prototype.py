import pygame
from datetime import datetime

pygame.init()
#captura del tiempo inicial
tiempo_inicial=datetime.now()

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
#player 1
x = 400
y = 500
width = 50
height = 50
vel = 25

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
        
        laser.play()
        
        disparo=True
        yb=y
        xb=x

    #repintado del fondi
    BackGround = Background('fondo.jpg', [0,0])

    win.fill([255, 255, 255])

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

    pygame.display.update() 
pygame.quit()