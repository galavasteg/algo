from binary_tree_14.binary_tree import BST, BSTNode, BSTFind


BSTNode.__repr__ = lambda x: 'Node %s %s' % (x.NodeKey, x.NodeValue)
BSTFind.__repr__ = lambda x: 'Find %s %s %s' % (
    x.Node.NodeKey if x.Node else None,
    int(x.NodeHasKey), int(x.ToLeft))
BST.__repr__ = lambda x: 'BST r:%s mn:%s mx:%s' % (
    x.Root, x.FinMinMax(x.Root, False), x.FinMinMax(x.Root, True))


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


def test_left_branch_only():
    t_ = BST(None)
    for k in range(5, 0, -1):
        t_.AddKeyValue(k, str(k))

    print(t_._get_all_nodes())
    assert t_.Count() == 5
    assert not any(n.RightChild for n in t_._get_all_nodes())


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_left_branch_only()

