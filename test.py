import pytest
from itertools import product

from linkedList import Node, LinkedList
from main import create_list, get_list_vals, get_nodes_vals, merge_lists


# linked objects, can be used to tests
d = dict((i, v)for i, v in enumerate([1, None, [], 'test']))
l_list = LinkedList()
[l_list.add_in_tail(Node(v)) for v in [0, None, d, 2]]

INIT_VALS = ([], [2], [1, 2, 2, 3, 2, 5],
             [None, None, None], [2, 2, 2, 2],
             [0, 0, 0], [None, 1, 4, 1, 1],
             [2, 1, 3, 2, 2], [2, 1, 2, 3, 2],
             [0, 1, 4, 3, 2], [2, 2, 0, 3, 2],
             [0, d, l_list, 3, 2], [d, 2, 0, 3, 2],
             [l_list, 0, 0], [None, 1, 4, d, l_list],)
VALS_ARGS = (None, 0, l_list, 'not listed', 2)


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
    @pytest.mark.parametrize('initVals', ([2, 11, 1], [100], [0], []))
    def test_clean(self, initVals: list):
        LList = create_list(initVals)
        print('init state:', get_list_vals(LList))
        print('expected (clean):', [])
        LList.clean()
        result = get_list_vals(LList)
        print('result:', result)
        assert result == []


# --------------------------- LEN -----------------------------------

class TestLen(BaseTest):
    @pytest.mark.parametrize('initVals', INIT_VALS)
    def test_len(self, initVals: list):
        expected = len(initVals)
        LList = create_list(initVals)
        print('init state:', get_list_vals(LList))
        print('expected (len):', expected)
        result = LList.len()
        print('result:', result)
        assert result == expected


# --------------------------- FIND ALL ------------------------------

FIND_ALL_PARAMS = dict(
    argnames='init_vals, val',
    argvalues=list(product(INIT_VALS, VALS_ARGS)))


class TestFindAll(BaseTest):
    @staticmethod
    def get_correct_findall_nodes(init_vals: list, val) -> list:
        return [init_vals[i:]
                for i, v in enumerate(list(init_vals))
                if v == val]

    @pytest.mark.parametrize(**FIND_ALL_PARAMS)
    def test_find_all(self, init_vals: list, val):
        expected = self.get_correct_findall_nodes(init_vals, val)
        LList = create_list(init_vals)
        print('init state:', get_list_vals(LList))
        print(f'find all nodes with "{val}"')
        print('expected:', expected)
        nodes = LList.find_all(val)
        result = get_nodes_vals(nodes)
        print('result:', result)
        assert result == expected


# --------------------------- DELETE --------------------------------

DELETE_PARAMS = dict(
    argnames='init_vals, del_val, del_all',
    argvalues=list(product(INIT_VALS, VALS_ARGS, (False, True))))


class TestDelete(BaseTest):
    @staticmethod
    def get_correct_delete_vals(init_vals: list, del_val, del_all: bool):
        corr_vals = list(init_vals)  # copy list
        if del_all:
            corr_vals = list(filter(lambda x: x != del_val, corr_vals))
        else:
            try:
                corr_vals.remove(del_val)
            except ValueError:
                pass
        return corr_vals

    @pytest.mark.parametrize(**DELETE_PARAMS)
    def test_delete(self, init_vals: list, del_val, del_all: bool):
        expected = self.get_correct_delete_vals(init_vals, del_val, del_all)
        LList = create_list(init_vals)
        print('init state:', get_list_vals(LList))
        print(f'del {"ALL nodes" if del_all else "1st node"} with "{del_val}"')
        print('expected:', expected)
        LList.delete(del_val, all=del_all)
        result = get_list_vals(LList)
        print('result:', result)
        assert result == expected


# --------------------------- INSERT --------------------------------

INSERT_PARAMS = dict(
    argnames='init_vals, after_val, val',
    argvalues=[
        ([2, 1, 3, 2, 2], 3, 2), ([2, 1, 3, 2, 2], 3, 4),
        ([2, 1, 3, 2, 2], 2, 4), ([2, 1, 3, 2, 2], 2, 2),
        ([4, 1, 3, 1, 2], 2, 2), ([4, 1, 3, 1, 2], 4, 6),
        ([2], 2, 0), ([2], 2, 2), ([2], 2, None), ([None, None, None], None, 6),
        ([4, 1, l_list, 1, 2], l_list, 8), ([4, 1, l_list, 1, 2], l_list, 0),
        ([d, 5], d, None), ([None, 5], None, d), ([2, l_list], l_list, None),
        ([d, 5], d, {'opa': l_list}), ([5, None], None, d),
        ([d, 5], d, 0), ([2, l_list], l_list, 0), ([2, l_list], l_list, d),
        ([], None, 0), ([], None, None), ([], None, 7),
    ])


class TestInsert(BaseTest):
    @staticmethod
    def get_correct_insert_vals(init_vals: list, after_val, val):
        corr_vals = list(init_vals)  # copy list
        print(corr_vals is not [], corr_vals is [], bool(corr_vals))
        ins_ind = (corr_vals.index(after_val) + 1) if corr_vals else 0
        corr_vals.insert(ins_ind, val)
        return corr_vals

    @pytest.mark.parametrize(**INSERT_PARAMS)
    def test_insert(self, init_vals: list, after_val, val):
        expected = self.get_correct_insert_vals(init_vals, after_val, val)
        LList = create_list(init_vals)
        print('init state:', get_list_vals(LList))
        print(f'after node with "{after_val}" ins node with"{val}"')
        print('expected:', expected)
        afterNode = LList.find(after_val)
        LList.insert(afterNode, Node(val))
        result = get_list_vals(LList)
        print('result:', result)
        assert result == expected


# --------------------------- MERGE ---------------------------------

MERGE_PARAMS = dict(
    argnames='init_vals1, init_vals2',
    argvalues=[
        ([2, 1, 3, 2, 2], [2, 1, 3, 2, 2]),
        ([2, 1, 3, 2, 2], [8, 9, 7, 8, 8]),
        ([-7, 5, 0, 1, -5], [-9, 9, 2, 4, 6]),
        ([], []), ([0], [0]), ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([0, 0, 0, 0], [7, 0, -1, -12]),
    ])


class TestMerge(BaseTest):
    @staticmethod
    def get_correct_merge_vals(init_vals1: list, init_vals2: list):
        if len(init_vals1) != len(init_vals2):
            raise AttributeError('Lengths of lists are not equal')
        if not all([isinstance(v, int) for v in init_vals1] +
                   [isinstance(v, int) for v in init_vals2]):
            raise AttributeError('Some values are not integer')
        return [v1 + v2 for v1, v2 in zip(init_vals1, init_vals2)]

    @pytest.mark.parametrize(**MERGE_PARAMS)
    def test_merge(self, init_vals1: list, init_vals2: list):
        expected = self.get_correct_merge_vals(init_vals1, init_vals2)
        LList1, LList2 = create_list(init_vals1), create_list(init_vals2)
        print('init state:', get_list_vals(LList1), get_list_vals(LList2))
        print('expected (sum vals):', expected)
        newLList = merge_lists(LList1, LList2)
        result = get_list_vals(newLList)
        print('result:', result)
        assert result == expected

