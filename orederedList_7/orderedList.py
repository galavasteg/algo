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

    def __get_half_node(self, direction: str, num: int):
        n = None
        for _ in range(num):
            n = self.__getattribute__(direction)
        return n


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
        """7.3. Добавление нового элемента по значению add() с единственным
 параметром -- новым добавляемым значением (новый узел для него
 создавайте внутри метода add). Элемент должен вставиться автоматически
 между элементами с двумя подходящими значениями (либо в начало или
 конец списка) с учётом его значения и признака упорядоченности.
 Используйте для этого метод сравнения значений из предыдущего пункта."""
        pass
        # автоматическая вставка value
        # в нужную позицию

    def find(self, val):
        """7.5. Переделайте функцию поиска элемента по значению с учётом
 признака упорядоченности и возможности раннего прерывания поиска,
 если найден заведомо больший или меньший элемент, нежели искомый.
 Оцените сложность операции поиска, изменилась ли она?"""
        return None  # здесь будет ваш код

    def delete(self, val):
        """Delete 1-st node with **val**"""
        pass  # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        pass  # здесь будет ваш код

    def len(self):
        return 0  # здесь будет ваш код

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

    @property
    def vals(self) -> list:
        values = []
        if self.head is not None:
            values = [self.head.value]
            for v in self.head._next_vals():
                values.append(v)
        return values


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        """7.4. Создайте OrderedStringList -- наследник текущего класса,
 который будет упорядоченно хранить строки. Для этого переопределите
 в нём метод сравнения значений -- он должен сравнивать строки,
 очищенные от начальных и конечных пробелов."""
        # переопределённая версия для строк
        return 0

