import random

import pygame

from main import screen


class Apple:
    def __init__(self,screen_width,screen_height):
        base = min(screen_width, screen_height)
        self.height = base // 50
        self.width = base // 50
        self.x = random.randTnt(0,screen_width-self.width)
        self.y = random.randInt(0, screen_height-self.height)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self,screen,red):
        pygame.draw.rect(screen, red, self.rect())