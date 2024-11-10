import pygame
from constants import *
from player import Player

def main():
    # initializing pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    updatable.add(player)
    drawable.add(player)

    # game loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()