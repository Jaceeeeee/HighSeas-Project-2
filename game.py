import pygame
import sys
import math
import random
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((1000,800))

def do():
    pygame.display.set_caption('Reaction Speed Test')
    clock = pygame.time.Clock()

    circle_pos = (1000/2, 800/2)

    nicecolour = "#808080"

    plunger_cursor = pygame.image.load("Plunger.png")
    plunger_cursor = pygame.transform.scale(plunger_cursor, (50, 50))


    def check_circle_collision() -> bool:
        mouse_pos = pygame.mouse.get_pos()

        if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <= 120:
            return True
        return False

    def check_start_collision() -> bool:
        mouse_pos = pygame.mouse.get_pos()
        return buttonx-150<mouse_pos[0]<buttonx+150 and buttony-50<mouse_pos[1]<buttony+50

    def check_start_collision() -> bool:
        mouse_pos = pygame.mouse.get_pos()
        return buttonx-150<mouse_pos[0]<buttonx+150 and buttony-50<mouse_pos[1]<buttony+50

    button1 = pygame.image.load('REALPRESSME.png')
    button1 = pygame.transform.scale(button1, (100,100))

    button2 = pygame.image.load('STARTUPBUTTON.png')
    button2 = pygame.transform.scale(button2, (300,100))

    circlex= -200
    circley= -200

    buttonx = 550
    buttony = 400

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
    started = False
    ended_time = 0
    while True:
        print(ended_time)
        if ended_time > 0:
            ended_time += 0.06
        if ended_time >= 10:
            return
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #THIS IS LEFT CLICK
                    if check_start_collision():
                        started = True
                        buttonx = -1000
                        buttony = -1000
                    if check_circle_collision() and started:
                        clicks += 1
                        screen.fill('gray')
                        pygame.draw.circle(screen, "darkgreen", (circlex, circley), 60)
                        screen.blit(button1,(circlex, circley))
                        circlex= (random.randint(0,900))
                        circley= (random.randint(0,700))
                        circle_pos = (circlex, circley)
                        if clicks == 16:
                            print("clear")
                            unaverage = time_taken/15 #secs per click
                            average = round(unaverage, 3)
                            ended_time += 0.06

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
        if started:
            time_taken += 1/60
        screen.fill(nicecolour)
        screen.blit(text, text_rect)
        screen.blit(secondtext, secondtext_rect)
        screen.blit(thirdtext, thirdtext_rect)
        #pygame.draw.circle(screen, 'green', (circlex, circley), 60)
        screen.blit(button1,(circlex, circley))
        screen.blit(button2,(buttonx-216.5, buttony-85))
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(plunger_cursor, (mouse_pos[0]-15, mouse_pos[1]-35))
        pygame.mouse.set_visible(False)

        pygame.display.update()

while True:
    do()
