import random
import sys
import os
import time
import pygame
from pygame.locals import *
from random import randint
from pygame.time import *


class ship:
    """Defines properties and functions of spaceship"""

    def __init__(self):
        self.x = 0
        pygame.init()
        self.icon = pygame.image.load("spaceship.png")
        self.icon = pygame.transform.scale(self.icon, (50, 50))

    def move(self, char):
        if char == 'l':
            if self.x != 0:
                self.x -= 50
        elif char == 'r':
            if self.x != 350:
                self.x += 50
