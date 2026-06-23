"""Go Counting Utility"""

from collections import deque

WHITE = "W"
BLACK = "B"
NONE = " "

DELTAS = [
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 0),
]


class Board:
    """Count territories of each player in a Go game."""

    def __init__(self, board: list[str]):
        if not board:
            raise ValueError("Board must not be empty")

        if any(len(row) != len(board[0]) for row in board):
            raise ValueError("Board must have rows of equal length")

        if any(piece not in {WHITE, BLACK, NONE} for row in board for piece in row):
            raise ValueError("Invalid board piece")

        self.board = [list(row) for row in board]
        self.rows = len(board)
        self.cols = len(board[0])

    def territory(self, x: int, y: int) -> tuple[str, set[tuple[int, int]]]:
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            raise ValueError("Invalid coordinate")

        if self.board[y][x] in {WHITE, BLACK}:
            return NONE, set()

        queue = deque([(y, x)])
        visited = {(y, x)}
        bordering_stones = set()

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
        result = {
            WHITE: set(),
            BLACK: set(),
            NONE: set(),
        }

        visited = set()

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == NONE and (row, col) not in visited:
                    owner, points = self.territory(col, row)
                    result[owner].update(points)

                    visited.update((y, x) for x, y in points)

        return result