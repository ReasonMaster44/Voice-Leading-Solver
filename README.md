
# Voice Leading Solver

## The Problem

When arranging a chord progression for four voices, there are many possible ways to voice each chord. Naively choosing voicings independently for each chord produces awkward leaps and unnecessary melodic movement. Smooth voice leading minimises the distance each voice travels between chords, creating singable lines.

## The Solution

Given any melodic line, a roughness score can be derived by adding up all the interval jumps between notes. A semitone interval has the smallest roughness value of 1.

Here are some examples of melodies with their corresponding roughness score:

* A, A# - 1
* C, D, C, C - 4
* F, G, G#, F - 6

For each chord in the input progression, many voicing (an ordered set of pitches heard simultaneously) options exist.

Here are two voicing examples of a Cmaj7 chord:

### A: 
* Sop - C
* Alt - G
* Ten - E
* Bass - C

### B: 
* Sop - E
* Alt - C
* Ten - G
* Bass - C

This tool finds the optimal set of voicings given a progression where roughness is minimised throughout.

## Usage

```bash
pip install pygame
```

```python
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
```

```ChoraleEngine.Progression``` takes a ```list``` of ```ChoraleEngine.Chord```s.

The first parameter of ```ChoraleEngine.Chord``` is the root of the chord. The second parameter is the quality of the chord (e.g. major). The third, optional parameter is the quality of the seventh degree of the chord (e.g. diminished).

```ChoraleEngine.Chorale``` takes a ```ChoraleEngine.Progression``` as an argument and computes the optimal voice leading.

```ChoraleUI.start``` takes a ```ChoraleEngine.Chorale``` object and runs a visualisation using standard western notation. Each stave is in treble clef.
