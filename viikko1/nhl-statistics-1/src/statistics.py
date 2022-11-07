from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def sort_by_points(player):
    return player.points


def sort_by_goals(player):
    return player.goals


def sort_by_assists(player):
    return player.assists


class Statistics:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sortby=SortBy.POINTS):
        if sortby == SortBy.POINTS:
            key = sort_by_points
        elif sortby == SortBy.GOALS:
            key = sort_by_goals
        else:
            key = sort_by_assists
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=key
        )

        players = []
        for i in range(0, how_many):
            players.append(sorted_players[i])

        return players
