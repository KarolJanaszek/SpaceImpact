import pygame
import random

from pygame.locals import (
    RLEACCEL,
    KEYUP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("resources\\jest.png").convert()
