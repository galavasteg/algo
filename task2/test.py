import pytest
from itertools import product

from task2.linkedList2 import Node, LinkedList2
from task2.main import create_list, get_list_vals, get_nodes_vals


# linked objects, can be used in tests' params
d = dict((i, v)for i, v in enumerate([1, None, [], 'test']))
l_list = LinkedList2()
[l_list.add_in_tail(Node(v)) for v in [0, None, d, 2]]

INIT_VALS = ([], [2], [1, 2, 2, 3, 2, 5],
             [None, None, None], [2, 2, 2, 2],
             [0, 0, 0], [None, 1, 4, 1, 1],
             [2, 1, 3, 2, 2], [2, 1, 2, 3, 2],
             [0, 1, 4, 3, 2], [2, 2, 0, 3, 2],
             [0, d, l_list, 3, 2], [d, 2, 0, 3, 2],
             [l_list, 0, 0], [None, 1, 4, d, l_list],)
# --------------------------- pytest settings -----------------------

class BaseTest:
    @classmethod
    def setup_class(cls):
        print(f'============= {cls.__name__} STARTED =================')

    @classmethod
    def teardown_class(cls):
        print(f'============= {cls.__name__} FINISHED ================')

    def teardown_method(self, method):
        print()


# --------------------------- CLEAN ---------------------------------

class TestClean(BaseTest):
    @pytest.mark.parametrize('init_vals', ([2, 1], [0], [None], []))
    def test_clean(self, init_vals: list):
        LList = create_list(init_vals)
        print('init state:', get_list_vals(LList))
        print('expected (clean):', [])
        LList.clean()
        result = get_list_vals(LList)
        print('result:', result)
        assert result == []


# --------------------------- LEN -----------------------------------

class TestLen(BaseTest):
    @pytest.mark.parametrize('init_vals', INIT_VALS)
    def test_len(self, init_vals: list):
        expected = len(init_vals)
        LList = create_list(init_vals)
        print('init state:', get_list_vals(LList))
        print('expected (len):', expected)
        result = LList.len()
        print('result:', result)
        assert result == expected


