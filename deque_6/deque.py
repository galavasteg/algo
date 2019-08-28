"""
TODO: 7.1. Почему и как будет различаться мера сложности
 для addHead/removeHead и addTail/removeTail?

TODO: 6.2. Напишите функцию, которая с помощью deque проверяет,
 является ли некоторая строка палиндромом (читается одинаково
 слева направо и справа налево).

TODO: 7.3. Добавьте для каждого из четырёх вышеупомянутых методов
 тесты: проверяйте изменившуюся длину очереди и наличие или
 отстутствие в ней добавляемого/удаляемого элемента.
"""


class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.deque:
            return self.deque.pop(0)

    def removeTail(self):
        if self.deque:
            return self.deque.pop(-1)

    def size(self):
        return len(self.deque)

    def to_list(self):
        return self.deque

    @classmethod
    def create(cls, vals: list):
        new_queue = cls()
        for v in vals:
            new_queue.addTail(v)
        return new_queue

    @classmethod
    def is_pali(cls, s: str):
        d = cls.create(list(s.lower()))
        return all([d.removeFront() == d.removeTail()
                    for _ in range(d.size() // 2)])

