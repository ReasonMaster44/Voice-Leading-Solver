from globals import NOTES, get_interval
import itertools

class Voicing:
    def __init__(self, notes: list[str]):
        assert all(note in NOTES for note in notes), "Invalid notes"
        self.notes = notes # ORDERED
    
    def __iter__(self):
        for note in self.notes:
            yield note
    
    def __getitem__(self, index):
        return self.notes[index]
    
    def get_num_voices(self) -> int:
        return len(self.notes)

    
    @staticmethod
    def get_voice_leading_optimality(a: "Voicing", b: "Voicing") -> int:
        assert a.get_num_voices() == b.get_num_voices(), "Both voicings must have the same number of voices"

        total = 0

        for i in range(a.get_num_voices()):
            total += get_interval(a[i], b[i])
        
        return total

    def get_permutations(self) -> list["Voicing"]:
        """Returns a list of all possible voicings from the notes in self"""
        permutations = itertools.permutations(self.notes)
        
        voicings: list["Voicing"] = []
        for perm in permutations:
            voicings.append(Voicing(list(perm)))

        return voicings