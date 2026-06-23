"""Go Counting Utility"""
from collections import deque

WHITE: str = "W"
BLACK: str = "B"
NONE: str = " "

DELTAS: list[tuple[int, int]] = [
    (0, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 0)
]

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        """Initialize a board object

        Args:
            board (list[str]): A two-dimensional Go board
        "
        """
        if not board:
            raise ValueError("Board must not be empty")

        if any(len(row) != len(board[0]) for row in board):
            raise ValueError("Board must have rows of equal length")

        if any(piece not in {WHITE, BLACK, NONE} for row in board for piece in row):
            raise ValueError("Invalid board piece")

        self.board: list[list[str]] = [list(row) for row in board]
        self.rows: int = len(board)
        self.cols: int = len(board[0])


    def territory(self, x, y) -> tuple[str, set[tuple[int, int]]]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            raise ValueError("Invalid coordinate")

        if self.board[y][x] in {WHITE, BLACK}:
            return NONE, set()

        queue: deque[tuple[int, int]] = deque([(y, x)])
        visited: set[tuple[int, int]] = {(y, x)}
        bordering_stones: set[str] = set()

        while queue:
            row, col = queue.popleft()

            for dr, dc in DELTAS:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                    continue

                piece = self.board[nr][nc]

                if piece == NONE and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                elif piece in {WHITE, BLACK}:
                    bordering_stones.add(piece)

        territory_points = {(col, row) for row, col in visited}

        if len(bordering_stones) == 1:
            return bordering_stones.pop(), territory_points

        return NONE, territory_points

    def territories(self) -> dict[str, set[tuple[int, int]]]:
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        visited: set[tuple[int, int]] = set()
        result: dict[str, set[tuple[int, int]]] = {
            WHITE: set(),
            BLACK: set(),
            NONE: set()
        }

        for row_index in range(self.rows):
            for col_index in range(self.cols):
                if self.board[row_index][col_index] == NONE and (row_index, col_index) not in visited:
                    stone, territory = self.territory(col_index, row_index)
                    result[stone] = result.get(stone, set()).union(territory)
                    visited = visited.union(territory)
        return result
