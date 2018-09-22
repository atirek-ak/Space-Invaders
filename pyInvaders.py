import random
import sys
import os
import time
import Spaceship
import Alien
import math
import Missile
import pygame
from pygame.locals import *
from random import randint
from pygame.time import *
from pygame.font import *

spaceship = Spaceship.ship()
alien = Alien.alien()
missile1 = Missile.Missile1()
missile2 = Missile.Missile2()


class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Invaders")
        self.score = 0
        alien.spawn()
        self.printboard()

    def printboard(self):

        screen = pygame.display.set_mode((600, 400))
        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 400), 1)
        #pygame.draw.line(screen, (0, 0, 0), (0, 0.1), (400, 0.1), 1)
        #pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 400), 1)
        #pygame.draw.line(screen, (0, 0, 0), (0, 399), (400, 399), 1)
        screen.blit(spaceship.icon, (spaceship.x, 350))
        for i in range(0, len(alien.x)):
            for j in range(0, len(missile1.x)):
                if missile1.y[j] - alien.y[i] <= 25 and missile1.x[j]-alien.x[i] == 0:
                    if alien.cooldown[i] == 8000:
                        self.score += 1
                    alien.destruct(i)
                    missile1.destruct(j)
                    break

        for i in range(0, len(alien.x)):
            for j in range(0, len(missile2.x)):
                if alien.y[i] == missile2.y[j] and missile2.x[j] == alien.x[i]:
                    alien.start[i] = pygame.time.get_ticks()
                    if alien.cooldown[i] == 8000:
                        self.score += 1
                    alien.cooldown[i] = 5000
                    missile2.destruct(j)
                    alien.icon[i] = pygame.image.load("alienintrouble.png")
                    alien.icon[i] = pygame.transform.scale(
                        alien.icon[i], (50, 50))
                    break

        for i in range(0, len(alien.x)):
            screen.blit(alien.icon[i], (alien.x[i], alien.y[i]))
        for i in range(0, len(missile1.x)):
            screen.blit(missile1.icon, (missile1.x[i], missile1.y[i]))
        for i in range(0, len(missile2.x)):
            screen.blit(missile2.icon, (missile2.x[i], missile2.y[i]))

        font = pygame.font.Font(None, 65)
        scoretext = font.render("Score:"+str(self.score), 1, (0, 0, 0))
        screen.blit(scoretext, (410, 0))

        pygame.display.flip()

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == ord('a'):
                        spaceship.move('l')
                    elif event.key == ord('d'):
                        spaceship.move('r')
                    elif event.key == ord('q'):
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        missile1.spawn(spaceship.x)
                    elif event.key == ord('s'):
                        missile2.spawn(spaceship.x)

            alien.wait()
            if len(missile2.x) > 0:
                missile2.move()
            if len(missile1.x) > 0:
                missile1.move()
            self.printboard()


obj = Board()
obj.main()
