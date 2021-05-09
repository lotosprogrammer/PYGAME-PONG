
import pygame
import math
from random import randint
import time

pygame.init()
pygame.font.init()


WIN_SIZE = (1600, 900)

win = pygame.display.set_mode(WIN_SIZE)
pygame.display.flip()

tk = pygame.time.Clock()

PLAYER_RECT_1 = pygame.Rect(30, 350, 30, 150)   
PLAYER_RECT_2 = pygame.Rect(1540, 350, 30, 150)
BALL_RECT = pygame.Rect(1600/2, 900/2, 30, 30)

winning_side = 0 

speed = -10

player_color = (255, 0, 0)

ball_y_offset = 0
ball_y_offset_mulitplier = 0.05
yOffset = 3
ball_speed = 5 #default is 25 current value is placeholder for testing

def p1():
    
    global PLAYER_RECT_1
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        PLAYER_RECT_1.y += speed
    if keys[pygame.K_s]:
        PLAYER_RECT_1.y -= speed


    if PLAYER_RECT_1.y > 750:
        PLAYER_RECT_1.y = 750
    elif PLAYER_RECT_1.y < 0:
        PLAYER_RECT_1.y = 0


 

    pygame.draw.rect(win, player_color, PLAYER_RECT_1)


def p2():

    global PLAYER_RECT_2

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        PLAYER_RECT_2.y += speed
    if keys[pygame.K_DOWN]:
        PLAYER_RECT_2.y -= speed


    if PLAYER_RECT_2.y > 750:
        PLAYER_RECT_2.y = 750
    elif PLAYER_RECT_2.y < 0:
        PLAYER_RECT_2.y = 0


 


    pygame.draw.rect(win, player_color, PLAYER_RECT_2)


direction  = randint(1, 3)

if direction == 2:
    ball_direction = -1
else:
    ball_direction = 1
def ball():
    global ball_pos
    global ball_direction
    global ball_y_offset
    global BALL_RECT
    global PLAYER_RECT_1
    global PLAYER_RECT_2
    global is_running
    global winning_side

    


    if BALL_RECT.colliderect(PLAYER_RECT_1):
        ball_direction = 1
        ball_y_offset = ((PLAYER_RECT_1.y + PLAYER_RECT_1.h/2) - BALL_RECT.y) * ball_y_offset_mulitplier

    elif BALL_RECT.colliderect(PLAYER_RECT_2):
        ball_direction = -1
        ball_y_offset = ((PLAYER_RECT_2.y + PLAYER_RECT_2.h/2) - BALL_RECT.y) * ball_y_offset_mulitplier

    if BALL_RECT.y < 0:
        ball_y_offset *= -1
    elif BALL_RECT.y > 900 - BALL_RECT.h:
        ball_y_offset *= -1



    BALL_RECT.x += ball_direction * ball_speed
    BALL_RECT.y += ball_y_offset

    if BALL_RECT.x < 0:
        winning_side = 1
        is_running = False
    elif BALL_RECT.x > 1680:
        winning_side = 2
        is_running = False



    pygame.draw.rect(win, (255, 255, 255), BALL_RECT)

    

is_running = True


win.fill((0, 0, 0))


p1()
p2()
ball()


pygame.display.update()

time.sleep(3)

while is_running:
    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            is_running = False

    win.fill((0, 0, 0))


    p1()
    p2()
    ball()


    pygame.display.update()


    tk.tick(60)

if winning_side != 0:
    win.fill((255, 255, 0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    if winning_side == 1:
        textsurface = myfont.render('LEFT SIDE WON!', False, (0, 0, 0))
    elif winning_side == 2:
        textsurface = myfont.render('RIGHT SIDE WON!', False, (0, 0, 0))

    win.blit(textsurface,(1680/2,900/2))
    pygame.display.update()

    time.sleep(5)
