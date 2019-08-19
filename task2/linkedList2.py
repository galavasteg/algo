# TODO 2.9.: Напишите проверочные тесты для каждого из
#  предыдущих заданий. Особое внимание уделите корректности полей
#  head, prev, next и tail после ВСЕХ операций.


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def iter_node_vals(self):
        node = self
        while node is not None:
            yield node.value
            node = node.next


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
    def vals(self):
        return (list(self.head.iter_node_vals())
                if self.head is not None else [])

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
        # TODO 2.1.: поиск первого узла по его значению.
        node = self.head
        while node is not None:
            if node.value == val:
                break
            node = node.next
        return node

    def find_all(self, val) -> list:
        # TODO 2.2.: поиск всех узлов по конкретному значению
        #  (вернуть список найденных узлов).
        nodes = []
        node = self.find(val)
        while node is not None:
            nodes.append(node)
            temp_list = LinkedList2()
            if node.next is not None:
                temp_list.head = node.next
                temp_list.tail = self.tail
            node = temp_list.find(val)
        return nodes

    def delete(self, val, all=False):
        # TODO 2.3.: удалить только первый нашедшийся узел.
        # TODO 2.4.: удалить все узлы по конкретному значению
        nodes = self.find_all(val)
        for del_n in (nodes[::-1] if all else nodes[:1]):
            if del_n is self.head and del_n.next is None:
                self.clean()
            elif del_n is self.head:
                self.head = del_n.next
            else:
                del_n.prev.next = del_n.next
                if del_n.prev.next is None:
                    self.tail = del_n.prev

    def clean(self):
        # TODO 2.7.: очистить все содержимое
        #  (создание пустого списка)
        self.__init__()

    def len(self) -> int:
        # TODO 2.8.: вычислить текущую длину списка
        _len = 0
        node = self.head
        while node:
            _len += 1
            node = node.next
        return _len

    def insert(self, afterNode, newNode: Node):
        # TODO 2.5.: вставить узел newNode после заданного узла
        #  afterNode. Если afterNode = None и список пустой,
        #  добавить newNode первым в списке.
        #  Если afterNode = None и список непустой, добавить
        #  newNode последним в списке.
        if afterNode is self.tail or afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            afterNode.next.prev = newNode
            newNode.next = afterNode.next
            afterNode.next = newNode

    def add_in_head(self, newNode: Node):
        # TODO 2.6.: вставить узел первым элементом.
        pass  # здесь будет ваш код