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


class SimpleTree:
    def __init__(self, root):
        """:param root: tree root or None"""
        self.Root = root


