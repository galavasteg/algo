from random import shuffle

from heap_19.heap import Heap


Heap.__repr__ = lambda x: 'BST r:%s c:%s' % (
    x.HeapArray[0], len(x.HeapArray))


# --------------------------- TESTS ---------------------------------

h = Heap()
h._array_init(depth=3)
test_a = [
        11,
        9, 4,
        7, 8, 3, 1,
        2, 5, 6, None, None, None, None, None,
    ]
assert len(test_a) == len(h.HeapArray)
h.HeapArray = test_a
assert h.GetMax() == 11
assert h.HeapArray[0] == 9
assert 11 not in h.HeapArray
assert h.GetMax() == 9
assert h.HeapArray[0] == 8
assert 9 not in h.HeapArray
assert h.HeapArray == [
        8,
        7, 4,
        5, 6, 3, 1,
        2, None, None, None, None, None, None, None,
    ]

test_a = [
        11,
        4, 9,
        3, 1, 7, 8,
        None, None, None, None, 2, 5, 6, None,
    ]
assert len(test_a) == len(h.HeapArray)
h.HeapArray = test_a
assert h.GetMax() == 11
assert h.HeapArray[0] == 9
assert 11 not in h.HeapArray
assert h.GetMax() == 9
assert h.HeapArray[0] == 8
assert 9 not in h.HeapArray
assert h.HeapArray == [
        8,
        4, 7,
        3, 1, 5, 6,
        None, None, None, None, 2, None, None, None,
    ]

test_a = [
        11,
        None, None,
        None, None, None, None,
        None, None, None, None, None, None, None, None,
    ]
assert len(test_a) == len(h.HeapArray)
h.HeapArray = test_a
assert h.GetMax() == 11
assert h.HeapArray[0] is None
assert h.HeapArray == [None] * len(test_a)

assert h.GetMax() == -1


