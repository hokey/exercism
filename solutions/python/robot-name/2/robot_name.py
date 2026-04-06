"""
Robot Name Generator
"""
from random import seed, choices
from string import ascii_uppercase, digits


class Robot:
    """
    Robots do things.  This class sets up a robot with a unique random name
    """
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

    @staticmethod
    def generate_name():
        """
        Generates the name of a robot base on this pattern: [A-Z][A-Z][0-9][0-9][0-9]
        """
        seed()
        return "".join(choices(ascii_uppercase, k=2) + choices(digits, k=3))