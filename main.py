import pygame
import sys

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGTH = 800

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()


# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

    # Update Display
    pygame.display.update()
    clock.tick(60) # run at 60fps