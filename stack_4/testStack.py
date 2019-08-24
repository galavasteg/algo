import pytest

from stack_4.stack import Stack


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
            (list('(()()(()'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ),
            (8, 10, )):
        print(vals, res)
        assert Stack.create(vals).size() == res


