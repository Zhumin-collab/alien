class Gamestats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = False
        self.score = 0
        file_path = "high_score/high_score.txt"
        with open(file_path) as file_object:
            lines = file_object.readlines()
        pi_string = ""
        for line in lines:
            pi_string += line.strip()
        self.high_score = int(pi_string)
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
