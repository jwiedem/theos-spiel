import pygame

class score:
    def __init__(self,apfel):
        self.score = 0
        self.apfel = apfel
        if apfel.spawn(true):
                self.score = +1
