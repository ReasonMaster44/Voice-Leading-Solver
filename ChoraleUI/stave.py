import pygame as pg
from .note import Note
from globals import NOTES

class Stave:
    line_spacing = 10
    line_width = 1

    note_spacing = 50

    def __init__(self, x, y, width, notes):
        self.x, self.y = x, y
        self.width = width

        self.notes: list[Note] = []

        for note in notes:
            self.notes.append(Note(note, Stave.line_spacing / 2))

    def draw(self, surf: pg.Surface):
        for i in range(5):
            x = self.x
            y = self.y + (Stave.line_spacing * i)

            pg.draw.line(surf, (200, 200, 200), (x, y), (x + self.width, y), Stave.line_width)
        
        for i, note in enumerate(self.notes):
            note.draw(surf, self.x + (Stave.note_spacing * (i + 1)), self.get_y_from_note(note.note))
    
    @staticmethod
    def get_height() -> int:
        return Stave.line_spacing * 4

    def get_y_from_note(self, note: str):
        natural_notes = ["E", "F", "G", "A", "B", "C", "D"]

        index = natural_notes.index(note[0])

        y = self.y + Stave.get_height()

        y -= (Stave.line_spacing / 2) * (index)

        return y