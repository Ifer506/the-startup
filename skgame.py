import pygame
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 500))
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

font = pygame.font.SysFont('ARCADECLASSIC.TTF', 35)


def plot_snk(screen, color, snk_list, snk_width, snk_height):
    for i in snk_list:
        pygame.draw.rect(screen, (244, 164, 96), (i[ 0 ], i[ 1 ], 20, 20))

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


def Intro():
    music()
    intro = pygame.image.load('Background.jpg')

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
        click = pygame.mouse.get_pressed(3)
        # print(mouse)

        if mouse[0] > 352 and mouse[0] < 451 and 364 < mouse[1] < 403:
            show_score('START', green, 361, 372)
            if click == (1, 0, 0):
                game_loop()

        if 298 < mouse[0] < 501 and mouse[1] > 425 and mouse[1] < 463:
            show_score('INSTRUCTIONS', green, 308, 433)
            if click == (1, 0, 0):
                instruction()

        pygame.display.update()


def High_score():
    with open("highscore.txt", "r") as hs:
        return hs.read()


def game_loop():
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
            show_score(str(score), green, 660, 7)

            if highscore < score:
                highscore = score
            with open("highscore.txt", "w") as f:
                f.write("Highscore = " + str(highscore))
            show_score(str(highscore), green, 155, 7)
            pygame.display.update()

        clock.tick(400)
        pygame.display.update()


Intro()
pygame.quit()
quit()
