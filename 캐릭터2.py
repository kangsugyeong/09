class Game:
    def __init__(self, name, sex, job):
        self.game_id = name
        self.game_sex = sex
        self.game_job = job
    def fight(self, 상대방_id):
            print(self.game_id + "이가 " + 상대방_id + "를 공격해요!")


my_game = Game("수경", "여", "매니저")
my_game.fight("아진이")