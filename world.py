class World:
    def __init__(self):
        self.environment_list = []
        self.scene_tracker = None
        self.entity_tracker = []
        self.active_entity = None

    def add_entity(self, entity, ambush=False):
        new_tracker = TrackEntity(entity, ambush=ambush)
        self.entity_tracker.append(new_tracker)

    def set_scene_tracker(self, green, yellow, red):
        self.scene_tracker = SceneTracker(green, yellow, red)

    def get_scene_tracker(self):
        return self.scene_tracker

    def hand_off(self, entity_now):
        if self.active_entity != None:
            self.active_entity.set_acted(True)
        self.active_entity = entity_now


class TrackEntity:
    def __init__(self, entity, ambush=False):
        self.entity = entity
        self.acted = ambush

    def set_acted(self, acted):
        self.acted = acted


class SceneTracker:
    def __init__(self, green, yellow, red):
        assert (green >= 0) and (yellow >= 0) and (red >= 0)
        self.tracker = []
        for _ in range(0, green):
            self.tracker.insert("Green")
        for _ in range(0, yellow):
            self.tracker.insert("Yellow")
        for _ in range(0, red):
            self.tracker.insert("Red")

    def get_tracker(self):
        if len(self.tracker) == 0:
            return "Red"
        return self.tracker[-1]

    def advance_tracker(self):
        if len(self.tracker) == 0:
            return "End of Scene"
        self.tracker.pop()





