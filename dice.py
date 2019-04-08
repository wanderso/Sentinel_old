import random
from Sentinel.results import ResultGenerator

class Dice:
    def __init__(self, die, context={}):
        self.die = die
        self.context = context
        self.boost = 0
        self.value = None

    def __gt__(self, other):
        return self.get_value() > other.get_value()

    def __eq__(self, other):
        return self.get_value == other.get_value()

    def __lt__(self, other):
        return self.get_value() < other.get_value()

    @classmethod
    def copy_die(cls, die):
        retval = cls(die.get_die_size(), context=die.get_context())
        retval.value = retval.value
        retval.boost = die.boost
        return retval

    def get_context_true(self, from_context):
        if from_context not in self.context:
            return False
        else:
            return self.context[from_context]

    def get_value(self):
        return self.value + self.boost

    def roll(self):
        self.value = Dice.dn(self.die)
        if self.get_context_true("debug"):
            print("Die d%d rolled: %d" % (self.die, self.value))
        return self.value + self.boost

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
        self.dice_list = []
        self.help_dice = []
        self.hinder_dice = []

        for die in dice_list:
            self.dice_list.append(Dice.copy_die(die))
        for die in help_dice:
            self.help_dice.append(Dice.copy_die(die))
        for die in hinder_dice:
            self.hinder_dice.append(Dice.copy_die(die))

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
            die.roll()
        self.dice_list.sort()
        for die in self.help_dice:
            die.roll()
        self.help_dice.sort()
        for die in self.hinder_dice:
            die.roll()
        self.hinder_dice.sort()
        self.calculate_modifier()

    def calculate_modifier(self):
        self.modifier = 0
        for die in self.help_dice:
            self.modifier += ResultGenerator.boost_result(die.get_value())
        for die in self.hinder_dice:
            self.modifier -= ResultGenerator.boost_result(die.get_value())

    def max_val(self):
        return self.max_die().get_value() + self.modifier

    def min_val(self):
        return self.min_die().get_value() + self.modifier

    def mid_val(self):
        return self.mid_die().get_value() + self.modifier

    def max_die(self):
        return self.dice_list[-1]

    def mid_die(self):
        return self.dice_list[1]

    def min_die(self):
        return self.dice_list[0]



if __name__ == "__main__":
    print("Test of the diceroll system.")
    d6 = Dice(6)
    d8 = Dice(8)
    d10 = Dice(10)
    d12 = Dice(12)

    total_iterations = 100000
    value_list = [0, 0, 0, 0, 0]

    dp = DicePool([d10, d10, d10], help_dice=[d12])

    print("Is d6 > d12?")
    d6.roll()
    d12.roll()

    for _ in range(0, total_iterations):
        dp.roll()
        value_list[ResultGenerator.overcome_result(dp.max_val())] += 1

    i = 0
    for entry in value_list:
        print("%s: %.2f%%" % (ResultGenerator.get_result_text_from_value(i), (entry*100)/total_iterations))
        i += 1
