"""
TODO: EN doc
"""


class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = parent.Level + 1 if parent else 1

    def in_order_nodes_iterator(self):
        """
        In-order nodes iterator:
        left child - parent - right child
        """
        if self.LeftChild:
            for n in self.LeftChild.in_order_nodes_iterator():
                yield n
        yield self
        if self.RightChild:
            for n in self.RightChild.in_order_nodes_iterator():
                yield n

    @property
    def children(self):
        return self.LeftChild, self.RightChild

    @property
    def max_depth(self):
        return max(n.Level for n in self.in_order_nodes_iterator())


class BalancedBST:

    def __init__(self):
        self.Root = None

    def _get_all_nodes(self) -> tuple:
        nodes = ()
        if self.Root:
            nodes = tuple(self.Root.in_order_nodes_iterator())
        return nodes

    def Count(self) -> int:
        return len(self._get_all_nodes())

    @classmethod
    def _get_root_index(cls, tree_keys: tuple) -> int:
        root_i = len(tree_keys) // 2
        left_i = root_i - 1
        while (0 <= left_i
               and tree_keys[left_i] == tree_keys[root_i]):
            root_i = left_i
            left_i -= 1

        return root_i

    @classmethod
    def _keys2tree(cls, tree_keys: tuple,
                  parent: (BSTNode, None)) -> (BSTNode, None):
        if tree_keys:
            root_i = cls._get_root_index(tree_keys)

            child = BSTNode(tree_keys[root_i], parent)

            child.LeftChild = cls._keys2tree(
                    tree_keys[:root_i], child)
            child.RightChild = cls._keys2tree(
                    tree_keys[root_i + 1:], child)

            return child

    def GenerateTree(self, a: list):
        """TODO: EN doc
        """
        sorted_keys = tuple(sorted(a))
        self.Root = self._keys2tree(sorted_keys, parent=None)

    @staticmethod
    def _children_depths_diff(node: BSTNode) -> int:
        left_depth, right_depth = tuple(
            (c.max_depth if c else node.Level)
            for c in node.children)
        # TODO: diff with each other for non-binary tree too
        # t = left_depth, right_depth
        # depth_diffs = [abs(j - i) for i, j in zip(t, t[1:])]
        depths_diff = abs(left_depth - right_depth)
        return depths_diff

    def IsBalanced(self, root_node: BSTNode):
        """TODO: EN doc
        """
        balanced = True

        if root_node:
            left_balanced = self.IsBalanced(root_node.LeftChild)
            right_balanced = self.IsBalanced(root_node.RightChild)
            depths_diff = self._children_depths_diff(root_node)

            balanced = (left_balanced and right_balanced
                        and depths_diff <= 1)

        return balanced

