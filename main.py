import pygame
import os
from game import Game

def main():
    pygame.init()
    pygame.mixer.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
