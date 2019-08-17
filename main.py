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


def merge_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    # + TODO 1.8: Напишите функцию, которая получает на вход
    #    два связанных списка, состоящие из целых значений,
    #    и если их длины равны, возвращает список, каждый
    #    элемент которого равен сумме соответствующих элементов
    #    входных списков.
    if list1.len() == list2.len():
        new_list = LinkedList()
        n1, n2 = list1.head, list2.head
        while all((n1, n2)):
            new_list.add_in_tail(Node(n1.value + n2.value))
            n1, n2 = n1.next, n2.next
        return new_list

