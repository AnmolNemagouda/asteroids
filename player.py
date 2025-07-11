from circleshape import CircleShape
import pygame
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED
 
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot_position = self.position + pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
        shot.velocity = shot_velocity
    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]: # Decrease the shoot timer
            if self.shoot_timer > 0:
                self.shoot_timer -= dt
            else:
                self.shoot()
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN
class Shot(CircleShape):
    def __init__(self,x,y, radius=SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)

        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 1)
        
    def update(self, dt):
        self.position += self.velocity * dt
