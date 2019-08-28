"""
5.1. Realize three Queue-methods:
 1) size() - the number of elements in the queue,
 2) enqueue(item) - add **item** to the end of the queue,
 3) dequeue() - remove an item from the head of the queue
     and return this item
5.2. Rate the complexity of the enqueue() and dequeue() methods.
5.3. - 5.4. See in **queue_plus.py**
"""

# TODO: get to know about mistake in task description


class Queue:
    def __init__(self):
        self.queue = []

    # 5.2. O(1)
    def enqueue(self, item):
        self.queue.append(item)

    # 5.2. O(n)
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def to_list(self):
        return self.queue

    @classmethod
    def create(cls, vals: list):
        new_queue = cls()
        for v in vals:
            new_queue.enqueue(v)
        return new_queue

