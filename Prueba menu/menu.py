import pygame
from pygame.locals import *
import os
pygame.init()
 
# Centrar en la pantalla la ventana
os.environ['SDL_VIDEO_CENTERED'] = '1'
 

screen_width=1000
screen_height=700
screen=pygame.display.set_mode((screen_width, screen_height))

def formato(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
 
# Colores
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)

 
# Fuente de letra
font = "DroidSans.ttf"

def main_menu():
 
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="score"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        pygame.quit()                        
                        os.system("python menu_jugadores.py")
                        quit()

                    if selected=="score":
                        pygame.quit()
                        quit()

        screen.fill(gray)
        title=formato("DeadlySpace MASTER", font, 90, white)
        if selected=="start":
            text_start=formato("START", font, 80, white)
        else:
            text_start = formato("START", font, 80, black)
        if selected=="score":
            text_score=formato("SCORE", font, 80, white)
        else:
            text_score = formato("SCORE", font, 80, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        score_rect=text_score.get_rect()
 
       
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_score, (screen_width/2 - (score_rect[2]/2), 400))
        pygame.display.update()
        

main_menu()
pygame.quit()
quit()