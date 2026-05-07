"""
Allergies calculations utility
"""
from dataclasses import dataclass, field

ALLERGENS = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats"
}


@dataclass
class Allergies:
    """
    Allergies class for calculating score based allergies
    """
    score: int
    allergies: list[str] = field(default_factory=list)

    def __post_init__(self):
        """
        Validates and process score.  Builds the list of allergies given the score.
        """
        if self.score < 0:
            raise ValueError("Non negative scores only")
        allergy_score = self.score
        while allergy_score > 0:
            candidate = 1 << (allergy_score.bit_length() - 1)
            if candidate in ALLERGENS:
                self.allergies.append(ALLERGENS[candidate])
            allergy_score -= candidate
        self.allegies = self.allergies.reverse()
        
    def allergic_to(self, item):
        """
        Given an allergen, report the inclusion of it in the score

        :param str item: The allergen
        :return bool: If it's in the score or not
        """
        return item in self.allergies
    
    @property
    def lst(self):
        """
        Give the list of allergies scored

        :return list[str]: Allergy list
        """
        return self.allergies