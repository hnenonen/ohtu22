class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            pass

    def get_score(self):
      if self.player1_score == self.player2_score:
          return self.even_score()
      elif max(self.player1_score, self.player2_score) >= 4:
          return self.setpoint()
      return self.print_score()

    def even_score(self):
        if self.player1_score >= 4:
            return "Deuce"
        return f"{self.score_names[self.player1_score]}-All"

    def uneven_score(self):
        if self.player1_score > self.player2_score:
            return self.player1_name
        elif self.player1_score < self.player2_score:
            return self.player2_name
        else:
            return ''

    def setpoint(self):
        point_diff = abs(self.player1_score - self.player2_score)
        if point_diff == 1:
            return f"Advantage {self.uneven_score()}"
        return f"Win for {self.uneven_score()}"

    def print_score(self):
        return (f"{self.score_names[self.player1_score]}-"
                f"{self.score_names[self.player2_score]}")

  