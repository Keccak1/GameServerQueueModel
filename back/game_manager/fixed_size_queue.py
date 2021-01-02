from collections import deque


class FixedSizeQueue:

    def __init__(self, maxlen):
        self._q = deque(maxlen=maxlen)

    def __iter__(self):
        return iter(self._q)

    def __next__(self):
        return next(self._q)

    def __getitem__(self, index):
        return self._q.__getitem__(index)

    @property
    def capacity(self):
        return self._q.maxlen

    @property
    def size(self):
        return len(self._q)

    def can_push(self):
        return self.size + 1 <= self.capacity

    def free_places(self):
        return self.capacity - len(self._q)

    def copy(self):
        return self._q.copy()

    def can_pop(self):
        return self.size >= 1

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.capacity

    def push(self, i):
        can_push = self.can_push()

        if can_push:
            self._q.append(i)

        return can_push, self.copy()

    def pop(self):
        ret = None

        if self.can_pop():
            ret = self._q.pop()

        return ret

    def clear(self):
        self._q.clear()

    def push_range(self, r):
        to_add = min(len(list(r)), self.free_places())

        for i in to_add:
            self.push(i)

        return len(to_add) == len(r), self.copy()

    def pop_n(self, n):
        can_pop_amount = min(n, self.size)
        popped = []

        for _ in range(n):
            popped.append(self.pop())
            
        return can_pop_amount == n, self.copy()

    def remove(self, i):
        status = True
        try:
            self._q.remove(i)
        except ValueError:
            status = False

        return status, self.copy()

    def find_by_lambda(self, f):
        return list(filter(f, list(self._q)))

    def remove_lambda(self, f):
        to_remove = self.find_by_lambda(f)
        for i in to_remove:
            self._q.remove(i)

        return len(to_remove) != 0,  self.copy()