"""
TODO: doc
"""


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    @staticmethod
    def hash(s: str, sz: int):
        return sum(s.encode()) % sz

    def hash_fun(self, value):
        # TODO: doc
        return self.hash(value, self.size)

    def seek_slot(self, value):
        # TODO: doc
        hash_i = i = self.hash_fun(value)
        if self.slots[i] is not None:
            i = (hash_i + self.step) % self.size
            while (self.slots[i] is not None and hash_i != i):
                i = (i + self.step) % self.size
        if self.slots[i] is None:
            return i

    def put(self, value):
        # TODO: doc
        i = self.seek_slot(value)
        if i is not None:
            self.slots[i] = value
        return i  # None or int

    def find(self, value):
        # TODO: doc
        if value in self.slots:
            return self.slots.index(value)

    @classmethod
    def create(cls, sz: int, stp: int, vals: tuple):
        ht = cls(sz, stp)
        for v in vals:
            ht.put(v)
        return ht

