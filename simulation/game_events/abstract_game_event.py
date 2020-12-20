from abc import ABC, abstractmethod


class AbstractGameEvent(ABC):

    def __init__(self, manager, **kwargs):
        self._manager = manager

    @abstractmethod
    def trigger(self, **kwargs):
        pass

    def can_trigger(self, **kwargs):
        return True

    def __call__(self):
        if self.can_trigger():
            return self.trigger()
        raise Exception("Cannot invoke function")
