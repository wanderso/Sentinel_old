class Engine:
    def __init__(self):
        self.world = world.World()
        self.hand_off_required = False
        self.stack = []

    def add_character(self, chara, context={}):
        ambush = False
        if 'ambush' in context:
            ambush = context['ambush']
        timeline = timeline.CharacterTimeline(chara)
        chara.set_timeline(timeline)
        self.world.add_entity(chara, ambush=ambush)

        chara.set_world(self.world)

    def start_scene(self, green, yellow, red):
        self.world.set_scene_tracker(green, yellow, red)
        self.world.reset_turn()

    def execute_turn_split_second(self, turn):
        for entry in turn.get_start_action():
            self.place_action_on_stack(entry)
            self.resolve_action()
        for entry in turn.get_action_taken():
            self.place_action_on_stack(entry)
            self.resolve_action()
        for entry in turn.get_end_action():
            self.place_action_on_stack(entry)
            self.resolve_action()


    def place_action_on_stack(self, action):
        self.stack.append(action)

    def resolve_action(self):
        action = self.stack.pop()
        action.execute()


if __name__ == "__main__":
    world_engine = Engine()

    d6 = dice.Dice(6, context={'debug': True})
    d8 = dice.Dice(8, context={'debug': True})

    m1 = character.Minion("Combat Network Teuer", d6)
    m2 = character.Minion("Silens Combat Drone", d8)
    m3 = character.Minion("Silens Combat Drone", d8)
    m4 = character.Minion("Combat Network Teuer", d6)

    world_engine.add_character(m1)
    world_engine.add_character(m2)
    world_engine.add_character(m3)
    world_engine.add_character(m4)

    world_engine.start_scene(2, 4, 2)

    action1 = action.Attack(context={'target': m1, 'source': m2, 'damage types': ['Physical']})

    world_engine.place_action_on_stack(action1)
    world_engine.resolve_action()

    print(world_engine.world)
