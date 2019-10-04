"""
TODO: EN doc
"""


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.__count = 0

    def hash_fun(self, key):
        # TODO: EN doc
        return sum(key.encode()) % self.size

    def __get_collision_sub_slot(self, slot, key):
        if self.slots[slot] is not None:
            subSlot_ = next(filter(
                    lambda x: x[1] == key,
                    enumerate(self.slots[slot])),
                    None)
            return subSlot_[0] if subSlot_ else None

    def __get_least_hits_slot(self):
        return min((slot for slot in range(self.size)
                    if self.slots[slot] is not None),
                   key=lambda slot: min(self.hits[slot]))

    def __clear_slot(self, slot, sub_slot):
        subSlots = self.hits[slot]
        if len(subSlots) == 1:
            self.slots[slot] = None
            self.values[slot] = None
            self.hits[slot] = 0
        else:
            self.slots[slot].pop(sub_slot)
            self.values[slot].pop(sub_slot)
            self.hits[slot].pop(sub_slot)
        self.__count -= 1

    def is_key(self, key):
        slot = self.hash_fun(key)
        return self.__get_collision_sub_slot(slot, key) is not None

    def put(self, key, value):
        slot = self.hash_fun(key)
        subSlot = self.__get_collision_sub_slot(slot, key)

        if subSlot is None:
            if self.__count == self.size:
                minHitsSlot = self.__get_least_hits_slot()
                minHits = min(self.hits[minHitsSlot])
                minHitsSubSlot = self.hits[minHitsSlot].index(minHits)
                self.__clear_slot(minHitsSlot, minHitsSubSlot)

            if self.slots[slot] is None:
                subSlot = 0
                self.slots[slot] = [key]
                self.hits[slot] = [0]
                self.values[slot] = ['<placeholder>']
            else:
                subSlot = len(self.slots[slot])
                self.slots[slot].append(key)
                self.hits[slot].append(0)
                self.values[slot].append('<placeholder>')
            self.__count += 1

        self.values[slot][subSlot] = value

    def get(self, key):
        slot = self.hash_fun(key)
        subSlot = self.__get_collision_sub_slot(slot, key)
        if subSlot is not None:
            self.hits[slot][subSlot] += 1
            return self.values[slot][subSlot]

    @classmethod
    def create(cls, sz: int, vals: dict):
        instance = cls(sz)
        for k, v in vals.items():
            instance.put(k, v)
        return instance

