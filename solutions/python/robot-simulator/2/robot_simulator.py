"""
Robot Simulator
"""
from enum import IntEnum


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
CARDINAL = [NORTH, EAST, SOUTH, WEST]
ACTIONS = ["L","R","A"]
DELTAS = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1,0)
}


class Robot:
    """
    Robot class that handles positions and movement
    """

    
    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        """
        Initializer for the Robot class

        :param int direction: Where the robot is facing
        :param int x_pos: Starting x position
        :param int y_pos: Starting y position
        """
        if direction not in CARDINAL:
            raise ValueError("Invalid direction")
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
        

    def move(self, action: str) -> None:
        """
        Move action handler for robot.  The actions are:
        - "R": turn right
        - "L": turn left
        - "A": advance

        :param str action: Set of actions to process
        """
        for move_action in action:
            if move_action not in ACTIONS:
                raise ValueError("Invalid action")
            elif move_action == "L":
                self.direction = (self.direction - 1) % 4
            elif move_action == "R":
                self.direction = (self.direction + 1) % 4
            else:
                delta_x, delta_y = DELTAS[self.direction]
                self.coordinates = (
                    self.coordinates[0] + delta_x,
                    self.coordinates[1] + delta_y
                )