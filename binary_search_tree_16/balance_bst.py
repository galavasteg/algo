"""
TODO: EN doc
"""


def GenerateBBSTArray(a: list) -> list:
    """TODO: EN doc
    2. Для левой части по отношению к выбранному элементу
       повторяем этот алгоритм -- индекс корневого элемента
       левой части будет равен индексу левого наследника
       корня из пункта 1.
    3. Для правой части по отношению к выбранному элементу
       повторяем этот алгоритм -- индекс корневого элемента
       правой части будет равен индексу правого наследника
       корня из пункта 1.
    """
    assert a
    sorted_a = tuple(sorted(a))
    res = [None] * len(sorted_a)

    def balance_tree_vals(tree_keys: tuple, root_i: int):
        if tree_keys:
            center_i = len(tree_keys) // 2
            res[root_i] = tree_keys[center_i]

    balance_tree_vals(sorted_a, 0)

    return res

