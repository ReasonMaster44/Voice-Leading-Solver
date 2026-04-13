import pygame as pg
from globals import NOTES
from .text import Text

class Note:
    def __init__(self, note, radius):
        self.note = note
        self.radius = radius

        self.accidental_text = None

        if self.note[-1] == "b":
            self.accidental_text = Text(0, 0, "b", 17)
        elif self.note[-1] == "#":
            self.accidental_text = Text(0, 0, "#", 17)
    
    def draw(self, surf: pg.Surface, x, y):
        pg.draw.circle(surf, (255, 255, 255), (x, y), self.radius, 2)

        if self.accidental_text:
            text_y = y

            if self.note[-1] == "b":
                text_y -= 2

            self.accidental_text.set_pos(x - self.radius * 2.5, text_y)
            self.accidental_text.draw(surf)