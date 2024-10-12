import pygame
from pygame.locals import *
from shield import Shield
from sys import exit
enemies_array = [ ]

pygame.init()
dimension_x = 1000
dimension_y = 750
screen = pygame.display.set_mode((dimension_x, dimension_y))
shield = Shield((0, 0), (dimension_x/2, dimension_y/2))
img = pygame.image.load("cursor.png")
img.convert()

while True:
    
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            shield.update_position(pygame.mouse.get_pos())
            screen.blit(img, shield.get_position())
            pygame.display.update()
        if event.type == pygame.QUIT:  
           exit()