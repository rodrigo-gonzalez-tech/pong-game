import pygame
import sys
import random


pygame.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

cpu_points = 0
player_points = 0


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")


clock = pygame.time.Clock()


def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.centerx = SCREEN_WIDTH/2
    ball.centery = random.randint(10, 100)
    ball_speed_x *= random.choice([-1, 1])


# Scoring system
score_font = pygame.font.Font(None, 100)

def point(winner):
    global cpu_points, player_points
    if winner == "cpu":
        cpu_points += 1
    elif winner == "player":
        player_points += 1
    
    reset_ball()


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
    
    if ball.colliderect(player_paddle) or ball.colliderect(cpu_paddle):
        ball_speed_x *= -1
    
    if ball.right >= SCREEN_WIDTH:
        point("cpu")
    if ball.left <= 0:
        point("player")


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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            player_paddle_speed = -6
        elif keys[pygame.K_DOWN]:
            player_paddle_speed = 6
        else:
            player_paddle_speed = 0


    # Check position of game objects
    animate_ball()
    animate_cpu_paddle()
    move_player_paddle()
    

    # Draw game objects 
    screen.fill((25, 25, 25))

    cpu_score = score_font.render(str(cpu_points), True, "white")
    player_score = score_font.render(str(player_points), True, "white")
    screen.blit(cpu_score, (SCREEN_WIDTH/4, 20))
    screen.blit(player_score, (3*SCREEN_WIDTH/4, 20))

    pygame.draw.ellipse(screen, "white", ball)
    pygame.draw.rect(screen, "white", cpu_paddle)
    pygame.draw.rect(screen, "white", player_paddle)


    # Update display
    pygame.display.update()
    clock.tick(60) # run at 60fps