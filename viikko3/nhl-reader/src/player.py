class Player:
    """Object to save player attributes."""
    def __init__(self, player_dict: dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
        self.penalties = player_dict['penalties']
        self.team = player_dict['team']
        self.games = player_dict['games']

    def __str__(self):
        return (f'{self.name:20} '
                f'{self.team} '
                f'{self.goals} + {self.assists}'
                f'= {self.points()}')

    def __lt__(self, other):
        return self.points() < other.points()

    def points(self):
        """Get points of player."""
        return self.goals + self.assists