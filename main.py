import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Protect the Pumpkin")

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
pumpkin_img = pygame.image.load('dyhtg/halloween-ghost-pumpkin.png')
pumpkin_img = pygame.transform.scale(pumpkin_img, (80, 80))

#locations
pumpkin_pos = [screen_width // 2, screen_height // 2]
shield_radius = 100
shield_color = (255, 255, 255)

#lives
hearts = 3

#hearts pic
heart_img = pygame.image.load('dyhtg/heart.png')
heart_img = pygame.transform.scale(heart_img, (40, 40))

#draws our hearts
def draw_lives():
    for i in range(hearts):
        heart_x = 20 + i * 50
        heart_y = screen_height - 60

        #draws a frame for each heart
        frame_rect = pygame.Rect(heart_x - 5, heart_y - 5, 50, 50)
        pygame.draw.rect(screen, (0, 0, 0), frame_rect, 3)

        screen.blit(heart_img, (heart_x, heart_y))


#draws our score
def draw_score():
    score = 100
    score_block_width = 200
    score_block_height = 40
    score_block_x = screen_width - score_block_width - 20
    score_block_y = screen_height - score_block_height - 20

    #draw a frame for a score
    pygame.draw.rect(screen, (255, 255, 255), (score_block_x, score_block_y, score_block_width, score_block_height))
    pygame.draw.rect(screen, (0, 0, 0), (score_block_x, score_block_y, score_block_width, score_block_height),
                     3)

    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0)) #suppose we have a var score instead of 0
    screen.blit(score_text, (score_block_x + 10, score_block_y + 10))

def game_loop():
    running = True
    while running:
        screen.fill((120, 100, 100))

        #title
        screen.blit(rules_title_main, (screen_width // 2 - rules_title_main.get_width() // 2, 50))
        screen.blit(pumpkin_img, (pumpkin_pos[0] - 40, pumpkin_pos[1] - 40))
        pygame.draw.circle(screen, shield_color, pumpkin_pos, shield_radius, 2)

        draw_lives()
        draw_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.flip()
        pygame.time.Clock().tick(60)


def start_screen():
    while True:
        screen.fill((120, 100, 100)) #main background

        # title
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

        # rules box
        pygame.draw.rect(screen, (198, 89, 33), (100, 200, 800, 300))
        pygame.draw.rect(screen, (0, 0, 0), (100, 200, 800, 300), 3)

        # description of the rules
        screen.blit(rules_title, (screen_width // 2 - rules_title.get_width() // 2, 230))
        screen.blit(rules_text, (screen_width // 2 - rules_text.get_width() // 2, 280))
        screen.blit(rules_text2, (screen_width // 2 - rules_text2.get_width() // 2, 320))

        # start game btn
        button_rect = pygame.Rect(screen_width // 2 - 150, 400, 300, 75)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
        screen.blit(button_text, (screen_width // 2 - button_text.get_width() // 2, 425))

        # Handle events
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
