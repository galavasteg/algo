import pytest

from linkedList import Node, LinkedList


def create_list(vals: list) -> LinkedList:
    list_ = LinkedList()
    [list_.add_in_tail(Node(x)) for x in vals]
    return list_

def get_list_vals(list_: LinkedList) -> list:
    values = []
    node = list_.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values

def get_ends(list_: LinkedList) -> tuple:
    return (list_.head, list_.tail)


def setup_function(func):
    print(f'============= {func.__name__} STARTED =================')

def teardown_function(func):
    print(f'============= {func.__name__} FINISHED ================')


class BaseTest:
    init_vals = []

    @classmethod
    def setup_class(cls):
        print(f'============= {cls.__name__} STARTED =================')
        print(f'initial state: {get_vals(get_init(cls.init_vals))}')
        print()

    @classmethod
    def teardown_class(cls):
        print(f'============= {cls.__name__} FINISHED ================')

    def setup_method(self, method, *args, **kwargs):
        self.list = get_init(self.init_vals)
        print(method.__name__, 'start')

    def teardown_method(self, method):
        print(method.__name__, 'finish', '\n')


# ------------------------------- TESTS -------------------------------------

@pytest.mark.parametrize('vals', ([2, 11, 1], [100], []))
def test_clean(vals):
    LIST = get_init(vals)
    print(f'init state: {get_vals(LIST)}')
    LIST.clean()
    print(f'output: {get_vals(LIST)}')
    assert get_ends(LIST) == (None, None)


