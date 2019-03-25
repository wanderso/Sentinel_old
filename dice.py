import random
from Sentinel.results import ResultGenerator

class Dice:
    def __init__(self, die, context={}):
        self.die = die
        self.context = context
        self.value = None

    def get_context_true(self, from_context):
        if from_context not in self.context:
            return False
        else:
            return self.context[from_context]

    def roll(self):
        self.value = Dice.dn(self.die)
        if self.get_context_true("debug"):
            print ("Die d%d rolled: %d" % (self.die, self.value))
        return self.value

    def increase_die_size(self):
        if self.die == 4:
            self.die = 6
        elif self.die == 6:
            self.die = 8
        elif self.die == 8:
            self.die = 10
        elif self.die == 10:
            self.die = 12

    def decrease_die_size(self):
        if self.die == 6:
            self.die = 4
        elif self.die == 8:
            self.die = 6
        elif self.die == 10:
            self.die = 8
        elif self.die == 12:
            self.die = 10

    def get_die_size(self):
        return self.die

    def get_context(self):
        return self.context

    @staticmethod
    def dn(n):
        return random.randint(1, n)

    @staticmethod
    def ndn(n, m):
        ret_val = 0
        for _ in range(n):
            ret_val += random.randint(1,m)
        return ret_val


class DicePool:
    def __init__(self, dice_list, help_dice=[], hinder_dice=[]):
        self.dice_list = dice_list
        self.help_dice = help_dice
        self.hinder_dice = hinder_dice
        self.core_values = []
        self.modifier = 0
        self.roll()

    def reset_values(self):
        self.core_values = []
        self.help_values = []
        self.hinder_values = []
        self.modifier = 0

    def roll(self):
        self.reset_values()
        for die in self.dice_list:
            self.core_values.append(die.roll())
        for die in self.help_dice:
            self.help_values.append(die.roll())
        for die in self.hinder_dice:
            self.hinder_values.append(die.roll())
        for value in self.help_values:
            self.modifier += ResultGenerator.boost_result(value)
        for value in self.hinder_values:
            self.modifier -= ResultGenerator.boost_result(value)


    def max(self):
        return max(self.core_values) + self.modifier

    def min(self):
        return min(self.core_values) + self.modifier

    def mid(self):
        valx = self.max()
        valn = self.min()
        dummy_list = list(self.core_values)
        dummy_list.remove(valx)
        dummy_list.remove(valn)
        return dummy_list[0] + self.modifier


if __name__ == "__main__":
    print ("Test of the diceroll system.")
    d6 = Dice(6)
    d8 = Dice(8)
    d10 = Dice(10)
    d12 = Dice(12)

    total_iterations = 100000
    value_list = [0,0,0,0,0]

    dp = DicePool([d10,d10,d10], help_dice=[d8])

    for _ in range(0,total_iterations):
        dp.roll()
        value_list[ResultGenerator.overcome_result(dp.max())] += 1

    i = 0
    for entry in value_list:
        print("%s: %.2f%%" % (ResultGenerator.get_result_text_from_value(i), (entry*100)/total_iterations))
        i += 1
