import pygame as pg
from .stave import Stave
from ChoraleEngine import Chorale

class System:
    stave_spacing = 100
    def __init__(self, x, y, width, chorale: Chorale):
        self.x, self.y = x, y
        self.width = width

        self.staves: list[Stave] = []

        for i in range(4):
            notes = []

            for voicing in chorale.voicings:
                notes.append(voicing.notes[i])
            
            new_stave = Stave(self.x, self.y + (System.stave_spacing * i), self.width, notes)
            self.staves.append(new_stave)

    def draw(self, surf: pg.Surface):
        for stave in self.staves:
            stave.draw(surf)

        for i in range(2):
            pg.draw.line(surf, (200, 200, 200), (self.x + (self.width * i), self.y), 
                                                (self.x + (self.width * i), self.y + System.get_height()), 1)
    
    @staticmethod
    def get_height():
        return (3 * System.stave_spacing) + Stave.get_height()