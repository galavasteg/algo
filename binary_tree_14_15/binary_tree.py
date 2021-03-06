"""
TODO: EN doc
"""


class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # node key
        self.NodeValue = val  # value stored in node
        self.Parent = parent  # parent of node or None
        self.LeftChild = None  # link on left child node
        self.RightChild = None  # link on right child node

    @property
    def Children(self):
        return tuple(child for child
                     in (self.LeftChild, self.RightChild)
                     if child)

    # TODO: non-recursive version
    # def in_order_nodes_iterator(self):
    #     """A non-recursive In-order nodes iterator:
    #     left child - parent - right child"""
    #     pass

    def in_order_nodes_iterator(self):
        """In-order nodes iterator:
        left child - parent - right child"""
        if self.LeftChild:
            for n in self.LeftChild.in_order_nodes_iterator():
                yield n
        yield self
        if self.RightChild:
            for n in self.RightChild.in_order_nodes_iterator():
                yield n

    def nodes_iterator(self):
        """A non-recursive Post-order nodes iterator:
        left child - right child - parent"""
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

    def post_order_nodes_iterator(self):
        """Post-order nodes iterator:
        left child - right child - parent"""
        if self.LeftChild:
            for n in self.LeftChild.post_order_nodes_iterator():
                yield n
        if self.RightChild:
            for n in self.RightChild.post_order_nodes_iterator():
                yield n
        yield self

    # TODO: non-recursion version
    # def pre_order_nodes_iterator(self):
    #     """A non-recursive Pre-order nodes iterator:
    #     parent - left child - right child"""
    #     pass

    def pre_order_nodes_iterator(self):
        """Pre-order nodes iterator:
        parent - left child - right child"""
        yield self
        if self.LeftChild:
            for n in self.LeftChild.pre_order_nodes_iterator():
                yield n
        if self.RightChild:
            for n in self.RightChild.pre_order_nodes_iterator():
                yield n


class BSTFind:
    """Partial result of searching"""
    def __init__(self):
        self.Node = None  # None if tree is empty
        self.NodeHasKey = False  # True if node found
        # True if new node with search key can be
        # added to **Node** as a LeftChild Node
        self.ToLeft = False

    def search_direction(self, key):
        n = self.Node
        self.NodeHasKey = n and n.NodeKey == key
        self.ToLeft = n and n.NodeKey > key
        return ('LeftChild' if self.ToLeft
                else 'RightChild')


class BST:
    def __init__(self, node):
        self.Root = node  # tree root node or None

    def FindNodeByKey(self, key) -> BSTFind:
        """Search for a tree node and related information
        by **key**. The result is a BSTFind with:
        a Node with the same key OR a Node which last
        **L/R** child is None"""
        found = BSTFind()
        # start from root
        n = found.Node = self.Root
        # TODO: If *key* < key or the current node go to the left
        #  (right otherwise) child
        LR = found.search_direction(key)  # NodeHasKey sets here
        while n and not found.NodeHasKey and getattr(n, LR):
            n = found.Node = getattr(n, LR)
            LR = found.search_direction(key)
        return found

    def AddKeyValue(self, key, val) -> bool:
        """Add new node if possible """
        found = self.FindNodeByKey(key)
        parent = found.Node
        added = (parent and not found.NodeHasKey
                 or not self.Root)
        # Add new node to the found leaf (or as root)
        # if the key does not exist in the tree then
        if added:
            newNode = BSTNode(key, val, parent)
            if not self.Root:
                self.Root = newNode
            else:
                LR = 'LeftChild' if found.ToLeft else 'RightChild'
                setattr(parent, LR, newNode)
        # False if the node with the *key* is already in the tree
        return added

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool):
        """Search for the node with min/max key"""
        LR = 'RightChild' if FindMax else 'LeftChild'
        node = FromNode
        while node and getattr(node, LR):
            node = getattr(node, LR)
        return node

    def DeleteNodeByKey(self, key):
        # TODO: EN doc
        found = self.FindNodeByKey(key)
        dN = found.Node
        deleted = dN and found.NodeHasKey  # если узел не найден
        if deleted:
            # successor node
            heir = self.FinMinMax(dN.RightChild or dN.LeftChild,
                                  FindMax=False)
            if heir:
                # pop heir from tree
                LR = ('LeftChild' if heir is heir.Parent.LeftChild
                      else 'RightChild')
                setattr(heir.Parent, LR, heir.RightChild)
                for child in (heir.RightChild, heir.LeftChild):
                    if child:
                        child.Parent = heir.Parent
                # link heir with parent of deleted node
                heir.Parent = dN.Parent
                # link parent with children of deleted node
                heir.LeftChild = (dN.LeftChild
                                  if heir.NodeKey > dN.NodeKey
                                  else dN.RightChild)
                heir.RightChild = (dN.LeftChild
                                   if heir.NodeKey < dN.NodeKey
                                   else dN.RightChild)

            # link parent of deleted node with heir
            if dN.Parent:
                LR = ('LeftChild' if dN is dN.Parent.LeftChild
                      else 'RightChild')
                setattr(dN.Parent, LR, heir)
            else:
                self.Root = heir

            # link children of deleted node with heir
            for child in (dN.LeftChild, dN.RightChild):
                if child:
                    child.Parent = heir

            dN.Parent = dN.LeftChild = dN.RightChild = None

        return deleted

    def _get_all_nodes(self, order=None) -> tuple:
        # call nodes_iterator or create empty tuple
        nodes_iterator_method = (
                'in_order_nodes_iterator' if order == 0
                else 'post_order_nodes_iterator' if order == 1
                else 'pre_order_nodes_iterator' if order == 2
                else 'nodes_iterator')
        return tuple(getattr(self.Root, nodes_iterator_method,
                             tuple)())

    def WideAllNodes(self) -> tuple:
        """TODO: EN doc"""
        nodes = levelNodes = (self.Root,) if self.Root else ()

        while levelNodes:
            # TODO: use reduce(
            #   lambda res, n: res + n.Children, levelNodes, ())
            nextLevelNodes = ()
            for n in levelNodes:
                nextLevelNodes += n.Children
            nodes += nextLevelNodes
            levelNodes = nextLevelNodes

        return nodes

    def DeepAllNodes(self, order: int) -> tuple:
        """TODO: EN doc"""
        return self._get_all_nodes(order)

    def Count(self):
        """Count of nodes in the tree"""
        return len(self._get_all_nodes())

