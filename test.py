import pytest
from itertools import product

from linkedList import Node, LinkedList


initVals = ([], [2], [1, 2, 2, 3, 2, 5],
            [None, None, None], [2, 2, 2, 2],
            [0, 0, 0], [None, 1, 4, 1, 1],
            [2, 1, 3, 2, 2], [2, 1, 2, 3, 2],
            [0, 1, 4, 3, 2], [2, 2, 0, 3, 2],
            #TODO: add linked vals
            )
valsArgs = (None, 0, 'not listed', 2)

delAllArgs = (False, True)
DELETE_PARAMS = dict(
    argnames='initVals, delVal, delAll',
    argvalues=list(product(initVals, valsArgs, delAllArgs)))


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


def get_correct_delete_vals(init_vals: list, del_val, del_all: bool):
    correct_vals = list(init_vals)  # copy list
    if del_all:
        correct_vals = list(filter(lambda x: x != del_val, correct_vals))
    else:
        try:
            correct_vals.remove(del_val)
        except ValueError:
            pass
    return correct_vals


# --------------------------- pytest settings -----------------------

class BaseTest:
    @classmethod
    def setup_class(cls):
        print(f'============= {cls.__name__} STARTED =================')

    @classmethod
    def teardown_class(cls):
        print(f'============= {cls.__name__} FINISHED ================')

    def setup_method(self, method):
        print(method.__name__, 'start')

    def teardown_method(self, method):
        print(method.__name__, 'finish', '\n')


def setup_function(func):
    print(f'============= {func.__name__} STARTED =================')

def teardown_function(func):
    print(f'============= {func.__name__} FINISHED ================')


# --------------------------- CLEAN ---------------------------------

@pytest.mark.parametrize('vals', ([2, 11, 1], [100], [0], []))
def test_clean(vals):
    LList = create_list(vals)
    print('init state:', get_list_vals(LList))
    print('expected:', [])
    LList.clean()
    result = get_list_vals(LList)
    print('result:', result)
    assert result == []


# --------------------------- DELETE --------------------------------

class TestDelete(BaseTest):
    @pytest.mark.parametrize(**DELETE_PARAMS)
    def test_delete(self, initVals, delVal, delAll):
        expected = get_correct_delete_vals(initVals, delVal, delAll)
        LList = create_list(initVals)
        print('init state:', get_list_vals(LList))
        print(f'to del{" ALL" if delAll else ""}:', delVal)
        print('expected:', expected)
        LList.delete(delVal, all=delAll)
        result = get_list_vals(LList)
        print('result:', result)
        assert result == expected

