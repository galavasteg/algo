"""
TODO: EN doc
Реализуйте двоичное дерево поиска в виде массива, и
сделайте функцию добавления нового узла (фактически,
целого ключа) и функцию поиска -- не линейно по
массиву, а на основе алгоритма из прошлых занятий,
через условные "узлы" дерева, только ограничьтесь
фиксированным размером массива.

Заполните полностью дерево глубины N значениями и
проверьте тестами работу функций добавления и поиска,
а также корректность значений в массиве, реализующем
дерево.
"""


class aBST:
    def __init__(self, depth: int):
        assert depth >= 0
        tree_size = 2 ** (depth + 1) - 1  # slots count
        self.Tree = [None] * tree_size  # keys array

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

