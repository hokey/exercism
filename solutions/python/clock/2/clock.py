"""
Clock Utility
"""
from dataclasses import dataclass

@dataclass
class Clock:
    """
    Clock representing 24 hour and 60 minute hands
    """
    hour: int
    minute: int
    def __post_init__(self):
        self.hour = ((self.minute // 60) + self.hour) % 24
        self.minute = self.minute % 60
        
    def __repr__(self):
        """
        Representation of Clock
        """
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        """
        String of Clock
        """
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        """
        Clock equality
        """
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute

    def __hash__(self):
        """
        Clock hash
        """
        return hash((self.hour, self.minute))

    def __add__(self, minutes: int):
        """
        Add minutes to Clock
        """
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int):
        """
        Subtract minutesfrom Clock
        """
        return Clock(self.hour, self.minute - minutes)
