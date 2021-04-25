import pygame
pygame.init()

win = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("First Game")


run = True


#player 1
x = 500
y = 500
width = 60
height = 40
vel = 15

#bala

velb=10

disparo=False

#target coordinates

xPos = 50
yPos = 100

xVel = 5
yVel = -2.5

bala = pygame.image.load('mega_man.png').convert_alpha()
bala_mask = pygame.mask.from_surface(bala)
bala_rect = bala.get_rect()

nave = pygame.image.load('nave.png').convert_alpha()
nave_mask = pygame.mask.from_surface(nave)
nave_rect = nave.get_rect()

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
 
    if xPos > 1150 or xPos <10:
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
        offset=(xb+30,yb)
        colision = nave_mask.overlap(bala_mask,offset)
        print(offset)
    
        if colision:
            print('La bala le dio')

    pygame.display.update() 
pygame.quit()