import pygame
pygame.init()

win = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("First Game")

secundario=Tk()

run = True


#player 1
x = 100
y = 100
width = 60
height = 40
vel = 15


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
    
    if keys[pygame.K_s]:
        y += vel

    win.fill((0,0,0))  # Fills the screen with black
    rojito=pygame.draw.rect(win, (255,0,0), (x, y, width, height))   

    pygame.display.update() 
pygame.quit()
