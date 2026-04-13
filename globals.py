NOTES = ["A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab"]

def get_interval(a: str, b: str) -> int:
    """Returs the number of semitoes between notes a and b."""

    interval = abs(NOTES.index(a) - NOTES.index(b))

    if interval > 6:
        interval = 12 - interval

    return interval