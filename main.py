import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    newobj = pygame.time.Clock()
    dt=60
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        a= newobj.tick(60)
        dt = a / 1000.0  # Convert milliseconds to seconds
        pygame.display.flip()
if __name__ == "__main__":
    main()