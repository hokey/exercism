"""
Tic Tac Toe Library
"""
from collections import Counter
WIN_LINES = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

def gamestate(board: list[str]) -> str:
    """
    Given a tic tac toe board game state, determine if it's ongoing, a win, or a draw.  Invalid states will be reported.

    :param list[str] board: state of the game board
    :return str: "ongoing", "win", "draw"
    """
    chits = Counter(board[0] + board[1] + board[2])
    
    if chits["O"] > chits["X"]:
        raise ValueError("Wrong turn order: O started")
    if chits["X"] - chits["O"] > 1:
        raise ValueError("Wrong turn order: X went twice")
        
    x_wins = 0
    o_wins = 0
    for line in WIN_LINES:
        if board[line[0][0]][line[0][1]] == board[line[1][0]][line[1][1]] == board[line[2][0]][line[2][1]] and board[line[0][0]][line[0][1]] != " ":
            if board[line[0][0]][line[0][1]] == "X":
                x_wins += 1
            else:
                o_wins += 1
            
    if x_wins + o_wins == 0:
        if chits["X"] == 5 and chits["O"] == 4:
            return "draw"
    else:
        if x_wins == o_wins:
            raise ValueError("Impossible board: game should have ended after the game was won")
        if x_wins + o_wins >= 1:
            return "win"
    return "ongoing"