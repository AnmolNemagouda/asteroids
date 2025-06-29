import pygame
import sys
from constants import *
from player import Player, Shot
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    # Initialize sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidgroup = pygame.sprite.Group()
    shotgroup = pygame.sprite.Group()
    # Create instances of the game objects
    Asteroid.containers = (asteroidgroup, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shotgroup, updatable, drawable)
    afield = AsteroidField()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    newobj = pygame.time.Clock()

    dt=60
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        a= newobj.tick(60)
        dt = a / 1000.0  # Convert milliseconds to seconds
        updatable.update(dt)
        for obj in asteroidgroup:
            if obj.is_colliding(player) == True:
                print("Game Over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroidgroup:
            for bullet in shotgroup:
                if obj.is_colliding(bullet):
                    obj.kill()
                    bullet.kill()
                    
        pygame.display.flip()
if __name__ == "__main__":
    main()