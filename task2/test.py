import pytest
from itertools import product

from task2.linkedList2 import Node, LinkedList2


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
VALS_ARGS = (None, 0, l_list, 'not listed', 2)


def get_node_vals_view(l_vals: list, ind: int):
    prev_vals = l_vals[:ind]
    next_vals = l_vals[ind+1:]
    return prev_vals, l_vals[ind], next_vals


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
        LList = LinkedList2.create(init_vals)
        print('init state:', LList.vals)
        print('expected (clean):', [])
        LList.clean()
        result = LList.vals
        print('result:', result)
        assert result == []


# --------------------------- LEN -----------------------------------

class TestLen(BaseTest):
    @pytest.mark.parametrize('init_vals', INIT_VALS)
    def test_len(self, init_vals: list):
        expected = len(init_vals)
        LList = LinkedList2.create(init_vals)
        print('init state:', LList.vals)
        print('expected (len):', expected)
        result = LList.len()
        print('result:', result)
        assert result == expected


# --------------------------- ADD INN HEAD -------------------------

ADD_IN_HEAD_PARAMS = dict(
    argnames='init_vals, val',
    argvalues=list(product(INIT_VALS, VALS_ARGS)))

class TestAddInHead(BaseTest):
    @pytest.mark.parametrize(**ADD_IN_HEAD_PARAMS)
    def test_len(self, init_vals: list, val):
        expected = list(init_vals)
        expected.insert(0, val)
        LList = LinkedList2.create(init_vals)
        print('init state:', LList.vals)
        print(f'insert "{val}" at the beginning')
        print('expected:', expected)
        LList.add_in_head(Node(val))
        result = LList.vals
        print('result:', result)
        assert result == expected


# --------------------------- FIND - FIND ALL -----------------------

FIND_PARAMS = dict(
    argnames='init_vals, val',
    argvalues=list(product(INIT_VALS, VALS_ARGS)))


class TestFind(BaseTest):
    @staticmethod
    def get_correct_find_node_vals(init_vals: list, val) -> tuple:
        return (get_node_vals_view(init_vals, init_vals.index(val))
                if val in init_vals else None)

    @pytest.mark.parametrize(**FIND_PARAMS)
    def test_find(self, init_vals: list, val):
        expected = self.get_correct_find_node_vals(init_vals, val)
        LList = LinkedList2.create(init_vals)
        print('init state:', LList.vals)
        print(f'find 1-st node with "{val}"')
        print('expected:', expected)
        node = LList.find(val)
        result = ((node.prev_vals(), val, node.next_vals())
                  if node else None)
        print('result:', result)
        assert result == expected

    @staticmethod
    def get_correct_findall_nodes_vals(init_vals: list, val) -> list:
        return [get_node_vals_view(init_vals, i)
                for i, v in enumerate(init_vals)
                if v == val]

    @pytest.mark.parametrize(**FIND_PARAMS)
    def test_find_all(self, init_vals: list, val):
        expected = self.get_correct_findall_nodes_vals(init_vals, val)
        LList = LinkedList2.create(init_vals)
        print('init state:', LList.vals)
        print(f'find all nodes with "{val}"')
        print('expected:', expected)
        nodes = LList.find_all(val)
        result = [(n.prev_vals(), n.value, n.next_vals())
                  for n in nodes]
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
        LList = LinkedList2.create(init_vals)
        print('init state:', LList.vals)
        print(f'del {"ALL nodes" if del_all else "1-st node"} with "{del_val}"')
        print('expected:', expected)
        LList.delete(del_val, all=del_all)
        result = LList.vals
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
        ([4, 1, 3, 1, 2], None, 6),
        ([2], None, 0), ([2], None, None), ([2], None, 7),
        ([d], None, l_list), ([2], None, 7), ([list], None, 0),
    ])


class TestInsert(BaseTest):
    @staticmethod
    def get_correct_insert_vals(init_vals: list, afterNode: Node, val):
        corr_vals = list(init_vals)  # copy list
        print(corr_vals is not [], corr_vals is [], bool(corr_vals))
        ins_ind = (corr_vals.index(afterNode.value if afterNode else
                                   corr_vals[-1])
                   + 1 if corr_vals else 0)
        corr_vals.insert(ins_ind, val)
        return corr_vals

    @pytest.mark.parametrize(**INSERT_PARAMS)
    def test_insert(self, init_vals: list, after_val, val):
        LList = LinkedList2.create(init_vals)
        print('init state:', LList.vals)
        print(f'after node with "{after_val}" ins node with"{val}"')
        afterNode = LList.find(after_val)
        expected = self.get_correct_insert_vals(init_vals, afterNode, val)
        print('expected:', expected)
        LList.insert(afterNode, Node(val))
        result = LList.vals
        print('result:', result)
        assert result == expected


