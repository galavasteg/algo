from itertools import product

import pytest

from orederedList_7.orderedList import OrderedList, OrderedStringList


def get_correct_nodes_vals(init_vals: list, val) -> tuple:
    return (get_node_vals_view(init_vals, init_vals.index(val))
            if val in init_vals else None)


def get_node_vals_view(l_vals: list, ind: int):
    prev_vals = l_vals[:ind]
    next_vals = l_vals[ind+1:]
    return prev_vals, l_vals[ind], next_vals


def get_correct_delete_vals(init_vals: list, del_val):
    corr_vals = list(init_vals)  # copy list
    try:
        corr_vals.remove(del_val)
    except ValueError:
        pass
    return [get_node_vals_view(corr_vals, i)
            for i, v in enumerate(corr_vals)]


VALS_ARGS = (-9, 0, 1, 1, 9)
INIT_VALS = [[]] + [[v] for v in VALS_ARGS]
INIT_VALS = tuple(INIT_VALS + [list(VALS_ARGS[:i] + VALS_ARGS[i+1:])
                               for i in range(len(VALS_ARGS))])
ASC_ARGS = (True, False)

PARAMS = dict(
    argnames='init_vals, asc, val',
    argvalues=list(product(INIT_VALS, ASC_ARGS, VALS_ARGS)))


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


# --------------------------- ADD -----------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_add(init_vals: list, asc: bool, val):
    expected = list(init_vals) + [val]
    expected = sorted(expected, reverse=not asc)
    expected = [get_node_vals_view(expected, i)
                for i, v in enumerate(expected)]
    OList = OrderedList.create(init_vals, asc)
    print('\ninit state', asc, ':', [n.value for n in OList.get_all()])
    print('insert "{val}"'.format(val=val))
    print('expected:', expected)
    OList.add(val)
    result = [(n._prev_vals(), n.value, n._next_vals())
              for n in OList.get_all()]
    print('result:', result)
    assert result == expected


# --------------------------- FIND ----------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_find(init_vals: list, asc: bool, val):
    expected = list(init_vals)
    expected = sorted(expected, reverse=not asc)
    expected = get_correct_nodes_vals(expected, val)
    OList = OrderedList.create(init_vals, asc)
    print('\ninit state', asc, ':', [n.value for n in OList.get_all()])
    print('find "{val}"'.format(val=val))
    print('expected:', expected)
    node = OList.find(val)
    result = ((node._prev_vals(), val, node._next_vals())
              if node else None)
    print('result:', result)
    assert result == expected


# --------------------------- DELETE --------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_delete(init_vals: list, asc: bool, val):
    expected = list(init_vals)
    expected = sorted(expected, reverse=not asc)
    expected = get_correct_delete_vals(expected, val)
    OList = OrderedList.create(init_vals, asc)
    print('\ninit state', asc, ':', [n.value for n in OList.get_all()])
    print('delete "{val}"'.format(val=val))
    print('expected:', expected)
    OList.delete(val)
    result = [(n._prev_vals(), n.value, n._next_vals())
              for n in OList.get_all()]
    print('result:', result)
    assert result == expected


# --------------------------- COMPARE STRINGS -----------------------

STR_COMP_PARAMS = dict(
    argnames='s1, s2, res',
    argvalues=[('     sds sdcsdcs  ', 'sds sdcsdcs  ', 0),
               ('       ', '', 0), ('', '', 0),
               ('     sds Adcsdcs  ', 'sds sdcsdcs  ', -1),
               ('     sds sdcsdcs  ', 'sds Sdcsdcs  ', 1),
            ])


@pytest.mark.parametrize(**STR_COMP_PARAMS)
def test_compare_strs(s1: str, s2: str, res: bool):
    OSList = OrderedStringList(True)
    print('compare "{s1}" and "{s2}"'.format(s1=s1, s2=s2))
    print('expected:', res)
    result = OSList.compare(s1, s2)
    print('result:', result)
    assert result == res


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_add()
    test_find()
    # test_len()
    # test_get_all()
    # test_clean()
    test_compare()
    test_delete()

