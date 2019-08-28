from stack_4.stack import Stack
from queue_5.queue import Queue


def offset_queue(queue: Queue, n: int) -> Queue:
    return Queue.create(queue.queue[n:] + queue.queue[:n])


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
        return self.inputs.to_list()[::-1] + self.outputs.to_list()

    @classmethod
    def create(cls, vals: list):
        new_queue = cls()
        for v in vals:
            new_queue.enqueue(v)
        return new_queue

