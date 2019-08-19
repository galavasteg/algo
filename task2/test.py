import pytest
from itertools import product

from task2.linkedList2 import Node, LinkedList2
from task2.main import create_list, get_list_vals, get_nodes_vals


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


