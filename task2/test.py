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


