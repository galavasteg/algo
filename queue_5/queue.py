"""
TODO: 5.1. В классе Queue нам понадобятся три метода:
 size() (количество элементов в очереди), enqueue(item) -
 добавить элемент в хвост очереди, и dequeue(), который
 возвращает элемент из головы очереди, удаляя его.
TODO: 5.2. Оцените меру сложности для операций enqueue()
 и dequeue().
TODO: 5.3. Напишите функцию, которая "вращает" очередь по
 кругу на N элементов.
TODO: 5.4. Попробуйте реализовать очередь с помощью двух
 стеков.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # вставка в хвост
        pass

    def dequeue(self):
        # выдача из головы
        return None  # если очередь пустая

    def size(self):
        return 0  # размер очереди

    def to_list(self):
        return self.queue[::-1]

    @classmethod
    def create(cls, vals: list):
        new_queue = cls()
        for v in vals:
            new_queue.enqueue(v)
        return new_queue

