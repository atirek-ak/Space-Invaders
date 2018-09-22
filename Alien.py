import random
import sys
import os
import time
import pygame
from pygame.locals import *
from random import randint
from pygame.time import *


class alien:
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.nextspawn = 10000
        self.start = []
        self.next = pygame.time.get_ticks()
        self.x = []
        self.y = []
        self.icon = []
        self.cooldown = []

    def destruct(self, i):
        self.start.pop(i)
        self.y.pop(i)
        self.x.pop(i)
        self.icon.pop(i)
        self.cooldown.pop(i)

    def wait(self):
        now = pygame.time.get_ticks()
        # print(now)
        # print(self.next)
        if now - self.next >= self.nextspawn:
            self.spawn()
        for i in range(0, len(self.start)):
            if now - self.start[i] >= self.cooldown[i]:
                self.destruct(i)
                break

    def spawn(self):
        self.a = randint(0, 7)*50
        self.b = randint(0, 1)*50
        for i in range(0, len(self.x)):
            if self.a == self.x[i] and self.b == self.y[i]:
                self.a = randint(0, 7)*50
                self.b = randint(0, 1)*50
                i = 0
        self.x.append(self.a)
        self.next = pygame.time.get_ticks()
        self.y.append(self.b)
        self.start.append(self.next)
        self.cooldown.append(8000)
        self.icon.append(pygame.image.load("alien.png"))
        var = len(self.icon)-1
        self.icon[var] = pygame.transform.scale(self.icon[var], (50, 50))
