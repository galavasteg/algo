"""
5.3. Write a function which "rotate" the queue on
 **N** elements.
5.4. Try to realize the Queue class using two Stacks.
"""

from stack_4.stack import Stack
from queue_5.queue import Queue


def get_shifted_queue(queue: Queue, n: int) -> Queue:
    s_queue = Queue.create(queue.to_list())
    size = s_queue.size()
    if size > 1:
        n_ = n if abs(n) <= size else (abs(n) % size)
        for _ in range(n_ if n_ >= 0 else size + n_):
            s_queue.enqueue(s_queue.dequeue())
    return s_queue


class StackedQueue:
    def __init__(self):
        self.inputs = Stack()
        self.outputs = Stack()

    def enqueue(self, item):
        self.inputs.push(item)

    def dequeue(self):
        if not self.outputs.size():
            while self.inputs.size():
                self.outputs.push(self.inputs.pop())
        return self.outputs.pop()

    def size(self):
        return self.inputs.size() + self.outputs.size()

    def to_list(self):
        return self.outputs.to_list()[::-1] + self.inputs.to_list()

    @classmethod
    def create(cls, vals: list):
        new_queue = cls()
        for v in vals:
            new_queue.enqueue(v)
        return new_queue

