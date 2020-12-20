class GameSimulatorRecoderd:
    def __init__(self):
        self._records = {}

    @property
    def records(self):
        return self._records

    def add_record(self, i, record):
        self._records[i] = record

    def check_chance(self, condition):
        true_counter = 0
        for i in self._records.values():
            if condition(i):
                true_counte += 1
        return true_counter/len(self._records)
