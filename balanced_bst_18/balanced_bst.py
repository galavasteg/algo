"""
TODO: EN doc
"""


class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0

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

    def GenerateTree(self, a: list):
        """TODO: EN doc
        """
        sorted_keys = tuple(sorted(a))
        
    def IsBalanced(self, root_node: BSTNode):
        """
        - правое поддерево каждого узла сбалансировано;
        - левое поддерево каждого узла сбалансировано;
        - разница между глубинами левого и правого поддеревьев не
          превышает единицы (или, проще говоря, левое и правое
          поддеревья равны по длинами или отличаются не более чем
          на одну ветку).
        """
        balanced = True

        return balanced  # сбалансировано ли дерево с корнем root_node

