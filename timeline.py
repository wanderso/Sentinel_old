class Scene:
    def __init__(self):
        self.start_of_scene = []
        self.end_of_scene = []


class Turn:
    def __init__(self):
        self.start_of_turn = []
        self.actions_on_turn = []
        self.end_of_turn = []

        self.actions_taken = []

        self.character = None


class CharacterTimeline:
    def __init__(self, character, scene=None):
        self.scene = scene
        self.character = character
        self.turns = []
        self.turn_index = 0

    def access_turn(self, distance_from_index=0):
        length_of_turns = len(self.turns)
        if length_of_turns >= self.turn_index + distance_from_index:
            pass


class FullTimeline:
    def __init__(self):
        self.turns = []

    def add_turn(self, turn):
        self.turns.append(turn)