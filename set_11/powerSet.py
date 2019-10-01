"""
TODO: EN doc
"""


# TODO: EN doc
class PowerSet:
    def __init__(self):
        self.sz = 20000
        self.__slots = tuple([] for _ in range(self.sz))
        self.__count = 0

    def hash_fun(self, value):
        # TODO: EN doc
        bStr = value.encode()
        return int('0' + ''.join(str(b) for b in bStr)) % self.sz

    def size(self):
        # TODO: EN doc
        return self.__count

    def get(self, value):
        # TODO: EN doc
        hash_i = self.hash_fun(value)
        return value in self.__slots[hash_i]

    def put(self, value):
        # TODO: EN doc
        if self.__count < self.sz:
            hash_i = self.hash_fun(value)
            collisions = self.__slots[hash_i]
            if not collisions or value not in collisions:
                self.__slots[hash_i].append(value)
                self.__count += 1

    def remove(self, value):
        # TODO: EN doc
        isRemoved = False
        hash_i = self.hash_fun(value)
        collisions = self.__slots[hash_i]
        if collisions and value in collisions:
            self.__slots[hash_i].remove(value)
            self.__count -= 1
            isRemoved = True
        return isRemoved

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
        return sum((collis for collis in self.__slots if collis), [])

    @classmethod
    def create(cls, vals):
        p_set = cls()
        for v in vals:
            p_set.put(v)
        return p_set

