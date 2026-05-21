"""
Hex Game Utility
"""
DIRECTIONS = [(-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0)]

class ConnectGame:
    """
    ConnectGame manages actions for the Hex style board game
    """
    def __init__(self, board):
        """
        Initializes board by splitting by new line characters and stripping whitespace

        :param str board: Board of the Hex game
        """
        self.board = [row.strip().split() for row in board.split("\n")]

    def get_winner(self) -> str:
        """
        Determines if there is a winner of the Hex game.  The winner is whomever has both ends
        of the board connected by their piece and filled with any piece inbetween.
        """
        if self.find_winner("X"):
            return "X"
        if self.find_winner("O"):
            return "O"
        return ""

    def find_winner(self, player: str) -> bool:
        """
        Finds the winner if available

        :param str player: The player string
        :return bool: If we have a winner
        """
        visited: set = set()
        num_rows: int = len(self.board)
        num_cols: int = len(self.board[0])
        if player == "X":
            stack: list[tuple[int, int]] = [(row, 0) for row in range(num_rows) if self.board[row][0] == player]
        else:
            stack: list[tuple[int, int]] = [(0, col) for col in range(num_cols) if self.board[0][col] == player]
        while stack:
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            reached: bool = row == num_rows - 1 if player == "O" else col == num_cols - 1
            if reached:
                return True
            for new_row, new_col in self.neighbors(row, col):
                if self.board[new_row][new_col] == player and (new_row, new_col) not in visited:
                    stack.append((new_row, new_col))
        return False

    def neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
        """
        Gets the neighbors from the board

        :param int row: Row
        :param int col: Col
        :return list[tuple[int, int]]
        """
        num_rows: int = len(self.board)
        num_cols: int = len(self.board[0])
        for dir_row, dir_col in DIRECTIONS:
            new_row, new_col = row + dir_row, col + dir_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                yield new_row, new_col

    
