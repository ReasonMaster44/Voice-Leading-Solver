import ChoraleEngine as ce
import ChoraleUI as cu

progression = ce.Progression([ce.Chord("C", "maj"),
                              ce.Chord("D", "min"),
                              ce.Chord("G", "maj"),
                              ce.Chord("E", "min"),
                              ce.Chord("A", "min"),
                              ce.Chord("G", "maj"),
                              ce.Chord("C", "maj"),
                              ce.Chord("A", "min")])

c = ce.Chorale(progression)

cu.start(c)