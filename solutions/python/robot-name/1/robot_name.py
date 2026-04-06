"""
Robot Name Generator
"""
import random
from time import time


class Robot:
    """
    Robots do things.  This class sets up a robot with a unique random name
    """
    def __init__(self):
        """
        Sets up the name for the robot
        """
        random.seed(str(time()))
        self.name = self.generate_name()

    def reset(self):
        """
        Generates a new name for the robot
        """
        random.seed(str(time()))
        self.name = self.generate_name()

    @staticmethod
    def generate_name():
        """
        Generates the name of a robot base on this pattern: [A-Z][A-Z][0-9][0-9][0-9]
        """
        return chr(random.randint(65,90)) + chr(random.randint(65,90)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))