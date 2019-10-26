"""
TODO:
"""


class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # node key
        self.NodeValue = val  # value stored in node
        self.Parent = parent  # parent of node or None
        self.LeftChild = None  # link on left child node
        self.RightChild = None  # link on right child node


class BSTFind:
    """Partial result of searching"""
    def __init__(self):
        self.Node = None  # None if tree is empty
        self.NodeHasKey = False  # True if node found
        # True if new node with search key can be
        # added to **Node** as a LeftChild Node
        self.ToLeft = False


class BST:
    def __init__(self, node):
        self.Root = node  # tree root node or None

    def FindNodeByKey(self, key) -> BSTFind:
        """Search for a tree node and related information
        by **key**. The result is a BSTFind with:
        a Node with the same key OR a Node which last
        **L/R** child is None"""
        found = BSTFind()
        return found

    def AddKeyValue(self, key, val) -> bool:
        """Add new node if possible """
        # False if the node with the *key* is already in the tree
        return added

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool):
        """Search for the node with min/max key"""
        return node

    def DeleteNodeByKey(self, key):
        # TODO: EN doc
        return deleted

    def Count(self):
        """Count of nodes in the tree"""
        return 0

