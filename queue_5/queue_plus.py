from queue_5.queue import Queue


def offset_queue(queue: Queue, n: int) -> Queue:
    return Queue.create(queue.queue[n:] + queue.queue[:n])


