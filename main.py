import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
    # initializing pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Groups:
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # game loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        # update:
        updatable.update(dt)

        # collision checks:
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
        
        # drawing:
        for sprite in drawable:
            sprite.draw(screen)

        # rendering:
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()