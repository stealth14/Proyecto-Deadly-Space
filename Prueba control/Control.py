import pygame
pygame.init()

def main():
    ventana = pygame.display.set_mode((800,800))
    pygame.display.set_caption('Prueba para Mando')

    fondo = pygame.Surface(ventana.get_size())
    fondo = fondo.convert()
    fondo.fill((255,255,255))

    mandos = []
    reloj = pygame.time.Clock()
    run = True
    #Para el control conectado
    for i in range(0,pygame.joystick.get_count()):
		#Añadir un control a la lista mandos
        mandos.append(pygame.joystick.Joystick(i))
		#Inicializar los mandos detectados
        mandos[-1].init()
		#comprovacion en consola
        print('MANDO DETECTADO -->',mandos[-1].get_name())
    while run:
        reloj.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Saliendo de la aplicacion...')
                run=False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print('Tecla escape presionada')
                run=False
            elif event.type == pygame.KEYDOWN:
                print('Se presiono --> ',event.key)
            elif event.type == pygame.KEYUP:
                print('Se solto --> ',event.key)

            #Comprobacion para el Mando

            #elif event.type ==pygame.JOYAXISMOTION:
                #print('Mando --> ', mandos[event.joy].get_name(), 'axis -->', event.axis, 'Movimineto')
            elif event.type ==pygame.JOYBUTTONDOWN:
                print('Mando --> ', mandos[event.joy].get_name(), 'boton -->', event.button, 'presionado')
                if event.button == 0:
                    fondo.fill((255,0,0))
                elif event.button == 1:
                    fondo.fill((0,0,255))
            elif event.type == pygame.JOYBUTTONUP:
                print('Mando --> ', mandos[event.joy].get_name(), 'boton -->', event.button, 'soltado')
                if event.button == 0:
                    fondo.fill((255,255,255))
                elif event.button == 1:
                    fondo.fill((255,255,255))

            elif event.type == pygame.JOYHATMOTION:
                print('Mando --> ', mandos[event.joy].get_name(), 'hat -->', event.hat, 'movido')

    ventana.blit(fondo, (0,0))
    pygame.display.flip()

main()

