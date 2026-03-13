import random

import pygame


class Apple:
    def __init__(self,screen_width,screen_height):
        base = min(screen_width, screen_height)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = base // 50
        self.width = base // 50
        self.x = random.randint(0,screen_width-self.width)
        self.y = random.randint(0, screen_height-self.height)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self,screen,red):
        pygame.draw.rect(screen, red, self.rect())

    def spawn(self):
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, self.screen_height - self.height)

