import pygame
import random
import sys
from pygame.locals import *
from shield import Shield
from sys import exit
from time import sleep
from Enemies import Enemies, populate
import math
from sounds import sound, play
enemies_array = populate()


# Initialize Pygame
pygame.init()

#set up the display
dimension_x = 1000
dimension_y = 800
x = 0
y = 0
shield_radius = 80
screen = pygame.display.set_mode((dimension_x, dimension_y))
pygame.display.set_caption("Gourd Guard")
shield = Shield((50, 50), shield_radius)

f = open("high-score.txt", "r")
shield.set_high_score(int(f.read()))
f.close()

#cursor img
shield_dim = 70
img = pygame.transform.scale(pygame.image.load("shield.png"), (shield_dim, shield_dim))
img.convert()

#ghost img
ghost_dim = 80
ghost_img = pygame.transform.scale(pygame.image.load("ghost_white.png"), (ghost_dim, ghost_dim))
ghost_img.convert()


SPAWNEVENT = pygame.USEREVENT + 1
TICKEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWNEVENT, 2000)
pygame.time.set_timer(TICKEVENT, 10)
enemy_count = 0


# fonts
title_font = pygame.font.Font("MidnightMinutes.ttf", 72)
rules_font = pygame.font.Font("HalloweenNight.ttf", 50)
description = pygame.font.Font("HalloweenNight.ttf", 36)
button_font = pygame.font.Font("HalloweenNight.ttf", 36)
score_font = pygame.font.Font("HalloweenNight.ttf", 36)


#main title
title_text = title_font.render("Gourd Guard", True, (255, 255, 255))
rules_title_main = title_font.render("Guard the Pumpkin!", True, (255, 255, 255))


#rule titles
rules_title = rules_font.render("How to play:", True, (0, 0, 0))
rules_text = description.render("Use your shield to repel ghosts by facing them and", True, (0, 0, 0))
rules_text2 = description.render("blocking their attacks before they reach the pumpkin!", True, (0, 0, 0))
button_text = button_font.render("Start Game!", True, (0, 0, 0))

#pumpkin pic
#pumpkin_img = pygame.image.load('halloween-ghost-pumpkin.png')
pumpkin_img = pygame.image.load('pumpkin_pxl.png')
pumpkin_img = pygame.transform.scale(pumpkin_img, (90, 90))

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
#bg
bg_img = pygame.image.load('graveyard.jpg')
bg_img = pygame.transform.scale(bg_img, (dimension_x, dimension_x))




#draw hearts and broken hearts
def draw_lives():
    hearts = 3
    remaining_lives = shield.get_lives()

    for i in range(hearts):
        heart_x = 20 + i * 50
        heart_y = dimension_y - 60

        #frame for hearts
        # frame_rect = pygame.Rect(heart_x - 5, heart_y - 5, 50, 50)
        # pygame.draw.rect(screen, (0, 0, 0), frame_rect, 3)

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
    screen.blit(score_text, (score_block_x + 10, score_block_y))

def game_loop():
    play('1')
    running = True
    global enemy_count
    pumpkin_radius = 30
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == SPAWNEVENT:
                if (enemy_count<20):
                    enemy_count += 1
                    sound('1')
            if event.type == TICKEVENT:
                if (shield.get_lives() == 0):
                    if (shield.get_score() > shield.get_high_score()):
                        shield.update_high_score()
                        f = open("high-score.txt", "w")
                        f.write(str(shield.get_score()))
                        f.close()
                        game_over_screen(True)
                    else:
                        shield.update_high_score()
                        game_over_screen(False)
                    break

                #screen.fill((120, 100, 100))
                screen.blit(bg_img, (0, -(dimension_x - dimension_y)/2))
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

                x_shield += (dimension_x / 2)
                y_shield += (dimension_y / 2)
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


                        #if (abs(current_enemy.get_distance() - shield.shield_distance)<(shield_dim/3 + ghost_dim/3) and abs(current_enemy.get_angle_pos()-shield.get_angle_pos())<0.45 and not enemies_array[i].get_taken_life()):
                        if (math.dist(enemies_array[i].get_position(), shield.get_position())<shield_dim/2):
                            if (current_enemy.get_hit()>0):
                                shield.add_score(abs(current_enemy.get_hit()))
                                enemies_array[i].set_hit(-abs(enemies_array[i].get_hit()))
                                sound('2')
                            
                        elif (current_enemy.get_distance()<10):
                            shield.reduce_lives()
                            current_enemy.set_taken_life(True)

                    x_enemy, y_enemy = current_enemy.get_position()
                    screen.blit(ghost_img, (x_enemy + (dimension_x/2) - ghost_dim/2, y_enemy + (dimension_y/2) - ghost_dim/2))
                    if (enemies_array[i].get_hit()<0 and enemies_array[i].get_distance()>(550 + 100*random.randint(2, 3))):
                        enemies_array[i].set_hit(abs(enemies_array[i].get_hit()))

                cursor = img.copy()
                cursor = pygame.transform.rotate(cursor, shield.angle_position*180/math.pi)
                screen.blit(cursor, (x_shield - cursor.get_width()/2, y_shield - cursor.get_height()/2))
            pygame.display.update()




