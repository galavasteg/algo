"""
Implement next methods of the class:
 - put(key, value)
 - is_key(key)
 - get(key).
 Write tests:
 - put the value of an existing key or new,
 - checking for the presence and absence of keys,
 - retrieving a value for an existing and missing key.
 Size of the dictionary not changes.
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
        """Always return correct slot index.
        **key** is always string"""
        return self.hash(key, self.size)

    def is_key(self, key):
        """Check if the **key** is in the dictionary"""
        return key in self.slots

    def put(self, key, value):
        """Put **value** in the slot corresponding
        to the **key** hash"""
        i = self.hash_fun(key)
        self.slots[i] = key
        self.values[i] = value

    def get(self, key):
        """Return **key**'s value or None if **key**
        does not exist in the dictionary"""
        if self.is_key(key):
            i = self.hash_fun(key)
            return self.values[i]

    @classmethod
    def create(cls, sz: int, vals: dict):
        instance = cls(sz)
        for k, v in vals.items():
            instance.put(k, v)
        return instance

