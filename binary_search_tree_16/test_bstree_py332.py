from random import shuffle

from binary_search_tree_16.bs_tree import aBST


aBST.__repr__ = lambda x: 'BST r:%s c:%s' % (
    x.Tree[0], len(x.Tree))


