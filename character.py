class Character:
    def __init__(self, name, context={}):
        self.abilities = []
        self.name = name

    def take_damage(self):
        #virtual method
        assert False

    def heal_damage(self):
        assert False

    def perform_action(self):
        pass

class Minion(Character):
    def __init__(self, name, context={}):
        super().__init__(name, context=context)
        self.max_die = context['die']