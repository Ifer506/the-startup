import pygame
import random
import time

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



def plot_snk(screen, color, snk_list, snk_width, snk_height):
    for i in snk_list:
        pygame.draw.rect(screen, black, (i[0], i[1], 20, 20))


font = pygame.font.SysFont('Monaco', 35)


def show_score(text, color, x, y):
    score = font.render(text, True, color)
    screen.blit(score, (x, y))

# def instruction():
#     Instruction_img = pygame.image.load('')
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#         screen.blit(, (0, 0))



def Intro():
    intro = pygame.image.load('Background.jpg')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(intro, (0, 0))
        pygame.draw.rect(screen, dgreen, (352, 364, 100, 40))
        show_score('START', white, 361, 372)

        pygame.draw.rect(screen, dgreen, (298, 424, 205, 40))
        show_score('INSTRUCTIONS', white, 308, 433)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(mouse)

        if mouse[0] > 352 and mouse[0] < 451 and mouse[1] > 364 and mouse[1] < 403:
            show_score('START', green, 361, 372)
            if click == (1, 0, 0):
                game_time = pygame.time.get_ticks()
                game_loop()

        if mouse[0] > 298 and mouse[0] < 501 and mouse[1] > 425 and mouse[1] < 463:
            show_score('INSTRUCTIONS', green, 308, 433)
            # if click == (1, 0, 0):

                # instruction()

        pygame.display.update()


def game_loop():
    snk_x = 100
    snk_y = 100
    snk_xchange = 0
    snk_ychange = 0
    snk_list = []
    snk_length = 3

    score = 0
    game_over = False

    food = pygame.image.load('fmouse.png')
    food_x = 400
    food_y = 300
    food_xchange = 0
    food_ychange = 0

    run = True

    while run:
        if game_over:
            screen.fill(black)

            show_score('Game over !!press enter to continue or esc to quit', red, 20, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    a = 0
                    if event.key == pygame.K_RETURN:
                        print(f"a is here {a}")
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        run = False

        else:

            screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

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
                        food_ychange = 0
                        food_xchange = 1
                    if event.key == pygame.K_a:
                        food_ychange = 0
                        food_xchange = -1
                    if event.key == pygame.K_s:
                        food_xchange = 0
                        food_ychange = 1
                    if event.key == pygame.K_w:
                        food_xchange = 0
                        food_ychange = -1

            if snk_x < 0:
                snk_x = 800
            if snk_x > 800:
                snk_x = 0

            if snk_y < 0:
                snk_y = 500
            if snk_y > 500:
                snk_y = 0

            # movement of snake
            snk_x += snk_xchange
            snk_y += snk_ychange



            # for food boudary
            if food_x < 0:
                food_x = 800
            if food_x > 800:
                food_x = 0

            if food_y < 0:
                food_y = 500
            if food_y > 500:
                food_y = 0

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
                score += 1
                snk_length += 7
                food_x = random.randint(20, 780)
                food_y = random.randint(20, 480)



            current_time = pygame.time.get_ticks()

            a = (current_time - game_time)
            if a > 6000:
                print(a)
                game_over = True


            screen.blit(food, (food_x, food_y, 8, 8))
            pygame.draw.rect(screen, yellow, (snk_x, snk_y, 20, 20))
            plot_snk(screen, yellow, snk_list, 20, 20)
            show_score('Score: ' + str(score), green, 630, 20)
            show_score('Timer: ' + str(a), green, 630, 40)

            clock.tick(400)
        pygame.display.update()


Intro()
pygame.quit()
quit()
