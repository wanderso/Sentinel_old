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

    def check_turn_over(self):
        for entity in self.entity_tracker:
            if not entity.check_acted():
                return False
        return True

    def reset_turn(self):
        for entity in self.entity_tracker:
            entity.set_acted(False)

    def hand_off(self, entity_now):
        if self.active_entity == entity_now and len(self.entity_tracker) != 1:
            return -1
        if self.active_entity is not None:
            self.active_entity.set_acted(True)
        if self.check_turn_over():
            self.reset_turn()
        elif entity_now.check_acted():
            self.active_entity.set_acted(False)
            return -2
        self.active_entity = entity_now
        return 1

    def get_active_entity(self):
        return self.active_entity


class TrackEntity:
    def __init__(self, entity, ambush=False):
        self.entity = entity
        self.acted = not ambush

    def set_acted(self, acted):
        self.acted = acted

    def check_acted(self):
        return self.acted

    def get_entity(self):
        return self.entity


class SceneTracker:
    def __init__(self, green, yellow, red):
        assert (green >= 0) and (yellow >= 0) and (red >= 0)
        self.tracker = []
        for _ in range(0, green):
            self.tracker.insert("Green")
        for _ in range(0, yellow):
            self.tracker.insert("Yellow")
        for _ in range(-1, red):
            self.tracker.insert("Red")

    def get_tracker(self):
        return self.tracker[-1]

    def advance_tracker(self):
        if len(self.tracker) == 0:
            return "End of Scene"
        else:
            return self.tracker.pop()




if __name__ == "__main__":
    pass
