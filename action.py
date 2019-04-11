from Sentinel.dice import Dice, DicePool

class Action:
    def __init__(self, context={}):
        self.dice_pool = None
        self.context = context
        self.on_stack = []
        self.before_dice_roll = []
        self.after_dice_roll = []
        self.after_resolution = []
        self.process_context()

    def process_context(self):
        pass

    def execute(self):
        for fxn in self.before_dice_roll:
            fxn(self.context)
        self.roll_dice()
        for fxn in self.after_dice_roll:
            fxn(self.context)
        self.execute_internals()
        for fxn in self.after_resolution:
            fxn(self.context)

    def execute_internals(self):
        #virtual method
        assert False

    def roll_dice(self):
        if self.dice_pool is None:
            return None
        elif type(self.dice_pool) == Dice:
            # single die
            pass
        elif type(self.dice_pool) == DicePool:
            # multiple dice
            pass


    def roll_dice(self):
        #virtual method
        assert False


class Attack(Action):
    def __init__(self, context={}):
        super().__init__(context=context)

    def process_context(self):
        self.target = self.context['target']
        self.source = self.context['source']
        self.dice_pool = self.context['dice pool']
        self.types = self.context['damage types']



    def execute(self):
        dam_val = self.pool.roll()
        self.target.take_damage(dam_val)