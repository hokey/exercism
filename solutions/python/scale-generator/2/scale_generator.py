"""
Scale Generator Utility
"""
SHARP_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT_SCALE = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
KEY_SHARP = ["G", "D", "A", "E", "B", "F#", "C", "e", "b", "f#", "c#", "g#", "d#", "a"]
KEY_FLAT = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]

class Scale:
    """
    Scale for generating musical scales of multiple types
    """
    def __init__(self, tonic: str) -> None:
        """
        Scale class initializer
        :param str tonic: Tonic of the scale
        """
        if not tonic or tonic not in KEY_SHARP and tonic not in KEY_FLAT:
            raise ValueError("Must be a valid tonic")
        if tonic in KEY_SHARP:
            index: int = SHARP_SCALE.index(tonic.upper())
            self.chromatic_scale = SHARP_SCALE[index::] + SHARP_SCALE[:index:]
        else:
            if len(tonic) == 2:
                test: str = tonic[0].upper() + tonic[1]
            else:
                test: str = tonic.upper()
            index: int = FLAT_SCALE.index(test)
            self.chromatic_scale = FLAT_SCALE[index::] + FLAT_SCALE[:index:]


    def chromatic(self):
        """
        Gets the chromatic scale
        :return list[str]: The chromatic scale
        """
        return self.chromatic_scale


    def interval(self, intervals: str) -> list[str]:
        """
        Produced the desired interval of the scale
        :param str intervals: A string representing the intervals for the desired scale, using m, M, and A.
        :return list[str]: The list of intervals
        """
        if not intervals:
            raise ValueError("Must be a valid interval")
        step: int = 0
        result: list[str] = [self.chromatic_scale[0]]
        for note_type in intervals:
            if note_type == "A":
                step += 3
            elif note_type == "M":
                step += 2
            else:
                step += 1
            result.append(self.chromatic_scale[step % len(self.chromatic_scale)])
        return result
