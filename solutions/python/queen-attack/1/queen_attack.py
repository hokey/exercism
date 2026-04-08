"""
Queen Chess Attack Class
"""
BOARD_SIZE = 8

class Queen:
    """
    Queen Chess Piece
    """
    def __init__(self, row, column):
        self.validate(row, column)
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if not isinstance(another_queen, Queen):
            raise TypeError("can_attach expects a Queen instance")
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row:
            return True
        if self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False

    def validate(self, row: int, column: int) -> None:
        """
        Confirms position on chess board

        :param int row: Row position
        :param int column: Column position
        :return bool: Valid placement
        """
        if row < 0:
            raise ValueError("row not positive")
        if row >= BOARD_SIZE:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column >= BOARD_SIZE:
            raise ValueError("column not on board")

        