from math import ceil
from itertools import product

import pytest

from dynamic_list_3.dynArray import DynArray


d = dict((i, v)for i, v in enumerate([1, None, [], 'test']))


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


# --------------------------- DELETE --------------------------------

DELETE_PARAMS = dict(
    argnames='init_vals, del_indices',
    argvalues=[
        ([2], [0]), ([1, 2, 2, 3, 2, 5], [0]),
        ([None, d, None], [0]), ([0, 0, d], [0]),
        ([None, 1, 4, 5, 1], [1]), ([0, 1, 2, 3, 4], [1, 3]),
        ([5, d, 0, 3, 2], [1]), ([2, 1, 3, 2, 2], [3]),
        ([0, 1, 4, 3, 2], [2]), ([0, 1, 4, 3, 2], [4]),
        (list(range(17)), [16, 0]), ([0, 1, 4, 3, 0], [4]),
        (list(range(35)), list(range(15))),
        (list(range(32)), list(range(16, 0, -1))),
    ])
DELETE_NEGATIVE_PARAMS = dict(
    argnames='init_vals, del_indices',
    argvalues=[
        ([], [0]), ([], [-6]), ([], [1]), ([], [6]),
        (list(range(33)), [33]), ([2, 1, 3, 2, 2], [6]),
        ([None, None, None], [-1]), ([2, 1, 3, 2, 2], [5]),
        ([2, 2, 2, 2], [-10]), ([0, 0, ''], [15]),
        ([2, 2, 2, 2, 5], [0, 4]),
        (list(range(32)), list(range(17))),
    ])

