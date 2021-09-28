import pygame
import random
from sys import exit
from pygame import mixer

# initializing pygame
pygame.init()
resolution = (800, 500)
screen = pygame.display.set_mode(resolution)

# setting up icon
icon = pygame.image.load("snake_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Snake Game ")

font = pygame.font.SysFont("times", 20)
Kristen = pygame.font.SysFont("Kristen ITC", 40)
Kristen_30 = pygame.font.SysFont("Kristen ITC", 30)
Comic_sans = pygame.font.SysFont("Comic Sans MS", 40)
Comic_sans_20 = pygame.font.SysFont("Comic Sans MS", 20)
digit = pygame.font.Font("digital-7 (mono).ttf", 28)

clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
orange = (255, 175, 10)
gray = (132, 132, 130)
green = (0, 200, 0)
dgreen = (0, 55, 65)
current_time = 0
game_time = 0

global ti, s
ti = 10000
s = 2


def show_score(text, color, font, x, y):
    score = font.render(text, True, color)
    screen.blit(score, (x, y))

def music():
    mixer.init()
    mixer.music.load('shee.wav')
    mixer.music.set_volume(0.7)
    mixer.music.play()


def classic_mode():
    intro_image = pygame.image.load("snake_back_1.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit()

        screen.blit(intro_image, (0, 0,))
        pygame.draw.rect(screen, red, (320, 344, 150, 40))
        show_score('START', black, Comic_sans_20, 361, 350)

        pygame.draw.rect(screen, red, (285, 424, 220, 40))
        show_score('INSTRUCTION', black, Comic_sans_20, 320, 430)

        pygame.draw.rect(screen, red, (700, 20, 80, 35))
        show_score("Back", black, Comic_sans_20, 715, 22)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        if 320 < mouse[0] < 470 and 344 < mouse[1] < 384:
            show_score('START', white, Comic_sans_20, 361, 350)
            if click == (1, 0, 0):
                print("hello")
                CLASSIC()

        if 285 < mouse[0] < 505 and 424 < mouse[1] < 464:
            show_score('INSTRUCTION', white, Comic_sans_20, 320, 430)
            if click == (1, 0, 0):
                print("helko")
                instruction()

        if 700 < mouse[0] < 780 and 20 < mouse[1] < 55:
            show_score("Back", white, Comic_sans_20, 715, 22)
            if click == (1, 0, 0):
                running = False
                pygame.display.update()

        pygame.display.update()


def one_vs_one():
    intro_image = pygame.image.load("snake_back_1.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit()

        screen.blit(intro_image, (0, 0,))
        pygame.draw.rect(screen, red, (320, 344, 150, 40))
        show_score('START', black, Comic_sans_20, 361, 350)

        pygame.draw.rect(screen, red, (285, 424, 220, 40))
        show_score('INSTRUCTION', black, Comic_sans_20, 320, 430)

        pygame.draw.rect(screen, red, (700, 20, 80, 35))
        show_score("Back", black, Comic_sans_20, 715, 22)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        if 320 < mouse[0] < 470 and 344 < mouse[1] < 384:
            show_score('START', white, Comic_sans_20, 361, 350)
            if click == (1, 0, 0):
                print("hello")
                game_loop()

        if 285 < mouse[0] < 505 and 424 < mouse[1] < 464:
            show_score('INSTRUCTION', white, Comic_sans_20, 320, 430)
            if click == (1, 0, 0):
                print("hello")
                Instruction()

        if 700 < mouse[0] < 780 and 20 < mouse[1] < 55:
            show_score("Back", white, Comic_sans_20, 715, 22)
            if click == (1, 0, 0):
                running = False
                pygame.display.update()

        pygame.display.update()


def game_exit():
    image = pygame.image.load("message_box.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(image, (0, 0))
        pygame.draw.rect(screen, red, (270, 300, 100, 40))
        show_score("Yes", black, Comic_sans_20, 300, 305)

        pygame.draw.rect(screen, red, (440, 300, 100, 40))
        show_score("No", black, Comic_sans_20, 480, 305)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        if 270 < mouse[0] < 370 and 300 < mouse[1] < 340:
            show_score("Yes", white, Comic_sans_20, 300, 305)
            if click == (1, 0, 0):
                pygame.quit()
                exit()

        if 440 < mouse[0] < 550 and 300 < mouse[1] < 340:
            show_score("No", white, Comic_sans_20, 480, 305)
            if click == (1, 0, 0):
                running = False

        pygame.display.update()


def intro_page():
    music()
    image = pygame.image.load("blank.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit()
        screen.blit(image, (0, 0))

        show_score("Select Mode", white, Kristen, 270, 80)
        pygame.draw.rect(screen, red, (300, 200, 200, 65))
        show_score('1v1', black, Comic_sans, 370, 200)

        pygame.draw.rect(screen, red, (300, 340, 200, 65))
        show_score("Classic", black, Comic_sans, 337, 340)

        pygame.draw.rect(screen, red, (690, 440, 90, 45))
        show_score("About", black, font, 710, 450)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        if 300 < mouse[0] < 500 and 200 < mouse[1] < 265:
            show_score("1v1", white, Comic_sans, 370, 200)
            if click == (1, 0, 0):
                one_vs_one()

        if 290 < mouse[0] < 501 and 340 < mouse[1] < 405:
            show_score("Classic", white, Comic_sans, 337, 340)
            if click == (1, 0, 0):
                classic_mode()

        if 700 < mouse[0] < 780 and 440 < mouse[1] < 480:
            show_score("About", white, font, 710, 450)
            if click == (1, 0, 0):
                about()
        pygame.display.update()


def Intro():
    intro_image = pygame.image.load("wallpaper.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(intro_image, (0, 1))
        show_score('Press ANYWHERE on the screen', red, font, 260, 450)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        if 0 < mouse[0] < 801 and 0 < mouse[1] < 801:
            if click == (1, 0, 0):
                intro_page()

        pygame.display.update()


def about():
    image = pygame.image.load("about.png")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        screen.blit(image, (0, 0))
        pygame.display.update()

def High_score():
    with open("highscore.txt", "r") as hs:
        return hs.read()


def instruction():
    Instruction_img = pygame.image.load('greeen.png')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        screen.blit(Instruction_img, (0, 0))

        pygame.draw.rect(screen, black, (198, 331, 50, 38))
        pygame.draw.rect(screen, black, (198, 407, 50, 38))

        current_time = pygame.time.get_ticks()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        pygame.display.update()


def Instruction():
    Instruction_img = pygame.image.load('greeen.png')
    up = pygame.image.load('up3.png')
    down = pygame.image.load('down3.png')
    up2 = pygame.image.load('up2.png')
    down2 = pygame.image.load('down2.png')

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

        global ti, s

        if mouse[0] > 161 and mouse[0] < 190 and mouse[1] > 307 and mouse[1] < 338:
            if click == (1, 0, 0):
                screen.blit(up2, (161, 307))
                print('high')
                ti = ti + 2500
                print(ti)

        if mouse[0] > 161 and mouse[0] < 192 and mouse[1] > 380 and mouse[1] < 408:
            screen.blit(down, (161, 380))
            if click == (1, 0, 0):
                screen.blit(down2, (161, 380))
                print('down ')
                if ti < 0:
                    ti = ti
                elif ti > 0:
                    ti = ti - 2500
                print(ti)

        if mouse[0] > 420 and mouse[0] < 451 and mouse[1] > 307 and mouse[1] < 328:
            if click == (1, 0, 0):
                screen.blit(up2, (420, 307))
                print('nex up')
                s += 1

        if mouse[0] > 420 and mouse[0] < 451 and mouse[1] > 380 and mouse[1] < 409:
            if click == (1, 0, 0):
                screen.blit(down2, (420, 380))
                print('nex down')
                if s < 0:
                    s = s
                elif s > 0:
                    s = s - 1

        pygame.draw.rect(screen, white, (151, 339, 50, 38))
        show_score(str(ti // 1000), dgreen,digit, 164, 347)

        pygame.draw.rect(screen, white, (409, 339, 50, 38))
        show_score(str(s), dgreen,digit, 422, 347)

        clock.tick(8)
        pygame.display.update()


def plot_snk(screen, color, snk_list, snk_width, snk_height):
    for i in snk_list:
        pygame.draw.rect(screen, (244,164,96), (i[0], i[1], 20, 20))


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
                sap = mixer.Sound('hiss.wav')
                sap.play()

            else:
                mousewin = pygame.image.load('mousewin.png')
                screen.blit(mousewin, (0, 0))
                trump = mixer.Sound('trumpet.wav')
                trump.play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mixer.music.stop()
                    trump.stop()
                    sap.stop()
                    run = False
                if event.type == pygame.KEYDOWN:
                    mixer.music.stop()
                    trump.stop()
                    sap.stop()
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
            show_score(str(s), green,digit, 100, 6)
            show_score(str((current_time - game_time) / 1000), green,digit, 686, 6)

        clock.tick(400)
        pygame.display.update()

def CLASSIC():
    mixer.music.stop()
    gam = mixer.Sound('gamesound.wav')
    gam.play(-1)


    snk_x = 100
    snk_y = 100
    snk_xchange = 0
    snk_ychange = 0
    snk_list = []
    snk_length = 50

    score = 0
    game_over = False

    try:
        highscore = int(High_score())
    except:
        highscore = 0

    foods = [ 'apple.png', 'mouse.png', 'mouse4.png']
    food = pygame.image.load(random.choice(foods))

    food_x = 400
    food_y = 300

    global border

    run = True

    while run:
        if game_over:
            gam.stop()
            over = mixer.Sound('dead (2).wav')
            over.play()
            with open("highscore.txt", "w") as hs:
                hs.write(str(highscore))

            gg = pygame.image.load('GG.png')
            screen.blit(gg,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    over.stop()
                    run = False
                if event.type == pygame.KEYDOWN:
                    over.stop()
                    if event.key == pygame.K_RETURN:
                        run = False
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        gam.stop()
                        run = False

        else:

            # screen.fill((32, 32, 32))
            back = pygame.image.load('Back2.png')
            screen.blit(back,(0,0))
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

            if snk_x < 0:
                game_over = True
            if snk_x > 800:
                game_over = True

            if snk_y < 0:
                snk_y = 30
                game_over = True
            if snk_y > 500:
                snk_y = 470
                game_over = True

            # movement of snake
            snk_x += snk_xchange
            snk_y += snk_ychange

            # snake length increase

            body = []
            body.append(snk_x)
            body.append(snk_y)
            snk_list.append(body)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # food interaction
            if abs(snk_x-food_x) < 23 and abs(snk_y-food_y) < 20:
                eat = mixer.Sound('gulp1.wav')
                eat.play()
                score += 1
                snk_length += 30
                food = pygame.image.load(random.choice(foods))
                food_x = random.randint(20, 780)
                food_y = random.randint(20, 480)

                if score > int(highscore):
                    highscore = score

            screen.blit(food, (food_x, food_y, 8, 8))
            pygame.draw.rect(screen, yellow, (snk_x, snk_y, 20, 20))
            plot_snk(screen, black, snk_list, 20, 20)
            show_score(str(score), green,digit, 660, 7)

            if highscore < score:
                highscore = score
            with open("highscore.txt", "w") as f:
                f.write("Highscore = " + str(highscore))
            show_score(str(highscore), green,digit, 155, 7)
            pygame.display.update()

        clock.tick(400)
        pygame.display.update()

Intro()
pygame.quit()
quit()
