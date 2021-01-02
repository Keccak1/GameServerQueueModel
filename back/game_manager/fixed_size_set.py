class FixedSizeSet:

    def __init__(self, maxlen):
        self._maxlen = maxlen
        self._s = set()

    def __iter__(self):
        return iter(self._s)

    def __next__(self):
        return next(self._s)

    def __repr__(self):
        return f"{repr(self._s)} max size: {self._maxlen}"

    @property
    def maxlen(self):
        return self._maxlen

    @property
    def size(self):
        return len(self._s)

    def full(self):
        return self.maxlen == self.size

    def empty(self):
        return len(self._s) == 0

    def copy(self):
        return self._s.copy()

    def update(self, rhs):
        self._s.update(rhs)

    def free_places(self):
        return self.maxlen - self.size

    def has_place(self):
        return self.free_places() > 0

    def add(self, i):
        return self.add_range([i])

    def add_range(self, l):
        free_places = min(len(l), self.free_places())
        to_add = set(l[:free_places])
        self._s.update(to_add)
        return len(to_add) == len(l), self.copy()

    def clear(self):
        self._s.clear()

    def remove(self, i):
        status = True
        try:
            self._s.remove(i)
        except ValueError:
            status = False
            
        return status, self.copy()

    def find_by_lambda(self, f):
        return set(filter(f, self._s))
    
    def remove_lambda(self, f):
        to_remove = self.find_by_lambda(f)
        self._s -= to_remove
        return len(to_remove) != 0, self.copy()
