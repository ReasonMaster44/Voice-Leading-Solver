from globals import NOTES
from .voicing import Voicing

class Chord:
    def __init__(self, root: str, quality: str, seventh: str | None=None):
        """
        **Root options:**
         - A
         - Bb
         - C
         - C#
         - D
         - Eb
         - F
         - G
         - Ab
        
        **Quality options:**
         - maj
         - min
         - dim
         - aug
         - sus2
         - sus4
         
        **Seventh options:**
         - maj
         - min
         - dim
        """
        
        self.quality = quality

        self.notes: dict[str: str] = {"root": root, 
                                      "seventh": None}

        if self.quality in ["maj", "aug"]:
            self.notes["third"] = NOTES[(NOTES.index(root) + 4) % 12]
        elif self.quality in ["min", "dim"]:
            self.notes["third"] = NOTES[(NOTES.index(root) + 3) % 12]
        elif self.quality == "sus2":
            self.notes["third"] = NOTES[(NOTES.index(root) + 2) % 12]
        elif self.quality == "sus4":
            self.notes["third"] = NOTES[(NOTES.index(root) + 5) % 12]

        if self.quality in ["maj", "min", "sus2", "sus4"]:
            self.notes["fifth"] = NOTES[(NOTES.index(root) + 7) % 12]
        elif self.quality == "dim":
            self.notes["fifth"] = NOTES[(NOTES.index(root) + 6) % 12]
        elif self.quality == "aug":
            self.notes["fifth"] = NOTES[(NOTES.index(root) + 8) % 12]

        if seventh == "maj":
            self.notes["seventh"] = NOTES[(NOTES.index(root) + 11) % 12]
        elif seventh == "min":
            self.notes["seventh"] = NOTES[(NOTES.index(root) + 10) % 12]
        elif seventh == "dim":
            self.notes["seventh"] = NOTES[(NOTES.index(root) + 9) % 12]
    
    def __iter__(self):
        for note in self.notes:
            yield note

    def __getitem__(self, key):
        return self.notes[key]
    
    def generate_voicing_permutations(self) -> list[Voicing]:
        if self.notes["seventh"]:
            return Voicing([self.notes["root"], self.notes["third"], self.notes["fifth"], self.notes["seventh"]]).get_permutations()
        else:
            voicings: list[Voicing] = []

            doubling_options = [Voicing([self.notes["root"], self.notes["root"], self.notes["third"], self.notes["fifth"]]),
                                Voicing([self.notes["third"], self.notes["third"], self.notes["root"], self.notes["fifth"]]),
                                Voicing([self.notes["fifth"], self.notes["fifth"], self.notes["root"], self.notes["third"]])]
            
            for voicing in doubling_options:
                voicings.extend(voicing.get_permutations())

        return voicings
