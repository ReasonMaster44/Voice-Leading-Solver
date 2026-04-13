from .voicing import Voicing
from .progression import Progression

class Chorale:
    def __init__(self, progression: Progression):
        self.voicings: list[Voicing] = []

        for i, chord in enumerate(progression):
            if i == 0:
                if chord["seventh"]:
                    new_voicing = Voicing([chord["seventh"], chord["fifth"], chord["third"], chord["root"]])
                else:
                    new_voicing = Voicing([chord["root"], chord["fifth"], chord["third"], chord["root"]])
                self.voicings.append(new_voicing)
            else:
                # All the possible permutations for next voicing in the chorale
                next_voicing_options = chord.generate_voicing_permutations()

                # Check which voicing option yields the best voice leading optimality:
                optimal_voicing = min(next_voicing_options, key=lambda voicing: Voicing.get_voice_leading_optimality(voicing, self.voicings[-1]))

                self.voicings.append(optimal_voicing)

    def __iter__(self):
        for voicing in self.voicings:
            yield voicing
    
    def log(self):
        for i in range(4):
            for voicing in self.voicings:
                print(voicing.notes[i], end=", ")
            print()