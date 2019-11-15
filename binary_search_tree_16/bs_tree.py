"""
TODO: EN doc
"""


class aBST:
    @staticmethod
    def _get_tree_size(depth):
        return 2 ** (depth + 1) - 1

    @staticmethod
    def _get_depth(tree_size):
        def log2(x: int, base=2):
            count = -1
            while x != 0:
                x = x // base
                count = count + 1
            return count

        to_logarithm = tree_size + 1
        log = log2(to_logarithm)
        depth = int(log) - 1
        return depth

    def __init__(self, depth: int):
        assert depth >= 0
        tree_size = self._get_tree_size(depth)  # slots count
        self.Tree = [None] * tree_size  # keys array

    @classmethod
    def create(cls, keys: list):
        t = cls(0)
        t.Tree = keys
        return t

    @staticmethod
    def _get_parent_i(node_i: int) -> int:
        return (node_i - 1) // 2

    @staticmethod
    def _get_left_child_i(parent_i: int) -> int:
        return 2 * parent_i + 1

    @staticmethod
    def _get_right_child_i(parent_i: int) -> int:
        return 2 * parent_i + 2

    def _get_next_search_i(self, i: int, key) -> (int, bool):
        """Returns index of child of i-th element and
        the key equality flag.
        NOTE: **i**-th tree element key != **key** """
        assert self.Tree[i] != key
        next_i = (self._get_left_child_i
                  if self.Tree[i] > key
                  else self._get_right_child_i
                  )(i)
        IndAndFoundFlag = (
            (next_i, self.Tree[next_i] == key)
            if next_i < len(self.Tree)
            else (None, False))
        return IndAndFoundFlag

    def FindKeyIndex(self, key) -> int:
        """Search for index with **key**.

        :return **a positive int** if the **key** is found OR
                **a negative int** if the **key** can be added
                to the tree in **-(returned index)** OR
                **None**, if **key** cannot be added"""
        child_ind = 0
        existing_key = self.Tree[child_ind]
        key_found = existing_key == key
        while (child_ind is not None
               and not key_found
               and existing_key is not None):
            child_ind, key_found = self._get_next_search_i(
                    child_ind, key)
            if child_ind is not None:
                existing_key = self.Tree[child_ind]

        return (child_ind
                if key_found or child_ind is None
                else -child_ind)

    def AddKey(self, key) -> int:
        """Returns the index of an existing **key** OR
        the index of the added **key** OR
        **-1** (the **key** cannot be added)"""
        i = -1
        found_i = self.FindKeyIndex(key)
        if found_i is not None:
            i = abs(found_i)
            if self.Tree[i] is None:
                self.Tree[i] = key
        return i

