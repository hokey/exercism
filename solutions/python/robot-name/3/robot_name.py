"""
Robot Name Generator
"""
import random
from string import ascii_uppercase, digits


class Robot:
    """
    Robots do things.  This class sets up a robot with a unique random name
    """
    _rng = random.Random()

    
    def __init__(self):
        """
        Sets up the name for the robot
        """
        self.name = self.generate_name()

    
    def reset(self):
        """
        Generates a new name for the robot
        """
        self.name = self.generate_name()

    
    @classmethod
    def generate_name(cls):
        """
        Generates the name of a robot base on this pattern: [A-Z][A-Z][0-9][0-9][0-9]

        :return str: randomly generated name
        """
        return "".join(cls._rng.choices(ascii_uppercase, k=2) + cls._rng.choices(digits, k=3))