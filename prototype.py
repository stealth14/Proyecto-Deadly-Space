import pygame
pygame.init()

win = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("First Game")


run = True


#player 1
x = 100
y = 100
width = 60
height = 40
vel = 15

#bala

velb=10

disparo=False

#probando sourcetree denuevo
    
#probando sourcetree
while run:
    #pausa el programa por una cantidad de tiempo 
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x -= vel
        xb=x
    if keys[pygame.K_d]:
        x += vel
        xb=x
    if keys[pygame.K_w]:
        y -= vel
        yb=y
    if keys[pygame.K_s]:
        y += vel
        yb=y
    if keys[pygame.K_SPACE]:
        disparo=True
    

    win.fill((0,0,0))

    
    

    pygame.draw.rect(win, (255,0,0), (x, y, width, height))

    if disparo and yb>0:
        yb-=velb
        pygame.draw.circle(win, (255,255,255 ),(xb,yb),10)
        
    pygame.display.update() 
pygame.quit()
