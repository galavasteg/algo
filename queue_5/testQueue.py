from queue_5.queue import Queue
from queue_5.queue_plus import StackedQueue


# --------------------------- pytest settings -----------------------

class BaseTest:
    @classmethod
    def setup_class(cls):
        print('============= {} STARTED ================='.format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        print('============= {} FINISHED ================'.format(cls.__name__))

    def teardown_method(self, method):
        print()


# --------------------------- SIZE ----------------------------------

def test_size():
    for vals, res in zip(
            (list('(()()(()'), [0, 1, 2, 3, 4, 5, 6], []),
            (8, 7, 0)):
        for cls in (Queue, StackedQueue):
            print(cls.__name__, vals, res)
            assert cls.create(vals).size() == res


# --------------------------- ENQUEUE -------------------------------

def test_enqueue():
    for (vals, adds), res in zip(
            (([1, 2], [3, 4]), ([], []), ([], [0]), ([], [None]),
             (list(range(5)), list(range(5, 0, -1)))),
            ([4, 3, 2, 1], [], [0], [None], [1,2,3,4,5,4,3,2,1,0])):
        for cls in (Queue, StackedQueue):
            queue = cls.create(vals)
            for a in adds:
                queue.enqueue(a)
            print(cls.__name__, vals, '+', adds, res)
            assert queue.to_list() == res


# --------------------------- DEQUEUE -------------------------------

def test_dequeue():
    for vals, (cor_res, popped) in zip(
            ([1, 2, 3, 4], [], [0], [None, 0, 17]),
            (([4, 3, 2], 1), ([], None), ([], 0),
             ([17, 0], None))):
        for cls in (Queue, StackedQueue):
            queue = cls.create(vals)
            p = queue.dequeue()
            print(cls.__name__, vals, 'pop:', cor_res, popped)
            assert queue.to_list() == cor_res and p == popped


if __name__ == '__main__':
    test_size()
    test_enqueue()
    test_dequeue()

