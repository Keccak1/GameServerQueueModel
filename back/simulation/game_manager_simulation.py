from time import sleep

from .game_events_generator import GameManagerEventsGenerator


class GameManagerSimulation:
    def __init__(self, manager):
        self._manager = manager
        self._generator = GameManagerEventsGenerator(manager)

    @property
    def manager(self):
        return self._manager

    def add_event(self, event):
        self._manager.add_event(event)

    def simulate(self, iter, time_range):
        time_min, time_max = time_range
        for i in range(iter):
            if i:
                time.sleep(time_min, time_max)
            yield self._generator.next_event()
