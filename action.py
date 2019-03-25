class Action:

    def execute(self):
        #virtual method
        assert False


class Attack(Action):
    def __init__(self, context={}):
        pass