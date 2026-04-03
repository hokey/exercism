"""
Character Class for Dungeons & Dragons (D&D)
"""
from random import randint
from math import floor

HITPOINTS = 10
ABILITIES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

class Character:
    """
    Character class for D&D
    """
    
    def __init__(self):
        """
        Instantiate the D&D character by assigning the six abilities; strength, dexterity, constitution, intelligence, wisdom and charisma. Then setup the hitpoints as a default of 10 plus the modifier based on the character's constitution.
        """
        self.abilities = {
            ability_name: self.ability()
            for ability_name in ABILITIES
        }
        self.hitpoints = HITPOINTS + modifier(self.constitution)
        
    def ability(self):
        """
        Generate an ability score by rolling a six sided dice 4 times and summing the largest 3 results
        """
        score = [randint(1,6) for roll in range(4)]
        score.remove(min(score))
        return sum(score)

def modifier(value):
    """
    Apply the modifier for the given value

    :param int value: The vaule to modify
    :return int: Modified value
    """
    return (value - 10) // 2

    
def _make_ability_property(name):
    """
    Create the accessible ability property for the 
    """
    return property(lambda self, n=name: self.abilities[n])


for ability in ABILITIES:
    setattr(Character, ability, _make_ability_property(ability))