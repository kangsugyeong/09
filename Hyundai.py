class Game:
    def __init__(self, name, sex, job):
        self.game_id = name
        self.game_sex = sex
        self.game_job = job
    def fight(self):
            print(self.game_id + self.game_job + " 공격!")


my_game = Game("강수경", "여", "매니저")
my_game.fight()