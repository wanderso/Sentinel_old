import random

class Dice:
    def __init__(self, die, context={}):
        self.die = die
        self.context=context
        self.value = self.roll()

    def roll(self):
        return Dice.dn(self.die)

    @staticmethod
    def dn(n):
        return random.randint(1, n)

    @staticmethod
    def ndn(n, m):
        ret_val = 0
        for _ in range(n):
            ret_val += random.randint(1,m)
        return ret_val

class Dice_Pool:
    def __init__(self, dice_list):
        pass