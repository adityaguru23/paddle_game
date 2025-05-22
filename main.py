import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paddle and Ball Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle setup
paddle_width, paddle_height = 100, 20
paddle_x = (width - paddle_width) // 2
paddle_y = height - 2 * paddle_height
paddle_speed = 5

# Ball setup
ball_size = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collision with walls
    if ball_x <= 0 or ball_x >= width - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # Collision with paddle
    if (
        paddle_x < ball_x < paddle_x + paddle_width and
        paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_speed_y = -ball_speed_y

    # Game Over if ball goes below the paddle
    if ball_y >= height:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)
