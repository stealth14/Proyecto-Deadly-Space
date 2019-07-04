import pygame
pygame.init()

win = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("First Game")


run = True
#sonidos
laser=pygame.mixer.Sound('laser.wav')
fondo=pygame.mixer.music.load('Song Of Storms Dubstep Remix - Ephixa.mp3')

pygame.mixer.music.play(-1)
#player 1
x = 500
y = 500
width = 60
height = 40
vel = 15

#bala

velb=20

disparo=False

#target coordinates

xPos = 50
yPos = 100

xVel = 10
yVel = -5
    
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
        laser.play()
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
        
    pygame.draw.polygon(win, pygame.Color('GREEN') , [ (xPos,yPos-50)  , (xPos+50,yPos) , (xPos+50,yPos-50) ] ) 


    #jugador1
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))


    #disparo
    if disparo and yb>0:
        yb-=velb
        pygame.draw.circle(win, (255,255,255 ),(xb+30,yb),10)
      
    

    pygame.display.update() 
pygame.quit()
