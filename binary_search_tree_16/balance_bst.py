"""
TODO: EN doc
"""


def GenerateBBSTArray(a: list) -> list:
    """TODO: EN doc
    """
    assert a
    sorted_a = tuple(sorted(a))
    res = [None] * len(sorted_a)

    def balance_tree_vals(tree_keys: tuple, root_i: int):
        if tree_keys:
            center_i = len(tree_keys) // 2
            res[root_i] = tree_keys[center_i]

            left_subtree = tree_keys[:center_i]
            right_subtree = tree_keys[center_i + 1:]
            left_i, right_i = 2 * root_i + 1, 2 * root_i + 2

            balance_tree_vals(left_subtree, left_i)
            balance_tree_vals(right_subtree, right_i)

    balance_tree_vals(sorted_a, 0)

    return res

