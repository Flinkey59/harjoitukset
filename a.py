import random 


class Event:
    def __init__(self, name: str, chance: float, effect: float):
        self.name = name
        self.chance = chance
        self.effect = effect

    def tick(self) -> bool:
        """
        Ticks and checks if event occurs based on its probability of occuring. 
        Event will occur if the randomly generated float is inferior to its probability of occuring.
        """

        return random.random() <= self.chance
