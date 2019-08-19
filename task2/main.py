from task2.linkedList2 import Node, LinkedList2


def get_nodes_vals(nodes: list) -> list:
    nodes_vals = []
    for n in nodes:
        n_vals = []
        node_ = n
        while node_ is not None:
            n_vals.append(node_.value)
            node_ = node_.next
        nodes_vals.append(n_vals)
    return nodes_vals

