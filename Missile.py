import random
import sys
import os
import time
import pygame
from pygame.locals import *
from random import randint
from pygame.time import *


class Missile:
    def __init__(self, speed, icon):
        self.speed = speed
        self.icon = icon
        self.icon = pygame.transform.scale(self.icon, (50, 50))

    def wait(self):
        for i in range(0, len(self.y)):
            if self.y[i] < 0:
                self.destruct(i)
                break

        now = pygame.time.get_ticks()
        if now - self.last >= 500:
            self.last = now
            for i in range(0, len(self.y)):
                self.y[i] -= self.speed

    def spawn(self, spacex):
        self.x.append(spacex)
        self.y.append(300)

    def destruct(self, i):
        self.x.pop(i)
        self.y.pop(i)


class Missile1(Missile):
    def __init__(self):
        super().__init__(25, pygame.image.load("Missile1.png"))
        self.x = []
        self.y = []
        self.last = 0

    def move(self):
        super().wait()

    def spawn(self, spacex):
        if len(self.x) == 0:
            self.last = pygame.time.get_ticks()
        super().spawn(spacex)

    def destruct(self, i):
        super().destruct(i)


class Missile2(Missile):
    def __init__(self):
        super().__init__(50, pygame.image.load("Missile2.png"))
        self.x = []
        self.y = []
        self.last = 0

    def move(self):
        super().wait()

    def spawn(self, spacex):
        if len(self.x) == 0:
            self.last = pygame.time.get_ticks()
        super().spawn(spacex)

    def destruct(self, i):
        super().destruct(i)
