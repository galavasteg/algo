from random import shuffle

from binary_tree_14.binary_tree import BST, BSTNode, BSTFind


BSTNode.__repr__ = lambda x: 'Node %s %s' % (x.NodeKey, x.NodeValue)
BSTFind.__repr__ = lambda x: 'Find %s %s %s' % (
    x.Node.NodeKey if x.Node else None,
    int(x.NodeHasKey), int(x.ToLeft))
BST.__repr__ = lambda x: 'BST r:%s mn:%s mx:%s' % (
    x.Root, x.FinMinMax(x.Root, False), x.FinMinMax(x.Root, True))


def get_random_tree(nodes_count: int):
    t = BST(None)
    keys = list(range(nodes_count))
    shuffle(keys)
    keys = tuple(keys)
    for k in keys:
        t.AddKeyValue(k, str(k))
    assert t.Count() == nodes_count
    assert t.FinMinMax(t.Root, False).NodeKey == 0
    assert t.FinMinMax(t.Root, True).NodeKey == nodes_count-1
    return t


# --------------------------- TESTS ---------------------------------

t = BST(None)
assert t.Count() == 0

t = BST(BSTNode(4, '4', None))
assert t.Count() == 1

n2 = t.Root.LeftChild = BSTNode(2, '2', t.Root)
n3 = n2.RightChild = BSTNode(3, '3', n2)
n1 = n2.LeftChild = BSTNode(1, '1', n2)

n6 = t.Root.RightChild = BSTNode(6, '6', t.Root)
n7 = n6.RightChild = BSTNode(7, '7', n6)
n5 = n6.LeftChild = BSTNode(5, '5', n6)

# print(t._get_all_nodes())
assert t.Count() == 7
t.AddKeyValue(3, 'exist')
t.AddKeyValue(1, 'exist')
t.AddKeyValue(4, 'exist')
# print(t._get_all_nodes())

# find min/max
assert t.FinMinMax(t.Root, True) is n7
assert t.FinMinMax(t.Root, False) is n1

assert t.FinMinMax(n3, True) is n3
assert t.FinMinMax(n3, False) is n3

assert t.FinMinMax(n2, True) is n3
assert t.FinMinMax(n2, False) is n1


def test_delete_root():
    # delete
    t.DeleteNodeByKey(4)
    print(t._get_all_nodes())
    assert t.Count() == 6
    assert t.Root is n5
    assert t.FinMinMax(n5, True) is n7
    assert t.FinMinMax(n5, False) is n1
    assert t.FinMinMax(n6, False) is n6
    assert t.FinMinMax(n6, True) is n7


def test_fill_empty_tree_and_clear():
    t_ = BST(BSTNode(0, '0', None))
    assert t_.Count() == 1
    t_.DeleteNodeByKey(0)
    assert t_.Count() == 0
    t_.AddKeyValue(0, '0')
    t_.AddKeyValue(-1, '-1')
    t_.AddKeyValue(1, '1')
    print(t_._get_all_nodes())
    assert t_.Count() == 3
    t_.DeleteNodeByKey(0)
    t_.DeleteNodeByKey(1)
    t_.DeleteNodeByKey(-1)
    assert t_.Count() == 0


def test_find_add():
    # add
    t.AddKeyValue(4, '4')  # add 4
    print(t._get_all_nodes())
    assert t.Count() == 7
    f = t.FindNodeByKey(4)
    assert not f.ToLeft and f.NodeHasKey
    n4 = f.Node
    assert n4
    assert n4 is t.FinMinMax(n3, True) is t.FinMinMax(n2, True)

    f = t.FindNodeByKey(1)
    assert not f.ToLeft and f.NodeHasKey
    n1 = f.Node
    assert n1
    assert n1 is t.FinMinMax(n2, False) is t.FinMinMax(t.Root, False)

    f = t.FindNodeByKey(5.5)
    assert f.ToLeft and not f.NodeHasKey and f.Node is n6
    f = t.FindNodeByKey(1.5)
    assert not f.ToLeft and not f.NodeHasKey and f.Node is n1

    f = t.FindNodeByKey(8)
    assert not f.ToLeft and not f.NodeHasKey and f.Node is n7
    t.AddKeyValue(8, '8')
    f = t.FindNodeByKey(8)
    assert not f.ToLeft and f.NodeHasKey
    assert t.Count() == 8
    n8 = f.Node

    f = t.FindNodeByKey(9)
    assert not f.ToLeft and not f.NodeHasKey and f.Node is n8
    t.AddKeyValue(9, '9')
    f = t.FindNodeByKey(9)
    assert not f.ToLeft and f.NodeHasKey
    assert t.Count() == 9
    n9 = f.Node

    print(t._get_all_nodes())
    assert n8, n9
    assert t.FinMinMax(t.Root, True) is t.FinMinMax(n6, True) is t.FinMinMax(n7, True) is n9
    assert n7.RightChild is n8 and n8.RightChild is n9

    f = t.FindNodeByKey(7.5)
    assert f.ToLeft and not f.NodeHasKey and f.Node is n8
    t.AddKeyValue(7.5, 'del after')
    f = t.FindNodeByKey(7.5)
    assert not f.ToLeft and f.NodeHasKey
    assert t.Count() == 10

    t.DeleteNodeByKey(7.5)
    assert t.Count() == 9 and n8.LeftChild is None
    assert t.FinMinMax(n8, False) is n8

    return n8, n9


def test_delete_and_add():
    assert t.Count() == 9
    t.DeleteNodeByKey(8)
    print(t._get_all_nodes())
    assert t.Count() == 8
    t.AddKeyValue(8, '8')
    print(t._get_all_nodes())
    assert t.Count() == 9
    n8 = t.FindNodeByKey(8).Node
    assert n8
    assert t.FinMinMax(t.Root, True) is t.FinMinMax(n6, True) is t.FinMinMax(n7, True) is n9
    assert t.FinMinMax(n9, False) is n8
    assert n7.RightChild is n9 and n9.LeftChild is n8
    return n8


def test_left_branch_only():
    t_ = BST(None)
    for k in range(5, 0, -1):
        t_.AddKeyValue(k, str(k))

    print(t_._get_all_nodes())
    assert t_.Count() == 5
    assert not any(n.RightChild for n in t_._get_all_nodes())

    for k in range(5, 0, -1):
        d = t_.DeleteNodeByKey(k)
        print(t_._get_all_nodes())
        assert d
        assert t_.Count() == k-1

    assert t_.Count() == 0


def test_create_and_cleare_random_tree(n: int, verbose=True):
    tree = get_random_tree(n)
    print(tree._get_all_nodes()[: n if verbose else 10])

    for k in range(n):
        tree.DeleteNodeByKey(k)

    assert tree.Count() == 0


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_delete_root()
    n8, n9 = test_find_add()
    n8 = test_delete_and_add()
    test_fill_empty_tree_and_clear()
    test_left_branch_only()
    for n in (5, 32, 100):
        test_create_and_cleare_random_tree(n, False)
    test_create_and_cleare_random_tree(10000, False)

