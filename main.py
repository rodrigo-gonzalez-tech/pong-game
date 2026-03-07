import pygame
import sys

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGTH = 800

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()