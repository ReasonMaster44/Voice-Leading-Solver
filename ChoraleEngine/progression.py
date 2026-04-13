from .chord import Chord
from globals import get_interval

class Progression:
    def __init__(self, chords: list[Chord]):
        self.chords: list[Chord] = chords
    
    def __iter__(self):
        for chord in self.chords:
            yield chord