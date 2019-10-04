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


