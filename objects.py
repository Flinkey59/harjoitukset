class Cretin:
    def __init__(self, goblin_type: str, goofiness: int):
        self.goblin_type = goblin_type
        self.goofiness = goofiness
    def silliness(self):
        return self.goofiness * 5

grimbler = Cretin('snotnose', 9)
print(grimbler, grimbler.goblin_type, grimbler.goofiness, grimbler.silliness())