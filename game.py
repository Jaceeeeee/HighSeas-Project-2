import pygame
import sys
import math
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,800))

pygame.display.set_caption('Reaction Speed Test')
clock = pygame.time.Clock()

circle_pos = (1000/2, 800/2)

nicecolour = "#808080"


def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <= 60:
        return True
    return False

button1 = pygame.image.load('REALPRESSME.png')
button1 = pygame.transform.scale(button1, (330,330))

circlex= (1000/2)
circley= (800/2)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('', True, (0, 0, 0), (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (100, 100)

secondtext = font.render('', True, (0, 0, 0), (255, 255, 255))
secondtext_rect = secondtext.get_rect()
secondtext_rect.center = (150, 150)

thirdtext = font.render('', True, (0, 0, 0))
thirdtext_rect = thirdtext.get_rect()
thirdtext_rect.center = (500, 375)


startup_img = pygame.image.load('STARTUPBUTTON.png').convert_alpha()




clicks = 0
time_taken = 0
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #THIS IS LEFT CLICK
                if check_circle_collision():
                    clicks += 1
                    screen.fill('gray')
                    pygame.draw.circle(screen, "darkgreen", (circlex, circley), 60)
                    screen.blit(button1,(circlex-63, circley-64))
                    circlex= (random.randint(0,1000))
                    circley= (random.randint(0,800))
                    circle_pos = (circlex, circley)
                    if clicks == 15:
                        print("clear")
                        unaverage = time_taken/15 #secs per click
                        average = round(unaverage, 3)
                      

                        #display the average#
                        #hide the circle
                        circlex = -100
                        circley = -100
                        font = pygame.font.Font('freesansbold.ttf', 32)
                        clear = '#00000000'
                        text = font.render(str(average), True, (0, 0, 0))
                        text_rect = text.get_rect()
                        text_rect.center = (430, 400)

                        messageto = "Your average reaction speed is... "

                        secondtext = font.render(str(messageto), True, (0, 0, 0))
                        secondtext_rect = secondtext.get_rect()
                        secondtext_rect.center = (500, 375)

                        secs = "seconds!"

                        thirdtext = font.render(str(secs), True, (0, 0, 0))
                        thirdtext_rect = thirdtext.get_rect()
                        thirdtext_rect.center = (545, 400)

                        

    clock.tick(60)
    time_taken += 1/60
    screen.fill(nicecolour)
    screen.blit(text, text_rect)
    screen.blit(secondtext, secondtext_rect)
    screen.blit(thirdtext, thirdtext_rect)
    #pygame.draw.circle(screen, 'green', (circlex, circley), 60)
    screen.blit(button1,(circlex-216.5, circley-85))
    

    pygame.display.update()

