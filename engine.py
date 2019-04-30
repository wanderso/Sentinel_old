import Sentinel.action as Action
import Sentinel.character as Character
import Sentinel.dice as Dice
import Sentinel.objective as Objective
import Sentinel.results as Sentinel
import Sentinel.world as World

class Engine:
    def __init__(self):
        self.world = World.World()

    def add_character(self, chara, context={}):
        ambush = False
        if 'ambush' in context:
            ambush = context['ambush']
        self.world.add_entity(chara, ambush=ambush)

    def start_scene(self, green, yellow, red):
        self.world.set_scene_tracker(green, yellow, red)
        self.world.reset_turn()



if __name__ == "__main__":

    world_engine = Engine()

    d1 = Dice.Dice(6, context={'debug': True})
    d2 = Dice.Dice(8, context={'debug': True})
    m1 = Character.Minion("Combat Network Teuer", d1)
    m2 = Character.Minion("Silens Combat Drone", d2)
    m3 = Character.Minion("Silens Combat Drone", d2)
    m4 = Character.Minion("Combat Network Teuer", d1)

    world_engine.add_character(m1)
    world_engine.add_character(m2)
    world_engine.add_character(m3)
    world_engine.add_character(m4)

    world_engine.start_scene(2, 4, 2)

    print(world_engine.world)

