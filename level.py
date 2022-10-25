import pygame
import sys

from settings import *

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        
        self.all_sprites = pygame.sprite.Group()
    def run(self, dt):
        dt = self.clock.tick()/1000
        self.level.run(dt)
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
