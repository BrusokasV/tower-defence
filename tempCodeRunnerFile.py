import pygame
from shield import Shield
from sys import exit

pygame.init()
dimension_x = 1000
dimension_y = 750
screen = pygame.display.set_mode((dimension_x, dimension_y))
shield = Shield((0, 0))
img = pygame.image.load("cursor.png")

running = True

while running:
    shield.update_position(pygame.mouse.get_pos())

    screen.fill((255, 255, 255))
    screen.blit(img, shield.get_position())

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           exit()