import pygame
from pygame.locals import *
from shield import Shield
from sys import exit
enemies_array = [ ]

pygame.init()
dimension_x = 1200
dimension_y = 1000
x = 0
y = 0
screen = pygame.display.set_mode((dimension_x, dimension_y))
shield = Shield((50, 50))
img = pygame.image.load("cursor.png")
img.convert()

while True:
    
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x = pygame.mouse.get_pos()[0] - (dimension_x/2)
            y = pygame.mouse.get_pos()[1] - (dimension_y/2)
            print("x = ", x, " y = ", y)
            shield.update_position((x, y))
            screen.fill((255, 255, 255))
            x_shield, y_shield = shield.get_position()
            screen.blit(img, (x_shield + (dimension_x/4), y_shield + (dimension_y/4)))
            pygame.display.update()
        if event.type == pygame.QUIT:  
           exit()