import pygame
import User
from sys import exit

pygame.init()
dimension_x = 1000
dimension_y = 750
screen = pygame.display.set_mode((dimension_x, dimension_y))
user = User((0, 0))
img = pygame.image.load("cursor.png")

running = True

while running:
    user.update_position(pygame.mouse.get_pos())

    screen.fill((255, 255, 255))
    screen.blit(img, user.get_position())

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           exit()