import pygame
import sys

from settings import *
from level import *
class Game(Level):
    def __init__ (self, ):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
        self.clock = pygame.time.clock()
        
        
    def run(self):
        while True:
            for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.level.run(dt)
            dt = self.clock.tick()/1000
            pygame.display.update()

            
if __name__ == '__main__':
    game = Game()
    game.run()