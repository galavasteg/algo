"""
In general, a simple tree is the root node (one field in the class),
for which the node or None is specified as a value. The SimpleTree
has next methods:
- AddChild - add child Node to existing parent Node
- DeleteNode - Delete not root Node
- GetAllNodes - sequentially go around the whole tree and get a list
                of all nodes in random order;
- FindNodesByValue - find all nodes with a specific value
- MoveNode - move a non-root Node with its subtree as a child node
             to the new parent Node, use existing methods
- Count and LeafCount - number of Nodes/Leafs(nodes without children)
                        in the tree

Another method might be:
- ResetSubTreeLevels - go around the whole sub tree and set the level
                       (the shortest path to the Root) for each Node
NOTE: levels can be set in the AddChild method with incrementing the
      parent level by 1
"""


class SimpleTreeNode:
    def __init__(self, val, parent):
        """
        :param val: Node value
        :param parent: parent Node or None
        """
        self.NodeValue = val
        self.Parent = parent
        self.Children = []  # child Nodes
        self.level = 0  # the shortest path to the Root
        # next Node on the same level (for nodes iteration)
        self._next_brother = None

    def nodes_iterator(self):
        # 1) Create an empty stack S.
        stack = []
        # 2) Initialize currentNode as root
        currentNode = self
        # 5) If currentNode is NULL and stack is empty then we are done.
        while currentNode or stack:
            # 3) Push the currentNode node to S and set currentNode
            # to his 1-st childNode until currentNode is NULL.
            # Another words: find the leftmost leaf.
            while currentNode:
                stack.append(currentNode)
                currentNode = (currentNode.Children[0]
                               if currentNode.Children
                               else None)
            # 4) If currentNode is NULL and stack is not empty then
            currentNode = stack.pop()  # a) Pop the top item from stack
            yield currentNode          # b) yield it
            # set currentNode to popped item next "bro" (Node on the same lvl)
            currentNode = currentNode._next_brother
            # currentNode = getattr(currentNode, '_next_brother', None)
            # c) Go to step 3.


class SimpleTree:
    def __init__(self, root):
        """:param root: tree root or None"""
        self.Root = root

    @classmethod
    def __get_nodes_recursive(cls, start_node: SimpleTreeNode):
        """NOTE: Remember about maximum recursion depth: 987"""
        nodes = []
        if start_node:
            nodes += start_node.Children
            for childNode in start_node.Children:
                nodes += cls.__get_nodes_recursive(childNode)
        return nodes

    def AddChild(self, ParentNode, NewChild: SimpleTreeNode):
        """Add child Node to existing parent Node"""
        __before_nodes = tuple(NewChild.nodes_iterator())
        if ParentNode:
            if ParentNode.Children:
                ParentNode.Children[-1]._next_brother = NewChild
            ParentNode.Children.append(NewChild)
            NewChild.level = ParentNode.level + 1
            NewChild.Parent = ParentNode
            assert NewChild in ParentNode.Children
            assert NewChild.level == ParentNode.level + 1
        else:
            self.Root = NewChild
        assert tuple(NewChild.nodes_iterator()) == __before_nodes

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        """Delete not root Node"""
        delN = NodeToDelete
        assert delN is not self.Root
        parent = delN.Parent
        ind = parent.Children.index(delN)
        if ind:
            prevBro = parent.Children[ind-1]
            prevBro._next_brother = delN._next_brother
        delN._next_brother = None
        parent.Children.pop(ind)
        delN.Parent = None
        assert not any((
            delN._next_brother, delN.Parent, delN in parent.Children))

    def GetAllNodes(self) -> list:
        nodes = []
        if self.Root:
            nodes = list(self.Root.nodes_iterator())
        return nodes

    def FindNodesByValue(self, val) -> list:
        """Find all nodes with a specific value"""
        foundNodes = []
        if self.Root:
            foundNodes = [node for node in self.Root.nodes_iterator()
                          if node.NodeValue == val]
        return foundNodes

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        """Move not root **OriginalNode** with his subtree as
        a child to **NewParent**"""
        assert OriginalNode is not self.Root
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
        self.ResetSubTreeLevels(OriginalNode)

    def Count(self) -> int:
        """Number of Nodes in the tree"""
        return len(self.GetAllNodes())

    def LeafCount(self) -> int:
        """Number of Nodes without children"""
        leafsCount = 0
        if self.Root:
            for node in self.Root.nodes_iterator():
                if not node.Children:
                    leafsCount += 1
        return leafsCount

    def _reset_node_lvl(self, Node: SimpleTreeNode):
        Node.level = 0
        node = Node
        while node.Parent:
            Node.level += 1
            node = node.Parent

    def ResetSubTreeLevels(self, start_node):
        """TODO: Go around the whole sub tree and
        set the level for each Node"""
        if start_node:
            for node in start_node.nodes_iterator():
                self._reset_node_lvl(node)

