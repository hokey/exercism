"""
Robot Simulator
"""
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


CARDINAL = [NORTH, EAST, SOUTH, WEST]


class Robot:
    """
    Robot class that handles positions and movement
    """

    
    def __init__(self, direction: str = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        """
        Initializer for the Robot class

        :param str direction: Where the robot is facing
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
            if move_action == "L":
                self.direction = (self.direction - 1) % 4
            if move_action == "R":
                self.direction = (self.direction + 1) % 4
            if move_action == "A":
                if self.direction == NORTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
                if self.direction == EAST:
                    self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
                if self.direction == SOUTH:
                    self.coordinates = (self.coordinates[0] , self.coordinates[1] - 1)
                if self.direction == WEST:
                    self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
    