import pygame
from pygame.locals import *
from shield import Shield
from sys import exit
from time import sleep
from Enemies import Enemies, populate
import math
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
img_ghost = pygame.transform.scale(pygame.image.load("cursor.png"), (50,50))
img.convert()
SPAWNEVENT = pygame.USEREVENT + 1
TICKEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWNEVENT, 2000)
pygame.time.set_timer(TICKEVENT, 10)
enemy_count = 0
current_rotation = 0
screen.fill((255, 255, 255))

while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            exit()
        if event.type == SPAWNEVENT:
            if (enemy_count<20):
                enemy_count += 1
        if event.type == TICKEVENT:
            if (shield.get_lives() == 0):
                #you died
                pass
            screen.fill((255, 255, 255))
            x = pygame.mouse.get_pos()[0] - (dimension_x/2)
            y = pygame.mouse.get_pos()[1] - (dimension_y/2)
            shield.update_position((x, y))
            x_shield, y_shield = shield.get_position()
            x_shield += (dimension_x/2) - 25
            y_shield += (dimension_y/2) - 25
            for i in range(0, enemy_count):
                if (not enemies_array[i].get_taken_life()):
                    current_enemy = enemies_array[i]
                    enemies_array[i].set_distance(current_enemy.distance - current_enemy.hit)                    
                    if (abs(current_enemy.get_distance() - shield.shield_distance)<0.0000001 and  abs(current_enemy.get_angle_pos()-shield.get_angle_pos())<1 and not enemies_array[i].get_taken_life()):
                        enemies_array[i].set_hit(-1)
                        shield.add_score(abs(current_enemy.get_hit()))
                    elif (current_enemy.get_distance()<10):
                        shield.reduce_lives()
                        current_enemy.set_taken_life(True)
                    x_enemy, y_enemy = current_enemy.get_position()
                    screen.blit(img_ghost, (x_enemy + (dimension_x/2) - 25, y_enemy + (dimension_y/2) - 25))
                    if (enemies_array[i].get_hit()<0 and enemies_array[i].get_distance()>700):
                        enemies_array[i].set_hit(-1)
                        print("return")
            #img = pygame.transform.rotate(img, (shield.get_angle_pos()*180/math.pi) - current_rotation)
            #current_rotation = shield.get_angle_pos()*180/math.pi
            screen.blit(img, (x_shield, y_shield))
            print("Score: ", shield.get_score(), " Lives = ", shield.get_lives())
        pygame.display.update()