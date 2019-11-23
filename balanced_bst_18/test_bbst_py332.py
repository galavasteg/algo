from balanced_bst_18.balanced_bst import BSTNode, BalancedBST


BSTNode.__repr__ = lambda x: 'Node %s L:%s R:%s' % (
    x.NodeKey, x.LeftChild.NodeKey if x.LeftChild else '-',
    x.RightChild.NodeKey if x.RightChild else '-')
BalancedBST.__repr__ = lambda x: x.Root.__repr__() if x.Root else '-'


def count_and_order_checks(t: BalancedBST, a: list):
    assert t.Count() == len(a)
    assert [n.NodeKey for n in t._get_all_nodes()
            ] == sorted(a)


# --------------------------- TESTS ---------------------------------

t = BalancedBST()
count_and_order_checks(t, a)

a = []
t.GenerateTree(a)
count_and_order_checks(t, a)
assert t.IsBalanced(t.Root)

a = [3, 2, 3, ]
t.GenerateTree(a)
count_and_order_checks(t, a)
assert t.IsBalanced(t.Root)

a = [1, 3, 2, 2, 1, ]
t.GenerateTree(a)
count_and_order_checks(t, a)
assert t.IsBalanced(t.Root)

a = [1, 3, 2, 2, 1, 3, 4, 4, ]
t.GenerateTree(a)
assert t.IsBalanced(t.Root)
assert t.Count() == len(a)
in_order_nodes = [n for n in t._get_all_nodes()]
assert list(n.NodeKey for n in in_order_nodes) == sorted(a)
assert t.Root.Level == 1
assert in_order_nodes[1].Level == 4  # 2-nd "1"
assert in_order_nodes[-1].Level == 3

a = [2, 2, 2, ]
t.GenerateTree(a)
assert not t.IsBalanced(t.Root)
assert t.Count() == len(a)
in_order_nodes = [n for n in t._get_all_nodes()]
assert list(n.NodeKey for n in in_order_nodes) == sorted(a)
assert in_order_nodes[0] == t.Root
assert t.Root.Level == 1
assert in_order_nodes[-1].Level == 3

a = [1, 3, 0, 2, 5, 3, 4, ]
t.GenerateTree(a)
count_and_order_checks(t, a)
assert t.IsBalanced(t.Root)

a = [1, 3, 0, 2, 5, 3, 4, -1, -2, -3, ]
t.GenerateTree(a)
count_and_order_checks(t, a)
assert t.IsBalanced(t.Root)

a = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, ]
t.GenerateTree(a)
count_and_order_checks(t, a)
assert not t.IsBalanced(t.Root)
assert t.IsBalanced(t.Root.LeftChild)
assert not t.IsBalanced(t.Root.RightChild)
assert not t.IsBalanced(t.Root.RightChild.LeftChild)
assert t.IsBalanced(t.Root.RightChild.RightChild)

