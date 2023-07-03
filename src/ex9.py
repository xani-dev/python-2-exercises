import random


class Character:

    def __init__(self, hit_points):
        self.hit_points = hit_points

    def fight(self, character):
        random_number = random.randint(1, 20)

        character.hit_points -= random_number
        if self.hit_points < 0:
            character.hit_points = 0
            print('game is over')


class Fighter(Character):
    def __repr__(self):
        return f'Fighter: {self.hit_points} hit points'
    pass


class Dwarf(Character):
    def __repr__(self):
        return f'Dwarf: {self.hit_points} hit points'
    pass


f = Fighter(18)
d = Dwarf(15)
print(f)
print(d)
f.fight(d)
d.fight(f)
print(f)
print(d)
