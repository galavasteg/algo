# + TODO 1.7: Напишите проверочные тесты для каждого из
#    предыдущих заданий.
# + TODO 1.8: Напишите функцию, которая получает на вход
#    два связанных списка, состоящие из целых значений,
#    и если их длины равны, возвращает список, каждый
#    элемент которого равен сумме соответствующих элементов
#    входных списков.

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

# TODO: translate doc in EN


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
        # + TODO 1.4.: найти узлы по конкретному значению
        #    На выход - список найденных узлов
        nodes = []
        node = self.find(val)
        while node:
            nodes.append(node)
            temp_list = LinkedList()
            temp_list.add_in_tail(node.next)
            temp_list.tail = self.tail
            node = temp_list.find(val)
        return nodes

    def delete(self, val, all=False):
        # + TODO 1.1.: удалить только первый нашедшийся узел
        # + TODO 1.2.: удалить все узлы по конкретному значению
        nodes = self.find_all(val)
        for del_n in (nodes[::-1] if all else nodes[:1]):
            if del_n is self.head and del_n.next is None:
                self.clean()
            elif del_n is self.head:
                self.head = del_n.next
            else:
                prev_node = self.head
                while prev_node.next is not del_n:
                    prev_node = prev_node.next
                prev_node.next = del_n.next
                if prev_node.next is None:
                    self.tail = prev_node
            # TODO: delete link or not delete?
            # del_n.next = None

    def clean(self):
        # + TODO 1.3.: очистить все содержимое
        #    (создание пустого LinkedList)
        self.__init__()

    def len(self) -> int:
        # + TODO 1.5.: вычислить текущую длину списка
        _len = 0
        node = self.head
        while node:
            node = node.next
            _len += 1
        return _len

    def insert(self, afterNode, newNode: Node):
        # + TODO 1.6.: вставить узел newNode после заданного узла
        #    afterNode (из списка). Если afterNode = None
        #    и список пустой, добавить newNode первым в списке.
        if afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

