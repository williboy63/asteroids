
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    my_clock = pygame.time.Clock()
    dt = 0

    
    game = True
    while game:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                return
            
        my_clock.tick(60)
        dt = my_clock.tick(60)/1000

        print(dt)



print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":

    main()
