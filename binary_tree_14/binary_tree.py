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

    def nodes_iterator(self):
        # 1) Create an empty stack S.
        stack = []
        # 2) Initialize currentNode as root
        currentNode = self
        # 5) If currentNode is NULL and stack is empty then we are done.
        while currentNode or stack:
            # 3) Push the currentNode to S and set currentNode
            # to his left or right (if left foes not exist)
            # childNode until currentNode is None.
            # Another words: find the deepest leaf of a subtree.
            while currentNode:
                stack.append(currentNode)
                currentNode = (currentNode.LeftChild
                               or currentNode.RightChild)
            # 4) If currentNode is NULL and stack is not empty then
            currentNode = stack.pop()  # a) Pop the top item from stack
            yield currentNode          # b) yield it
            # set currentNode to popped item's "right" brother
            # if it is possible
            p = currentNode.Parent
            currentNode = (p.RightChild
                           if p and currentNode is not p.RightChild else
                           None)
            # c) Go to step 3.


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

    def _get_all_nodes(self) -> tuple:
        # call nodes_iterator or create empty tuple
        return tuple(getattr(self.Root, 'nodes_iterator',
                             tuple)())

    def Count(self):
        """Count of nodes in the tree"""
        return len(self._get_all_nodes())

