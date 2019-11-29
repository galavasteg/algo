from random import shuffle

from heap_19.heap import Heap


Heap.__repr__ = lambda x: 'BST r:%s c:%s' % (
    x.HeapArray[0], len(x.HeapArray))


def get_random_heap(depth: int, nodes_count: int) -> Heap:
    h = Heap()
    keys = list(range(nodes_count))
    shuffle(keys)
    h.MakeHeap(keys, depth)
    return h


# --------------------------- TESTS ---------------------------------

def test_get_max():
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


def test_get_level_slots():
    h = Heap()
    h.HeapArray = [
            11,
            9, 4,
            7, 8, 3, 1,
            2, 5, 6, None, None, None, None, None,
        ]
    ks = h._get_bottom_level_slots()
    assert ks == (7, 8, 9, 10, 11, 12, 13, 14)
    s = h._get_bottom_left_free_slot()
    assert s == 10

    h.HeapArray = [
            11,
            9, 4,
            7, 8, 3, 1,
            None, None, None, None, None, None, None, None,
        ]
    ks = h._get_bottom_level_slots()
    assert ks == (3, 4, 5, 6)
    s = h._get_bottom_left_free_slot()
    assert s == 7


def test_add():
    h = Heap()
    h.MakeHeap(list(range(5)), 3)

    h.MakeHeap(list(range(10)), 3)
    assert h.HeapArray == [
            9,
            8, 5,
            6, 7, 1, 4,
            0, 3, 2, None, None, None, None, None,
        ]

    h.MakeHeap(list(range(15)), 3)
    assert h.Add(9) == False
    assert h.HeapArray == [
            14,
            9, 13,
            6, 8, 10, 12,
            0, 3, 2, 7, 1, 5, 4, 11,
        ]
    assert h.Add(100) == False

    h.MakeHeap([0]*15, 3)
    # TODO: is heap correct?
    assert h.Add(9) == False


def test_fill_empty_heap():
    h = Heap()
    h.MakeHeap([14, 13, 12, 11, 6, 8, 10, 2, 9, 3, 0, 1, 5, 4, 7], 3)
    for _ in h.HeapArray:
        assert h.GetMax() >= 0
    assert h.GetMax() == -1


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_get_max()
    test_get_level_slots()
    test_add()
    test_fill_empty_heap()

    for d, n in zip((2, 5, 7, 15, ),
                    (5, 32, 100, 1000, ),):
        get_random_heap(d, n)

