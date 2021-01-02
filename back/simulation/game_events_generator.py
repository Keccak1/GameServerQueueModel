class GameManagerEventsGenerator:

    def __init__(self,manager):
        self._manager = manager
        self._events = []

    @property
    def manager(self):
        return self._manager

    def add_event(self, event):
        self._events.append(event)

    def next_event(self):
        allowed_events = list(
            filter(lambda event: event.can_trigger(), self._evnets))
        if can_trigger:
            return random.choice(allowed_events)()
