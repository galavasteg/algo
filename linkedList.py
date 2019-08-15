# TODO 1.7: Напишите проверочные тесты для каждого из
#  предыдущих заданий.
# TODO 1.8: Напишите функцию, которая получает на вход
#  два связанных списка, состоящие из целых значений,
#  и если их длины равны, возвращает список, каждый
#  элемент которого равен сумме соответствующих элементов
#  входных списков.

# TODO Рекомендации по тестированию:
#  Проверяйте случаи, когда
#  - список пустой,
#  - содержит много элементов
#  - содержит один элемент
#  как в таких ситуациях будет работать
#  - удаление одного
#  - нескольких элементов,
#  - вставка,
#  - поиск.
#  Особое внимание уделите корректности полей
#  head и tail после ВСЕХ этих операций.


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list:
        # TODO 1.4.: найти узлы по конкретному значению
        #  На выход - список найденных узлов
        return []  # здесь будет ваш код

    def delete(self, val, all=False):
        # TODO 1.1.: удалить только первый нашедшийся узел
        # TODO 1.2.: удалить все узлы по конкретному значению
        nodes = self.find_all(val) if all else [self.find(val)]
        for n in nodes:
            next_node = n.next
            n.value = next_node.value
            n.next = next_node.next

    def clean(self):
        # TODO 1.3.: очистить все содержимое
        #  (создание пустого LinkedList)
        pass  # здесь будет ваш код

    def len(self) -> int:
        # TODO 1.5.: текущая длина списка
        return 0  # здесь будет ваш код

    def insert(self, afterNode, newNode):
        # TODO 1.6.: Добавьте в класс LinkedList метод
        #  вставки узла newNode после заданного узла
        #  afterNode (из списка). Если afterNode = None
        #  и список пустой, добавьте новый элемент
        #  первым в списке.
        pass  # здесь будет ваш код