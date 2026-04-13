
# Voice Leading Solver

## The Problem

When arranging a chord progression for four voices, there are many possible ways to voice each chord. Naively choosing voicings independently for each chord produces awkward leaps and unnecessary melodic movement. Smooth voice leading minimises the distance each voice travels between chords, creating singable lines.

## The Solution

Given any melodic line, a smoothness score can be derived by adding up all the interval jumps between notes. A semitone interval has the smallest smoothness value of 1

Here are some examples of melodies with their corresponding smoothness score:

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

This tool finds the most optimal set of voicings given a progression where smoothness is maximised throughout.
