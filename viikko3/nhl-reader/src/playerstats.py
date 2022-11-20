class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
 
    def top_scorers_by_nationality(self, nationality):
        players = [player for player in self.reader.get_players()
                   if player.nationality == nationality]
        return sorted(players[:5], reverse=True)