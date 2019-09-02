"""
TODO: 7.6. Добавьте тесты для добавления, удаления и поиска элемента
 по его значению -- каждый случай с учётом признака упорядоченности.
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def _next_vals(self):
        values = []
        node = self.next
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    def _prev_vals(self):
        values = []
        node = self.prev
        while node is not None:
            values.append(node.value)
            node = node.prev
        values.reverse()
        return values


class OrderedList:
    def __init__(self, asc):
        """7.1. Реализуйте дополнительную опцию asc в конструкторе
 OrderedList, которая указывает, по возрастанию (True) или по
 убыванию (False) должны храниться элементы в массиве. Эту
 опцию сделайте приватной -- изменять её можно только в конструкторе
 и методе очистки clean()."""
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        """7.2. Метод сравнения двух значений compare(). В общем случае,
 мы можем хранить в нашем списке произвольные объекты (например,
 экземпляры класса Cat), и способ, которым мы желаем их сравнивать,
 потенциально может быть самым произвольным. Пока сделайте базовый
 вариант этого метода, который сравнивает числовые значения."""
        return (-1 if v1 < v2 else
                0 if v1 == v2 else 1)

    def add(self, value):
        """TODO: 7.3. doc"""
        # TODO: one cycle
        newNode = Node(value)
        nodes = self.get_all()
        if not nodes:
            self.head = newNode
            self.tail = newNode
        else:
            stop_search = 1 if self.__ascending else -1
            for next_n in nodes:
                comp_res = self.compare(next_n.value, value)
                if comp_res == stop_search:
                    afterNode = next_n.prev
                    break
                else:
                    afterNode = next_n
            if afterNode is None:  # prev of head
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif afterNode is self.tail:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                newNode.prev = afterNode
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
                afterNode.next = newNode
                newNode.prev = afterNode

    def find(self, val):
        """TODO: 7.5. doc"""
        node = self.head
        while node != None:
            if self.compare(node.value, val) == 0:
                return node
            node = node.next

    def delete(self, val):
        """Delete 1-st node with **val**"""
        del_n = self.find(val)
        if del_n is not None and del_n.value == val:
            if del_n is self.head and del_n.next is None:
                self.clean(self.__ascending)
            elif del_n is self.tail:
                self.tail = del_n.prev
                del_n.prev.next = None
            elif del_n is self.head:
                self.head = del_n.next
                del_n.next.prev = None
            else:
                del_n.prev.next = del_n.next
                del_n.next.prev = del_n.prev
            # TODO: delete links or not delete?
            del_n.prev = None
            del_n.next = None

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        return len(self.get_all())

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    @classmethod
    def create(cls, vals: list, asc: bool):
        list_ = cls(asc)
        for v in vals:
            list_.add(v)
        return list_


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        """TODO: 7.4. doc"""
        return super(OrderedStringList, self).compare(
            v1.strip(), v2.strip())

