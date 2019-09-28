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
        hash_i = i = self.hash_fun(value)
        collisionsInds = [hash_i]
        while self.slots[i] is not None and hash_i != i:
            collisionsInds.append(i)
            i = self.get_next_index(i)
        return any(self.slots[i] == value for i in collisionsInds)

    def _get_exist_val_index(self, value):
        i = self.hash_fun(value)
        while self.slots[i] != value:
            i = self.get_next_index(i)
        return i

    def seek_slot(self, value):
        # TODO: doc
        hash_i = i = self.hash_fun(value)
        if self.slots[i] is not None:
            i = self.get_next_index(hash_i)
            while self.slots[i] is not None and hash_i != i:
                i = self.get_next_index(i)
        if self.slots[i] is None:
            return i
        # None if set is overflow

    def put(self, value):
        # TODO: EN doc
        if self.get(value):
            i = self._get_exist_val_index(value)
        else:
            i = self.seek_slot(value)
            if i is not None:
                self.slots[i] = value
        # ind of new/existing val, None if set is overflow
        return i

    def remove(self, value):
        # TODO: EN doc
        is_rm = False
        if self.get(value):
            i = self._get_exist_val_index(value)
            self.slots[i] = None
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

