class GameSimulatorReporter:
    def __init__(self):
        self._records = []

    @property
    def records(self):
        return self._records

    def reset(self):
        self._records = []

    def add_record(self, i, record):
        self._records.append(record)

    def filter_events(self, condition):
        return list(filter(condition, self._records))
        
    def check_chance(self, condition):
        return len(filter_events) / len(self._records)