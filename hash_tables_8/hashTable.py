"""
Implement the four methods of the HashTable class:
- hash_fun (value)
- seek_slot (value) - find the correct slot
- put (value) - put the value in the slot returned by seek_slot
- find (value) - check if the value is in the table.
Write tests for all of these methods.
"""


class HashTable:
    def __init__(self, sz, stp):
        """:param sz: size of table
        :param stp: count of slots for searching of the next free slot.

        **sz** and **stp** have to be coprime numbers
        """

        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    @staticmethod
    def hash(s: str, sz: int):
        return sum(s.encode()) % sz

    def hash_fun(self, value):
        """Always return correct slot index.
        **value** is always string"""
        return self.hash(value, self.size)

    def seek_slot(self, value):
        """Return free slot index or None"""
        hash_i = i = self.hash_fun(value)
        if self.slots[i] is not None:
            i = (hash_i + self.step) % self.size
            while self.slots[i] is not None and hash_i != i:
                i = (i + self.step) % self.size
        if self.slots[i] is None:
            return i

    def put(self, value):
        """Return slot index of put **value** or
        None if **value** is impossible to put
        because of collisions"""
        i = self.seek_slot(value)
        if i is not None:
            self.slots[i] = value
        return i  # None or int

    def find(self, value):
        """Return **value**'s slot index or None"""
        if value in self.slots:
            return self.slots.index(value)

    @classmethod
    def create(cls, sz: int, stp: int, vals: tuple):
        ht = cls(sz, stp)
        for v in vals:
            ht.put(v)
        return ht

