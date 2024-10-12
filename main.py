import pygame
from pygame.locals import *
from shield import Shield
from sys import exit
from time import sleep
from Enemies import Enemies, populate
enemies_array = []
populate(enemies_array)


pygame.init()
dimension_x = 1000
dimension_y = 750
x = 0
y = 0
screen = pygame.display.set_mode((dimension_x, dimension_y))
shield = Shield((50, 50))
img = pygame.transform.scale(pygame.image.load("cursor.png"), (50,50))
img.convert()
SPAWNEVENT = pygame.USEREVENT + 1
TICKEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWNEVENT, 1000)
pygame.time.set_timer(TICKEVENT, 10)
enemy_count = 0
flag = False
screen.fill((255, 255, 255))

while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            exit()
        if event.type == SPAWNEVENT:
            enemy_count += 1
        if event.type == TICKEVENT:
            screen.fill((255, 255, 255))
            x = pygame.mouse.get_pos()[0] - (dimension_x/2)
            y = pygame.mouse.get_pos()[1] - (dimension_y/2)
            shield.update_position((x, y))
            x_shield, y_shield = shield.get_position()
            x_shield += (dimension_x/2) - 25
            y_shield += (dimension_y/2) - 25
            for i in range(0, enemy_count):
                current_enemy = enemies_array[i]
                enemies_array[i].set_distance(current_enemy.distance - current_enemy.hit)
                if (current_enemy.distance < 0.5):
                    flag = True
                if (abs(current_enemy.get_distance() - shield.shield_distance)<1 and  abs(current_enemy.get_angle_pos()-shield.get_angle_pos())<1):
                    enemies_array[i].set_hit(-1)
                    print("Hit")
                x_enemy, y_enemy = current_enemy.get_position()
                screen.blit(img, (x_enemy + (dimension_x/2) - 25, y_enemy + (dimension_y/2) - 25))
            
            screen.blit(img, (x_shield, y_shield ))
            if (flag):
                #show you lose screen
                pass
        pygame.display.update()