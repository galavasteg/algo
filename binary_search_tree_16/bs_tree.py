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

    def FindKeyIndex(self, key) -> int:
        child_ind = 0
        return child_ind

    def AddKey(self, key) -> int:
        i = -1
        return i

