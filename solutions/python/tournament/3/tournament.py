"""
Tournament Tally
"""
from dataclasses import dataclass

POINT_MAP: dict[str, int] = {
    "win": 3,
    "draw": 1,
    "loss": 0
}

@dataclass
class Team:
    """
    Team class
    """
    name: str
    played: int = 0
    wins: int = 0
    draws: int = 0
    losses: int = 0
    points: int = 0
    
def tally(rows: list[str]) -> list[str]:
    """
    Given the results of tournament matches, determing the standings
    :param list[str] rows: The semi-colon delimited list of match results
    :return list[str]: Formate table of the team standings
    """
    teams: dict[str, Team] = {}
    for row in rows:
        row_pieces = row.split(";")
        home = row_pieces[0]
        away = row_pieces[1]
        result = row_pieces[2]
        if result not in POINT_MAP:
            raise ValueError(f"Must be a valid result: {POINT_MAP.keys()}")

        teams.setdefault(home, Team(home))
        teams.setdefault(away, Team(away))
        teams[home].played += 1
        teams[away].played += 1
        if result == "win":
            teams[home].points += POINT_MAP[result]
            teams[home].wins += 1
            teams[away].losses += 1
        elif result == "loss":
            teams[away].points += POINT_MAP["win"]
            teams[away].wins += 1
            teams[home].losses += 1
        else:
            teams[home].points += POINT_MAP[result]
            teams[away].points += POINT_MAP[result]
            teams[away].draws += 1
            teams[home].draws += 1
    sorted_teams: list[str] = sorted(
        teams.items(),
        key=lambda item: (-item[1].points, item[0])
    )
    standings: list[str] = ["Team                           | MP |  W |  D |  L |  P"]
    for _, team in sorted_teams:
        standings.append(" | ".join([
            team.name.ljust(30, " "), 
            str(team.played).rjust(2, " "),
            str(team.wins).rjust(2, " "),
            str(team.draws).rjust(2, " "),
            str(team.losses).rjust(2, " "),
            str(team.points).rjust(2, " ")
        ]))
    return standings