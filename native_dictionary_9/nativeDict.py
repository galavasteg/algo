"""
TODO: EN doc
"""


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    @staticmethod
    def hash(s: str, sz: int):
        return sum(s.encode()) % sz

    def hash_fun(self, key):
        return self.hash(key, self.size)

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        i = self.hash_fun(key)
        self.slots[i] = key
        self.values[i] = value

    def get(self, key):
        if self.is_key(key):
            i = self.hash_fun(key)
            return self.values[i]

    @classmethod
    def create(cls, sz: int, vals: dict):
        instance = cls(sz)
        for k, v in vals.items():
            instance.put(k, v)
        return instance

