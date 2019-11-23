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

