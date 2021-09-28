import pygame
import random
import time
from pygame import mixer
from pygame import mouse
pygame.init()

screen = pygame.display.set_mode(((800, 500)))
pygame.display.set_caption('Sarpa khel')

clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 200, 0)
dgreen = (0, 55, 65)

current_time = 0
game_time = 0

global ti,s
ti = 10000
s= 2

game_font = pygame.font.Font('ARCADECLASSIC.TTF', 28)
font = game_font


def plot_snk(screen, color, snk_list, snk_width, snk_height):
    for i in snk_list:
        pygame.draw.rect(screen, (244,164,96), (i[0], i[1], 20, 20))




def show_score(text, color, x, y):
    score = font.render(text, True, color)
    screen.blit(score, (x, y))

def music():
    mixer.init()
    mixer.music.load('shee.wav')
    mixer.music.set_volume(0.7)
    mixer.music.play()


def instruction():
    Instruction_img = pygame.image.load('greeen.png')
    up = pygame.image.load('up3.png')
    down = pygame.image.load('down3.png')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        screen.blit(Instruction_img, (0, 0))

        screen.blit(up, (161, 307))
        screen.blit(down, (161, 380))

        screen.blit(up, (420, 307))
        screen.blit(down, (420, 380))

        current_time = pygame.time.get_ticks()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)

        global ti,s


        if mouse[0] > 161 and mouse[0] < 190 and mouse[1] > 307 and mouse[1] < 338:
            screen.blit(up,(161, 307))
            if click == (1, 0, 0):
                print('high')
                ti =ti + 2500
                print(ti)


        if mouse[0] > 161 and mouse[0] < 192 and mouse[1] > 380 and mouse[1] < 408:
            screen.blit(down, (161, 380))
            if click == (1, 0, 0):
                print('down ')
                if ti<0:
                    ti = ti
                elif ti>0:
                    ti = ti - 2500
                print(ti)

        if mouse[0] > 421 and mouse[0] < 451 and mouse[1] > 312 and mouse[1] < 328:
            screen.blit(up, (420, 312))
            if click == (1, 0, 0):
                print('nex up')
                s += 1

        if mouse[0] > 420and mouse[0] < 451 and mouse[1] > 380 and mouse[1] < 409:
            screen.blit(down, (420, 380))
            if click == (1, 0, 0):
                print('nex down')
                if s < 0:
                    s = s
                elif s > 0:
                    s = s - 1

        pygame.draw.rect(screen, white, (151, 339, 50, 38))
        show_score(str(ti//1000), dgreen, 164, 347)

        pygame.draw.rect(screen, white, (409, 339, 50, 38))
        show_score(str(s), dgreen, 422, 347)

        clock.tick(8)
        pygame.display.update()


def Intro():
    music()
    intro = pygame.image.load('snake_back_1.png')


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        screen.blit(intro, (0, 0))
        pygame.draw.rect(screen, dgreen, (352, 364, 100, 40))
        show_score('START', white, 361, 372)

        pygame.draw.rect(screen, dgreen, (298, 424, 205, 40))
        show_score('INSTRUCTIONS', white, 308, 433)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(mouse)

        if 320 < mouse[0] < 470 and 344 < mouse[1] < 384:
            show_score('START', white, font, 361, 350)
            if click == (1, 0, 0):
                game_loop()

        if mouse[0] > 298 and mouse[0] < 501 and mouse[1] > 425 and mouse[1] < 463:
            show_score('INSTRUCTIONS', green, 308, 433)
            if click == (1, 0, 0):
                instruction()

        pygame.display.update()


def game_loop():
    mixer.music.stop()
    gam = mixer.Sound('gamesound.wav')
    gam.play()

    snk = pygame.image.load('snake head.png')
    snk_x = 100
    snk_y = 100
    snk_xchange = 0
    snk_ychange = 0
    snk_list = []
    snk_length = 50

    score = 0
    game_over = False

    food = pygame.image.load('mouse.png')
    food_x = 400
    food_y = 300
    food_xchange = 0
    food_ychange = 0
    game_time = pygame.time.get_ticks()

    run = True

    while run:

        if game_over:
            screen.fill(black)
            gam.stop()
            if score >= s:
                snakewin = pygame.image.load('snakewin.png')
                screen.blit(snakewin, (0, 0))
                mixer.music.load('hiss.wav')
                mixer.music.play()

            else:
                trump = mixer.Sound('trumpet.wav')
                trump.play(1)
                mousewin = pygame.image.load('mousewin.png')
                screen.blit(mousewin, (0, 0))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mixer.music.stop()
                    trump.stop()
                    run = False
                if event.type == pygame.KEYDOWN:
                    trump.stop()
                    mixer.music.stop()
                    if event.key == pygame.K_RETURN:
                        run = False
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        run = False

        else:
            background = pygame.image.load('Back.png')
            screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    gam.stop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        gam.stop()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:

                        snk_ychange = 0
                        snk_xchange = 1
                    if event.key == pygame.K_LEFT:
                        snk_ychange = 0
                        snk_xchange = -1
                    if event.key == pygame.K_DOWN:
                        snk_xchange = 0
                        snk_ychange = 1
                    if event.key == pygame.K_UP:
                        snk_xchange = 0
                        snk_ychange = -1

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_d:
                        food = pygame.image.load('mouse.png')
                        food_ychange = 0
                        food_xchange = 1
                    if event.key == pygame.K_a:
                        food = pygame.image.load('mousele.png')
                        food_ychange = 0
                        food_xchange = -1
                    if event.key == pygame.K_s:
                        food = pygame.image.load('mousedow.png')
                        food_xchange = 0
                        food_ychange = 1
                    if event.key == pygame.K_w:
                        food = pygame.image.load('mouseup.png')
                        food_xchange = 0
                        food_ychange = -1

            if snk_x < 0:
                snk_x = 800
            if snk_x > 800:
                snk_x = 0

            if snk_y < 37:
                snk_y = 500
            if snk_y > 500:
                snk_y = 37

            # movement of snake
            snk_x += snk_xchange
            snk_y += snk_ychange

            # for food boudary
            if food_x < 0:
                food_x = 800
            if food_x > 800:
                food_x = 0

            if food_y < 37:
                food_y = 500
            if food_y > 500:
                food_y = 37

            food_x += food_xchange
            food_y += food_ychange

            # snake length increase

            body = []
            body.append(snk_x)
            body.append(snk_y)
            snk_list.append(body)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # food interaction
            if abs(snk_x - food_x) < 23 and abs(snk_y - food_y) < 20:
                eat = mixer.Sound('gulp1.wav')
                eat.play()
                score += 1
                snk_length += 50
                food_x = random.randint(20, 780)
                food_y = random.randint(20, 480)

                if score >= s:
                    game_over = True

            current_time = pygame.time.get_ticks()


            if (current_time - game_time) > ti:
                a = (current_time - game_time)
                game_time = 0
                current_time = 0
                if a / 1000 == 2.0 or 4.0 or 6.0 or 8 or 10.0:
                    snk_length += 50
                print(pygame.time.get_ticks())
                game_over = True

            screen.blit(food, (food_x, food_y, 8, 8))
            pygame.draw.rect(screen, yellow, (snk_x, snk_y, 20, 20))
            plot_snk(screen, black, snk_list, 20, 20)
            show_score(str(s), green, 100, 6)
            show_score(str((current_time - game_time) / 1000), green, 686, 6)

        clock.tick(900)
        pygame.display.update()

Intro()
pygame.quit()
quit()
