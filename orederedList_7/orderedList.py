"""
TODO: 7.1. Дополнительную опцию asc в конструкторе OrderedList,
 которая указывает, по возрастанию (True) или по убыванию (False)
 должны храниться элементы в массиве. Эту опцию сделайте приватной
 -- изменять её можно только в конструкторе и методе очистки clean().

TODO: 7.2. Метод сравнения двух значений compare(). В общем случае,
 мы можем хранить в нашем списке произвольные объекты (например,
 экземпляры класса Cat), и способ, которым мы желаем их сравнивать,
 потенциально может быть самым произвольным. Пока сделайте базовый
 вариант этого метода, который сравнивает числовые значения.

TODO: 7.3. Добавление нового элемента по значению add() с единственным
 параметром -- новым добавляемым значением (новый узел для него
 создавайте внутри метода add). Элемент должен вставиться автоматически
 между элементами с двумя подходящими значениями (либо в начало или
 конец списка) с учётом его значения и признака упорядоченности.
 Используйте для этого метод сравнения значений из предыдущего пункта.

TODO: 7.4. Создайте OrderedStringList -- наследник текущего класса,
 который будет упорядоченно хранить строки. Для этого переопределите
 в нём метод сравнения значений -- он должен сравнивать строки,
 очищенные от начальных и конечных пробелов.

TODO: 7.5. Переделайте функцию поиска элемента по значению с учётом
 признака упорядоченности и возможности раннего прерывания поиска,
 если найден заведомо больший или меньший элемент, нежели искомый.
 Оцените сложность операции поиска, изменилась ли она?

TODO: 7.6. Добавьте тесты для добавления, удаления и поиска элемента
 по его значению -- каждый случай с учётом признака упорядоченности.
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        return 0
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        pass
        # автоматическая вставка value
        # в нужную позицию

    def find(self, val):
        return None  # здесь будет ваш код

    def delete(self, val):
        # TODO: from LinkedList2
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


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0

