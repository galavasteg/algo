"""
4.4. Write tests for tasks 3.1.-3.2.:
 1) insert:
    - after insertion the capacity is not exceeded;
    - after insertion the capacity is overfill (check if the
      capacity changes correctly);
    - insertion into invalid index;
 2) delete:
    - after deletion the capacity has not changed;
    - after deletion the capacity is reduced (check if the
      capacity changes correctly);
    - deletion from invalid index;
"""

import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    @classmethod
    def create(cls, values: list):
        array = cls()
        for v in values:
            array.append(v)
        return array

    @property
    def fill_percent(self):
        return self.count/self.capacity * 100

    def to_list(self):
        array, end = [], False
        try:
            for v in self.array:
                array.append(v)
        except ValueError:
            pass
        except IndexError:
            pass
        return array

    @property
    def meta(self):
        return (self.to_list(), self.count,
                self.capacity, self.fill_percent)

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """3.1. Insert **itm** into **i**-th position. It shifts
        forward all subsequent objects. Double capacity if it is
        full before insertion. If **i** is equal to count then
        insert **itm** in tail. Check if **i** is in the valid
        range of values.
        """
        if self.count == i:
            self.append(itm)
        else:
            self[i]  # check IndexError
            count = self.count + 1
            if count > self.capacity:
                self.resize(2 * self.capacity)
            move_forward_indices = list(range(i, self.count))
            for ind in move_forward_indices[::-1]:
                self.array[ind + 1] = self.array[ind]
            self.count = self.count + 1
            self.array[i] = itm

    def delete(self, i):
        """3.2. Delete object in **i**-th position. Reduce capacity
        if the array is less than 50% full after deletion. The logic
        of power reduction is as follows: the result of dividing the
        current power by 1.5 is converted to int (without rounding)
        NOTE: minimum capacity is 16"""
        self[i]  # check IndexError
        move_back_indices = list(range(i + 1, self.count))
        for ind in move_back_indices:
            self.array[ind - 1] = self.array[ind]
        self.count = self.count - 1
        capacity = (int(self.capacity / 1.5)
                    if self.capacity > 16 and self.fill_percent < 50 else
                    self.capacity)
        self.resize(capacity if capacity > 16 else 16)

