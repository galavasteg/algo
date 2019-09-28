"""
TODO: EN doc
"""


# TODO: EN doc
class PowerSet:
    def __init__(self):
        self.sz = 20000
        self.slots = [None] * self.sz

    def hash_fun(self, value):
        # TODO: EN doc
        bStr = value.encode()
        return int('0' + ''.join(str(b) for b in bStr)) % self.sz

    def size(self):
        # TODO: EN doc
        return len(self.get_vals())

    def get(self, value):
        # TODO: EN doc
        i = self.hash_fun(value)
        return self.slots[i] is not None

    def put(self, value):
        # TODO: EN doc
        i = self.hash_fun(value)
        self.slots[i] = value
        return i

    def remove(self, value):
        # TODO: EN doc
        i = self.hash_fun(value)
        is_rm = False
        if self.slots[i] is not None:
            self.slots[i] = None
            is_rm = True
        return is_rm

    def intersection(self, set2):
        # TODO: EN doc
        intersection_vals = tuple(v1 for v1, v2 in
                                  zip(self.slots, set2.slots)
                                  if v1 is not None and v1 == v2)
        return self.create(intersection_vals)

    def union(self, set2):
        # TODO: EN doc
        union_vals = self.get_vals() + set2.get_vals()
        return self.create(union_vals)

    def difference(self, set2):
        # TODO: EN doc
        diff_vals = tuple(v1 for v1, v2
                          in zip(self.slots, set2.slots)
                          if v1 is not None and v1 != v2)
        return self.create(diff_vals)

    def issubset(self, set2):
        # TODO: EN doc
        equal_vals = tuple(self.slots[i] == v2 for i, v2 in
                           enumerate(set2.slots)
                           if v2 is not None)
        return all(equal_vals)

    def get_vals(self):
        return tuple(filter(lambda x: x is not None, self.slots))

    @classmethod
    def create(cls, vals):
        p_set = cls()
        for v in vals:
            p_set.put(v)
        return p_set

