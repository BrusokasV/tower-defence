import pygame
import User
from sys import exit

pygame.init()

screen = pygame.display.set_mode((100, 50))
user = User((0, 0))
img = pygame.image.load("cursor.png")

running = True

while running:
    User.update_position(user, pygame.mouse.get_pos())

    screen.fill((255, 255, 255))
    screen.blit(img, user.get_position())

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           exit()