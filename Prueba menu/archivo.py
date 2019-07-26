import pygame
from pygame.locals import *
import os
pygame.init()
 
# Centrar en la pantalla la ventana
os.environ['SDL_VIDEO_CENTERED'] = '1'

screen_width=1000
screen_height=700
screen=pygame.display.set_mode((screen_width, screen_height))

pygame.mixer.music.set_volume(0.9) 
pygame.mixer.music.load("fondo.mp3")
pygame.mixer.music.play(0, 0.0)

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
 
        #LEE EL PUNTAJE GUARDADO"
    menu=True
    while menu:
        archivo=open("Puntajes_1jugador.txt","r")
        lines=archivo.readlines() 
        screen.fill(gray)
        title=formato("Puntaje anterior", font, 90, white)        
        text_score=formato(str(lines), font, 80, white)       
 
        title_rect=title.get_rect()
        score_rect=text_score.get_rect()
       
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_score, (screen_width/2 - (score_rect[2]/2), 300))
        pygame.display.update()
        
main_menu()
pygame.display.quit()
pygame.quit()
sys.exit()

