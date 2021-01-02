from .util import to_iterarable
from .game_element import GameElement

class Player(GameElement):
    
    def __init__(self, name, regions):
        super().__init__
        self._name = name
        self._regions = set(regions)

    def __repr__(self):
        return f"Name: {self.name}, regions: {self.regions}"

    
    @property
    def name(self):
        return self._name

    @property
    def regions(self):
        return self._regions

    def to_dict(self):
        return {"name": self.name, "regions": list(self.regions)}

