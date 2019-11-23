from balanced_bst_18.balanced_bst import BSTNode, BalancedBST


BSTNode.__repr__ = lambda x: 'Node %s L:%s R:%s' % (
    x.NodeKey, x.LeftChild.NodeKey if x.LeftChild else '-',
    x.RightChild.NodeKey if x.RightChild else '-')
BalancedBST.__repr__ = lambda x: x.Root.__repr__() if x.Root else '-'


# --------------------------- TESTS ---------------------------------

t = BalancedBST()
assert t.Count() == 0

