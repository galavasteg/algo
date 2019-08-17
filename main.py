from linkedList import Node, LinkedList


def create_list(vals: list) -> LinkedList:
    list_ = LinkedList()
    [list_.add_in_tail(Node(x)) for x in vals]
    return list_


def get_list_vals(list_: LinkedList) -> list:
    values = []
    node = list_.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


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

