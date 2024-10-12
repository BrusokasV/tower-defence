import pygame
import sys
from pygame.locals import *
from shield import Shield
from sys import exit
from time import sleep
from Enemies import Enemies, populate
import math
enemies_array = []
populate(enemies_array)


# Initialize Pygame
pygame.init()

#set up the display
dimension_x = 1000
dimension_y = 750
x = 0
y = 0
shield_radius = 90
screen = pygame.display.set_mode((dimension_x, dimension_y))
pygame.display.set_caption("Protect the Pumpkin")


shield = Shield((50, 50), shield_radius)
#cursor img
img = pygame.transform.scale(pygame.image.load("cursor.png"), (50, 50))
img.convert()

#ghost img
ghost_img = pygame.transform.scale(pygame.image.load("ghost.png"), (50, 50))
ghost_img.convert()


SPAWNEVENT = pygame.USEREVENT + 1
TICKEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWNEVENT, 2000)
pygame.time.set_timer(TICKEVENT, 10)
enemy_count = 0
flag = False


# titles
title_font = pygame.font.SysFont(None, 72)
rules_font = pygame.font.SysFont(None, 50)
description = pygame.font.SysFont(None, 36)
button_font = pygame.font.SysFont(None, 36)
score_font = pygame.font.SysFont(None, 36)

#main title
title_text = title_font.render("Welcome to Pumpkin Guard!", True, (255, 255, 255))
rules_title_main = title_font.render("Protect the Pumpkin!", True, (255, 255, 255))


#rule titles
rules_title = rules_font.render("Rules:", True, (0, 0, 0))
rules_text = description.render("Use your shield to repel ghosts by facing them and", True, (0, 0, 0))
rules_text2 = description.render("blocking their attacks before they reach the pumpkin", True, (0, 0, 0))
button_text = button_font.render("Start Game!", True, (0, 0, 0))

#pumpkin pic
pumpkin_img = pygame.image.load('halloween-ghost-pumpkin.png')
pumpkin_img = pygame.transform.scale(pumpkin_img, (80, 80))

