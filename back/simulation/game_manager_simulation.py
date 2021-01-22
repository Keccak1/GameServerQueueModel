from time import sleep
from random import randint

from .game_events_generator import GameManagerEventsGenerator
from .game_simulation_reporter import GameSimulatorReporter

class GameManagerSimulation:
    def __init__(self, manager, report=False):
        self._manager = manager
        self._reporter = GameSimulatorReporter() if report else None
        self._generator = GameManagerEventsGenerator(manager)

    @property
    def manager(self):
        return self._manager

    def add_event(self, event):
        self._manager.add_event(event)

    @staticmethod
    def _sleep(time_range):
        if time_range:
            time_min, time_max = time_range
            time.sleep(randint(time_min, time_max))

    def _report(self, record):
        if reporter:
            reporter.add_record(record)
        
    def simulate(self, iter, time_range = None):
        self._reporter.reset()
        for i in range(iter):
            record = self._generator.next_event(), self._manager.to_dict()
            GameManagerSimulation._sleep(time_range)
            _report(record)
            yield record
