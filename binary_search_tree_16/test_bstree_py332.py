from random import shuffle

from binary_search_tree_16.bs_tree import aBST


aBST.__repr__ = lambda x: 'BST r:%s c:%s' % (
    x.Tree[0], len(x.Tree))


# --------------------------- TESTS ---------------------------------

assert len(aBST(0).Tree) == 1
assert len(aBST(3).Tree) == 15
assert len(aBST(5).Tree) == 63

t = aBST(3)

assert t.FindKeyIndex(5) is -0

t_arr = [50,
         25, 75,
         None, 37, 62, 84,
         None, None, 31, 43, 55, None, None, 92]
t.Tree = t_arr

assert t.FindKeyIndex(50) == 0
assert t.FindKeyIndex(84) == 6
assert t.FindKeyIndex(62) == 5
assert t.FindKeyIndex(64) == -12
assert t.FindKeyIndex(53) is None
assert t.FindKeyIndex(59) is None
assert t.FindKeyIndex(24) == -3
assert t.FindKeyIndex(1) == -3
assert t.FindKeyIndex(0) == -3

assert t.AddKey(24) == 3
assert t.AddKey(59) == -1
assert t.AddKey(53) == -1
assert t.AddKey(55) == 11


def test_fill_empty_tree():
    print()
    t = aBST(3)
    for elem in (8,4,12,2,6,10,14,1,3,5,7,9,11,13):
        t.AddKey(elem)

    assert t.FindKeyIndex(15) == -14
    t.AddKey(15)
    assert t.FindKeyIndex(15) == 14

    assert t.AddKey(100) == -1
    assert t.AddKey(10) == 5
    assert t.AddKey(15) == 14

    assert t.FindKeyIndex(100) is None
    assert t.FindKeyIndex(8) == 0
    assert t.FindKeyIndex(1) == 7

