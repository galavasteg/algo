# -*- coding: utf-8 -*-

# + TODO 2.9.: Напишите проверочные тесты для каждого из
#    предыдущих заданий. Особое внимание уделите корректности полей
#    head, prev, next и tail после ВСЕХ операций.


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def next_vals(self):
        values = []
        node = self.next
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    def prev_vals(self):
        values = []
        node = self.prev
        while node is not None:
            values.append(node.value)
            node = node.prev
        values.reverse()
        return values


class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    @classmethod
    def create(cls, values):
        list_ = cls()
        [list_.add_in_tail(Node(v)) for v in values]
        return list_

    @property
    def vals(self) -> list:
        return ([self.head.value, *self.head.next_vals()]
                if self.head is not None else [])

    @property
    def nodes(self) -> list:
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node)
            node = node.next
        return nodes

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        # + TODO 2.1.: поиск первого узла по его значению.
        node = self.head
        while node is not None:
            if node.value == val:
                break
            node = node.next
        return node

    def find_all(self, val) -> list:
        # + TODO 2.2.: найти узлы по конкретному значению
        #    (вернуть список найденных узлов).
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        # + TODO 2.3.: удалить только первый нашедшийся узел.
        # + TODO 2.4.: удалить все узлы по конкретному значению
        nodes = self.find_all(val)
        for del_n in (nodes[::-1] if all else nodes[:1]):
            if del_n is self.head and del_n.next is None:
                self.clean()
            elif del_n is self.tail:
                self.tail = del_n.prev
                del_n.prev.next = None
            elif del_n is self.head:
                self.head = del_n.next
                del_n.next.prev = None
            else:
                del_n.prev.next = del_n.next
                del_n.next.prev = del_n.prev
            del_n.prev = None
            del_n.next = None

    def clean(self):
        # + TODO 2.7.: очистить все содержимое
        #    (создание пустого списка)
        self.__init__()

    def len(self) -> int:
        # + TODO 2.8.: вычислить текущую длину списка
        values = ([self.head.value, *self.head.next_vals()]
                  if self.head is not None else [])
        return len(values)

    def insert(self, afterNode, newNode: Node):
        # + TODO 2.5.: вставить узел newNode после заданного узла
        #    afterNode. Если afterNode = None и список пустой,
        #    добавить newNode первым в списке.
        #    Если afterNode = None и список непустой, добавить
        #    newNode последним в списке.
        if afterNode is self.tail or afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            afterNode.next.prev = newNode
            newNode.next = afterNode.next
            afterNode.next = newNode

    def add_in_head(self, newNode: Node):
        # + TODO 2.6.: вставить узел первым элементом.
        if self.head is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode