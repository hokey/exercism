"""
Tic Tac Toe Library
"""

from collections import Counter

WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

CHIT_PIECES = {"X", "O", " "}

def gamestate(board: list[str]) -> str:
    if (
        not isinstance(board, list)
        or len(board) != 3
        or any(not isinstance(row, str) or len(row) != 3 for row in board)
    ):
        raise ValueError("Board must be a list of three strings of length 3")

    flat = board[0] + board[1] + board[2]

    if any(chit not in CHIT_PIECES for chit in flat):
        raise ValueError("Invalid character on board")

    chits = Counter(flat)

    if chits["O"] > chits["X"]:
        raise ValueError("Wrong turn order: O started")
    if chits["X"] - chits["O"] > 1:
        raise ValueError("Wrong turn order: X went twice")

    x_wins = o_wins = 0
    for one, two, three in WIN_LINES:
        cell = flat[one]
        if cell != " " and cell == flat[two] == flat[three]:
            if cell == "X":
                x_wins += 1
            else:
                o_wins += 1

    if x_wins or o_wins:
        if x_wins == o_wins:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"

    if chits["X"] == 5 and chits["O"] == 4:
        return "draw"

    return "ongoing"
