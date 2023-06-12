import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set up game variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
fruit_position = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
fruit_spawned = True
direction = 'RIGHT'
change_to = direction
score = 0

# Set up game clock
clock = pygame.time.Clock()

# Function to display score
def show_score():
    font = pygame.font.Font('freesansbold.ttf', 20)
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])

# Function to display game over message
def game_over():
    font = pygame.font.Font('freesansbold.ttf', 60)
    game_over_text = font.render("Game Over", True, white)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    window.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.display.flip()
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'

    # Update snake's direction
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Move the snake
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawned = False
    else:
        snake_body.pop()

    # Respawn the fruit
    if not fruit_spawned:
        fruit_position = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
        fruit_spawned = True

    # Game over if snake hits the boundaries or itself
    if snake_position[0] < 0 or snake_position[0] > width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Clear the game window
    window.fill(black)

    # Draw the snake
    for position in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(position[0], position[1], 10, 10))

    # Draw the fruit
    pygame.draw.rect(window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Display the score
    show_score()

    # Refresh the game window
    pygame.display.flip()

    # Set the game speed
    clock.tick(20)
