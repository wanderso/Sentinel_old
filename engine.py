import Sentinel.action as Action
import Sentinel.character as Character
import Sentinel.dice as Dice
import Sentinel.objective as Objective
import Sentinel.results as Sentinel
import Sentinel.world as World

class Engine:
    def __init__(self):
        self.world = World.World()

    def add_character_to_world(self, chara, context={}):
        ambush = False
        if 'ambush' in context:
            ambush = context['ambush']
        self.world.add_entity(chara, ambush=ambush)



if __name__ == "__main__":
    pass