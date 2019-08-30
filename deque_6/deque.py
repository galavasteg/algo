"""
6.1. The measure of complexity of the addHead/removeHead and
 addTail/removeTail methods depends to a large extent on what
 we choose as list heading and list tail. Rate the complexity
 of these methods in both options.
6.2. Write a function that uses deque to determine that
 the string is a palindrome (a string that reads the same
 backward as forward).
6.3. Write tests for addHead/removeHead and addTail/removeTail
 methods: check the deque size and deque state after
 adding/removing elements.
"""


class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        # 6.1. head - [0, ...] - O(n)
        # head - [..., -1] - O(1)
        self.deque.insert(0, item)

    def addTail(self, item):
        # 6.1. tail - [..., -1] - O(1)
        # tail - [0, ...] - O(n)
        self.deque.append(item)

    def removeFront(self):
        # 6.1. head - [0, ...] - O(n)
        # head - [..., -1] - O(1)
        if self.deque:
            return self.deque.pop(0)

    def removeTail(self):
        # 6.1. tail - [..., -1] - O(1)
        # tail - [0, ...] - O(n)
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

