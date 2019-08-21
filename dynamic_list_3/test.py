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

class TestDelete(BaseTest):
    @staticmethod
    def get_correct_delete_res(da: DynArray, del_indices: list):
        array, count, capacity, fill_percent = da.meta
        for del_ind in del_indices:
            try:
                ind = del_ind if del_ind >= 0 else count - del_ind
                array.pop(ind)
            except IndexError:
                break
            count = len(array)
            fill_percent = count / capacity * 100
            if capacity > 16 and fill_percent < 50:
                capacity = int(capacity / 1.5)
                fill_percent = count / capacity * 100
        return array, count, capacity, fill_percent

    @pytest.mark.parametrize(**DELETE_NEGATIVE_PARAMS)
    def test_delete_negative(self, init_vals: list, del_indices: list):
        da = DynArray.create(init_vals)
        expected = self.get_correct_delete_res(da, del_indices)
        print('init state:', da.meta)
        print('del items in indices:', del_indices)
        print('expected: IndexError("Index is out of bounds"),', expected)
        with pytest.raises(
                IndexError, match='Index is out of bounds') as excinfo:
            for del_ind in del_indices:
                da.delete(del_ind)
        e_type, e_val = ((excinfo.typename, str(excinfo.value))
                         if excinfo else ('', ''))
        print('result: {et}("{ev}"),'.format(et=e_type, ev=e_val), da.meta)
        assert (e_type == 'IndexError' and
                e_val == 'Index is out of bounds' and
                da.meta == expected)

    @pytest.mark.parametrize(**DELETE_PARAMS)
    def test_delete(self, init_vals: list, del_indices: list):
        da = DynArray.create(init_vals)
        expected = self.get_correct_delete_res(da, del_indices)
        print('init state:', da.meta)
        print('del items in indices:', del_indices)
        print('expected:', expected)
        for del_ind in del_indices:
            da.delete(del_ind)
        result = da.meta
        print('result:', result)
        assert result == expected