def game_over_screen(hs_beat):
    popup_width = 400
    popup_height = 300
    popup_x = (dimension_x // 2) - (popup_width // 2)
    popup_y = (dimension_y // 2) - (popup_height // 2)

    while True:
        #screen.fill((120, 100, 100))
        screen.blit(bg_img, (0, -(dimension_x - dimension_y)/2))

        #pop up window
        pygame.draw.rect(screen, (50, 50, 50), (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height), 3)

        #title
        game_over_font = pygame.font.Font("MidnightMinutes.ttf", 70)
        game_over_text = game_over_font.render("Game Over!", True, (255, 255, 255))
        screen.blit(game_over_text, (dimension_x // 2 - game_over_text.get_width() // 2, 50))

        pygame.draw.rect(screen, (198, 89, 33), (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 3)

        #description
        high_score_font = pygame.font.Font("HalloweenNight.ttf", 50)
        current_font = pygame.font.Font("HalloweenNight.ttf", 36)
        if (not hs_beat):
            high_score_text = high_score_font.render(f"High score:{shield.get_high_score()}", True, (0, 0, 0))
            current_score_text = current_font.render(f"Current score:{shield.get_score()}", True, (0, 0, 0))
            screen.blit(high_score_text, (dimension_x // 2 - game_over_text.get_width() // 2 + 25, dimension_y // 3 + 10))
            screen.blit(current_score_text, (dimension_x // 2 - game_over_text.get_width() // 2 + 25, (dimension_y // 3) + 60))
        else:
            new_hs_text = high_score_font.render(f"New High Score: {shield.get_score()}", True, (0, 0, 0))
            screen.blit(new_hs_text, (dimension_x // 2 - game_over_text.get_width() // 2 - 25, 300))

        #restart btn
        button_font = pygame.font.Font("HalloweenNight.ttf", 32)
        button_text = button_font.render("Try Again!", True, (255, 255, 255))
        button_rect = pygame.Rect(popup_x + 50, popup_y + 150, 120, 50)
        pygame.draw.rect(screen, (255, 0, 0), button_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
        screen.blit(button_text, (button_rect.x + (button_rect.width // 2 - button_text.get_width() // 2), button_rect.y + 10))

        #quit btn
        quit_text = button_font.render("Quit", True, (255, 255, 255))
        quit_rect = pygame.Rect(popup_x + popup_width - 170, popup_y + 150, 120, 50)
        pygame.draw.rect(screen, (255, 0, 0), quit_rect)
        pygame.draw.rect(screen, (0, 0, 0), quit_rect, 3)
        screen.blit(quit_text, (quit_rect.x + (quit_rect.width // 2 - quit_text.get_width() // 2), quit_rect.y + 10))

        #functionality for buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    reset_game()
                    return
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()



def reset_game():
    global enemy_count
    enemy_count = 0
    global enemies_array 
    enemies_array = populate()
    shield.reset_state()

def start_screen():
    play('3')
    while True:
        #screen.fill((120, 100, 100)) #main background
        screen.blit(bg_img, (0, -(dimension_x - dimension_y)/2))

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
        screen.blit(button_text, (dimension_x // 2 - button_text.get_width() // 2, 420))

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