#locations
pumpkin_pos = [dimension_x // 2, dimension_y // 2]
shield_color = (255, 255, 255)

#hearts pic
heart_img = pygame.image.load('heart.png')
heart_img = pygame.transform.scale(heart_img, (40, 40))
#broken hearts pic
broken_heart_img = pygame.image.load('broken-heart.png')
broken_heart_img = pygame.transform.scale(broken_heart_img, (40, 40))
#death pic
death_img = pygame.image.load('death.png')
death_img = pygame.transform.scale(death_img, (40, 40))





#draw hearts and broken hearts
def draw_lives():
    hearts = 3
    remaining_lives = shield.get_lives()

    for i in range(hearts):
        heart_x = 20 + i * 50
        heart_y = dimension_y - 60

        #frame for hearts
        frame_rect = pygame.Rect(heart_x - 5, heart_y - 5, 50, 50)
        pygame.draw.rect(screen, (0, 0, 0), frame_rect, 3)

        #displaying the type of heart
        if i < remaining_lives:
            screen.blit(heart_img, (heart_x, heart_y))
        else:
            screen.blit(broken_heart_img, (heart_x, heart_y))

#draws our score
def draw_score():

    score_block_width = 200
    score_block_height = 40
    score_block_x = dimension_x - score_block_width - 20
    score_block_y = dimension_y - score_block_height - 20

    #draw a frame for a score
    pygame.draw.rect(screen, (255, 255, 255), (score_block_x, score_block_y, score_block_width, score_block_height))
    pygame.draw.rect(screen, (0, 0, 0), (score_block_x, score_block_y, score_block_width, score_block_height),
                     3)

    score_text = score_font.render(f"Score: {shield.get_score()}", True, (0, 0, 0))
    screen.blit(score_text, (score_block_x + 10, score_block_y + 10))

def game_loop():
    running = True
    global enemy_count, hearts
    pumpkin_radius = 30
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == SPAWNEVENT:
                if (enemy_count<20):
                    enemy_count += 1
            if event.type == TICKEVENT:
                if (shield.get_lives() == 0):
                    print("Game Over!")
                    running = False
                    break

                screen.fill((120, 100, 100))
                screen.blit(rules_title_main, (dimension_x // 2 - rules_title_main.get_width() // 2, 50))
                pygame.draw.circle(screen, shield_color, pumpkin_pos, shield_radius, 2)
                screen.blit(pumpkin_img, (pumpkin_pos[0] - pumpkin_img.get_width() // 2,
                                          pumpkin_pos[1] - pumpkin_img.get_height() // 2))

                draw_lives()
                draw_score()



                x = pygame.mouse.get_pos()[0] - (dimension_x / 2)
                y = pygame.mouse.get_pos()[1] - (dimension_y / 2)
                shield.update_position((x, y))
                x_shield, y_shield = shield.get_position()
                x_shield += (dimension_x / 2) - 25
                y_shield += (dimension_y / 2) - 25

                for i in range(0, enemy_count):
                    if (not enemies_array[i].get_taken_life()):
                        current_enemy = enemies_array[i]
                        enemies_array[i].set_distance(current_enemy.distance - current_enemy.hit)

                        difference_ghost_pumpkin_x = pumpkin_pos[0] - (current_enemy.get_position()[0] + (dimension_x / 2))
                        difference_ghost_pumpkin_y = pumpkin_pos[1] - (current_enemy.get_position()[1] + (dimension_y / 2))
                        distance_from_pumpkin = math.sqrt(difference_ghost_pumpkin_x ** 2 + difference_ghost_pumpkin_y ** 2)

                        if distance_from_pumpkin <= pumpkin_radius and not enemies_array[i].get_taken_life():
                            shield.reduce_lives()
                            print(f"Hearts left: {shield.get_lives()}")
                            enemies_array[i].set_taken_life(True)

                        if (abs(current_enemy.get_distance() - shield.shield_distance)<0.0000001 and  abs(current_enemy.get_angle_pos()-shield.get_angle_pos())<1 and not enemies_array[i].get_taken_life()):
                            enemies_array[i].set_hit(-1)
                            shield.add_score(abs(current_enemy.get_hit()))
                        elif (current_enemy.get_distance()<10):
                            shield.reduce_lives()
                            current_enemy.set_taken_life(True)

                    x_enemy, y_enemy = current_enemy.get_position()
                    screen.blit(ghost_img, (x_enemy + (dimension_x/2) - 25, y_enemy + (dimension_y/2) - 25))
                    if (enemies_array[i].get_hit()<0 and enemies_array[i].get_distance()>700):
                        enemies_array[i].set_hit(-1)
                        print("return")
                # img = pygame.transform.rotate()
                screen.blit(img, (x_shield, y_shield))
            pygame.display.update()


def start_screen():
    while True:
        screen.fill((120, 100, 100)) #main background

        #title
        screen.blit(title_text, (dimension_x // 2 - title_text.get_width() // 2, 50))

        #rules box
        pygame.draw.rect(screen, (198, 89, 33), (100, 200, 800, 300))
        pygame.draw.rect(screen, (0, 0, 0), (100, 200, 800, 300), 3)

        #description of the rules
        screen.blit(rules_title, (dimension_x // 2 - rules_title.get_width() // 2, 230))
        screen.blit(rules_text, (dimension_x // 2 - rules_text.get_width() // 2, 280))
        screen.blit(rules_text2, (dimension_x // 2 - rules_text2.get_width() // 2, 320))

        #start game btn
        button_rect = pygame.Rect(dimension_x // 2 - 150, 400, 300, 75)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
        screen.blit(button_text, (dimension_x // 2 - button_text.get_width() // 2, 425))

        #handing events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

        pygame.display.flip()


start_screen()

game_loop()


