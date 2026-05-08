"""
Frogger High Scores Tracker
"""
import heapq
from dataclasses import dataclass, field

@dataclass
class HighScores:
    """
    Tracker for Frogger Scores
    """
    scores: list[int] = field(repr=False)
    
    def __post_init__(self) -> None:
        """
        HighScores Initializer

        :param list[int] scores: List of scores 
        """
        if not self.scores:
            raise ValueError("Score list is empty")
        self.scores = list(self.scores)

    
    def latest(self) -> int:
        """
        Gives the latest score

        :return int: The latest score
        """
        return self.scores[-1]


    def personal_best(self) -> int:
        """
        Gives the personal best

        :return int: The highest score
        """
        return max(self.scores)


    def personal_top_three(self) -> list[int]:
        """
        Gives the top three scores

        :return list[int]: The top three scores
        """
        return heapq.nlargest(3, self.scores)