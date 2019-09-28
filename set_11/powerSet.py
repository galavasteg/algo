"""
TODO: EN doc
"""


# TODO: EN doc
class PowerSet:
    def __init__(self):
        self.sz, self.stp = 20000, 71
        self.slots = [None] * self.sz

    def hash_fun(self, value):
        # TODO: EN doc
        bStr = value.encode()
        return int('0' + ''.join(str(b) for b in bStr)) % self.sz

    def size(self):
        # TODO: EN doc
        return len(self.get_vals())

    def get_next_index(self, ind):
        return (ind + self.stp) % self.sz

    def get(self, value):
        # TODO: EN doc
        isExist = False
        hash_i = self.hash_fun(value)
        if self.slots[hash_i] == value:
            isExist = True
        elif self.slots[hash_i] is not None:
            i = self.get_next_index(hash_i)
            while self.slots[i] is not None and hash_i != i:
                if self.slots[i] == value:
                    isExist = True
                    break
                i = self.get_next_index(i)
        return isExist

    def put(self, value):
        # TODO: EN doc
        # get existing/new *value* slot
        valueSlot = None
        hash_i = i = self.hash_fun(value)
        if self.slots[hash_i] == value:
            valueSlot = hash_i
        elif self.slots[hash_i] is not None:
            i = self.get_next_index(hash_i)
            while self.slots[i] is not None and hash_i != i:
                if self.slots[i] == value:
                    valueSlot = i
                    break
                i = self.get_next_index(i)
        # if there is a free slot
        if valueSlot is None and self.slots[i] is None:
            self.slots[i] = value
            valueSlot = i
        # slot of existing/new *value* or None (if set is overflow)
        return valueSlot

    def _get_last_collision_slot(self, hash_i, from_i):
        lastCollisionSlot = from_i
        i = self.get_next_index(hash_i)
        while (self.slots[i] is not None and  # slot is busy
               # there are free slots <= step is prime for size
               hash_i != i):
            # hash of value in i-slot equal to *hash_i*
            if self.hash_fun(self.slots[i]) == hash_i:
                lastCollisionSlot = i
            i = self.get_next_index(i)
        return lastCollisionSlot

    def remove(self, value):
        # TODO: EN doc
        is_rm, valueSlot, hash_i = False, None, self.hash_fun(value)
        if self.slots[hash_i] == value:
            valueSlot = hash_i
        elif self.slots[hash_i] is not None:
            i = self.get_next_index(hash_i)
            while self.slots[i] is not None and hash_i != i:
                if self.slots[i] == value:
                    valueSlot = i
                    break
                i = self.get_next_index(i)

        if valueSlot is not None:
            lastCollisionSlot = self._get_last_collision_slot(hash_i, valueSlot)
            # replace value in last collision slot to slot of exiting
            self.slots[valueSlot] = self.slots[lastCollisionSlot]
            self.slots[lastCollisionSlot] = None
            is_rm = True
        return is_rm

    def intersection(self, set2):
        # TODO: EN doc
        vals1, vals2 = self.get_vals(), set2.get_vals()
        intersection_vals = tuple(v1 for v1 in vals1
                                  if v1 in vals2)
        return self.create(intersection_vals)

    def union(self, set2):
        # TODO: EN doc
        union_vals = self.get_vals() + set2.get_vals()
        return self.create(union_vals)

    def difference(self, set2):
        # TODO: EN doc
        vals1, vals2 = self.get_vals(), set2.get_vals()
        diff_vals = tuple(v1 for v1 in vals1
                          if v1 not in vals2)
        return self.create(diff_vals)

    def issubset(self, set2):
        # TODO: EN doc
        vals2 = set2.get_vals()
        if vals2:
            intersection_vals = self.intersection(set2).get_vals()
            vals2 = set2.get_vals()
            equal_vals = tuple(v2 in intersection_vals for v2 in vals2)
        else:
            equal_vals = ()
        return all(equal_vals)

    def get_vals(self):
        return tuple(filter(lambda x: x is not None, self.slots))

    @classmethod
    def create(cls, vals):
        p_set = cls()
        for v in vals:
            p_set.put(v)
        return p_set

