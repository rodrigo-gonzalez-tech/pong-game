import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

# Ball
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
ball_speed_x = 6
ball_speed_y = 6

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0:
        ball_speed_y *= -1
    if ball.right >= SCREEN_WIDTH or ball.left <= 0:
        ball_speed_x *= -1

# "AI"-controlled paddle 
cpu_paddle = pygame.Rect(0, 0, 20, 100)
cpu_paddle.centery = SCREEN_HEIGHT/2
cpu_paddle_speed = 6

def animate_cpu_paddle():
    global cpu_paddle_speed
    cpu_paddle.y += cpu_paddle_speed

    if ball.centery <= cpu_paddle.centery:
        cpu_paddle_speed = -6
    if ball.centery >= cpu_paddle.centery:
        cpu_paddle_speed = 6

    if cpu_paddle.top <= 0:
        cpu_paddle.top = 0
    if cpu_paddle.bottom >= SCREEN_HEIGHT:
        cpu_paddle.bottom = SCREEN_HEIGHT

# Player paddle
player_paddle = pygame.Rect(0, 0, 20, 100)
player_paddle.midright = (SCREEN_WIDTH, SCREEN_HEIGHT/2)
player_paddle_speed = 0

def move_player_paddle():
    global player_paddle_speed
    player_paddle.y += player_paddle_speed
    if player_paddle.top <= 0:
        player_paddle.top = 0
    if player_paddle.bottom >= SCREEN_HEIGHT:
        player_paddle.bottom = SCREEN_HEIGHT

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_paddle_speed = -6
            if event.key == pygame.K_DOWN:
                player_paddle_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_paddle_speed = 0
            if event.key == pygame.K_DOWN:
                player_paddle_speed = 0



    # Check position of game objects
    animate_ball()
    animate_cpu_paddle()
    move_player_paddle()
    

    # Draw game objects 
    screen.fill("black")
    pygame.draw.aaline(screen, "white", (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, "white", ball)
    pygame.draw.rect(screen, "white", cpu_paddle)
    pygame.draw.rect(screen, "white", player_paddle)


    # Update display
    pygame.display.update()
    clock.tick(60) # run at 60fps