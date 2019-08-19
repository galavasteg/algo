# TODO 2.9.: Напишите проверочные тесты для каждого из
#  предыдущих заданий. Особое внимание уделите корректности полей
#  head, prev, next и tail после ВСЕХ операций.


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
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
        return []  # здесь будет ваш код

    def delete(self, val, all=False):
        # TODO 2.3.: удалить только первый нашедшийся узел.
        # TODO 2.4.: удалить все узлы по конкретному значению
        pass  # здесь будет ваш код

    def clean(self):
        # TODO 2.7.: очистить все содержимое
        #  (создание пустого списка)
        pass  # здесь будет ваш код

    def len(self) -> int:
        # TODO 2.8.: вычислить текущую длину списка
        return 0  # здесь будет ваш код

    def insert(self, afterNode, newNode: Node):
        # TODO 2.5.: вставить узел newNode после заданного узла
        #  afterNode. Если afterNode = None и список пустой,
        #  добавить newNode первым в списке.
        #  Если afterNode = None и список непустой, добавить
        #  newNode последним в списке.
        pass  # здесь будет ваш код

    def add_in_head(self, newNode: Node):
        # TODO 2.6.: вставить узел первым элементом.
        pass  # здесь будет ваш код