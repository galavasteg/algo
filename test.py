import pytest
from itertools import product

from linkedList import Node, LinkedList
from main import create_list, get_list_vals, get_nodes_vals


d = dict((i, v)for i, v in enumerate([2, 1, 3, 2, 2]))
l_list = LinkedList()
[l_list.add_in_tail(Node(v)) for v in [0, 1, 4, 3, 2]]
INIT_VALS = ([], [2], [1, 2, 2, 3, 2, 5],
             [None, None, None], [2, 2, 2, 2],
             [0, 0, 0], [None, 1, 4, 1, 1],
             [2, 1, 3, 2, 2], [2, 1, 2, 3, 2],
             [0, 1, 4, 3, 2], [2, 2, 0, 3, 2],
             [0, d, l_list, 3, 2], [d, 2, 0, 3, 2],
             [l_list, 0, 0], [None, 1, 4, d, l_list],)
VALS_ARGS = (None, 0, l_list, 'not listed', 2)

DELETE_PARAMS = dict(
    argnames='initVals, delVal, delAll',
    argvalues=list(product(INIT_VALS, VALS_ARGS, (False, True))))

FIND_ALL_PARAMS = dict(
    argnames='initVals, val',
    argvalues=list(product(INIT_VALS, VALS_ARGS)))


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


# --------------------------- CLEAN ---------------------------------

class TestClean(BaseTest):
    @pytest.mark.parametrize('initVals', ([2, 11, 1], [100], [0], []))
    def test_clean(self, initVals: list):
        LList = create_list(initVals)
        print('init state:', get_list_vals(LList))
        print('expected:', [])
        LList.clean()
        result = get_list_vals(LList)
        print('result:', result)
        assert result == []


# --------------------------- FIND ALL ------------------------------

class TestFindAll(BaseTest):
    @staticmethod
    def get_correct_findall_nodes(init_vals: list, val) -> list:
        return [init_vals[i:]
                for i, v in enumerate(list(init_vals))
                if v == val]

    @pytest.mark.parametrize(**FIND_ALL_PARAMS)
    def test_find_all(self, initVals: list, val):
        expected = self.get_correct_findall_nodes(initVals, val)
        LList = create_list(initVals)
        print('init state:', get_list_vals(LList))
        print('to find:', val)
        print('expected:', expected)
        nodes = LList.find_all(val)
        result = get_nodes_vals(nodes)
        print('result:', result)
        assert result == expected


# --------------------------- DELETE --------------------------------

class TestDelete(BaseTest):
    @staticmethod
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

    @pytest.mark.parametrize(**DELETE_PARAMS)
    def test_delete(self, initVals: list, delVal, delAll: bool):
        expected = self.get_correct_delete_vals(initVals, delVal, delAll)
        LList = create_list(initVals)
        print('init state:', get_list_vals(LList))
        print(f'to del{" ALL" if delAll else ""}:', delVal)
        print('expected:', expected)
        LList.delete(delVal, all=delAll)
        result = get_list_vals(LList)
        print('result:', result)
        assert result == expected

