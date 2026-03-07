import pygame
import sys

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGTH = 800

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

# Ball
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (WINDOW_WIDTH/2, WINDOW_HEIGTH/2)

# AI-controlled paddle 
cpu_paddle = pygame.Rect(0, 0, 20, 100)
cpu_paddle.centery = WINDOW_HEIGTH/2

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

    # Draw game objects 
    pygame.draw.ellipse(window, "white", ball)
    pygame.draw.rect(window, "white", cpu_paddle)



    # Update Display
    pygame.display.update()
    clock.tick(60) # run at 60fps