import pygame

# Code a simple snake game using pygame
# 1. Create a snake class
def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
# 2. Create a food class
# 3. Create a game class
# 4. Create a main function
