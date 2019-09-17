from itertools import product
from math import gcd

import pytest

from set_11.powerSet import PowerSet


VALS_ARGS = ('', 'лещ', 'dca')
INIT_VALS = (tuple(),) + tuple((v,) for v in VALS_ARGS)
INIT_VALS = tuple(INIT_VALS + tuple(VALS_ARGS[:i] + VALS_ARGS[i+1:]
                                    for i in range(len(VALS_ARGS))) +
                  (VALS_ARGS,))
PARAMS = dict(
    argnames='vals, val',
    argvalues=tuple(product(INIT_VALS, VALS_ARGS)))
SETS_PARAMS = dict(
    argnames='vals1, vals2',
    argvalues=tuple(product(INIT_VALS, INIT_VALS)))


# --------------------------- PUT -----------------------------------


# --------------------------- REMOVE --------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_remove(vals, val):
    ps = PowerSet.create(vals)
    i_val_map = dict(filter(lambda x: x[1] is not None, enumerate(ps.slots)))
    init_set = set(i_val_map.values())
    print('\ninit ind-val mapping:', i_val_map)
    print('init set:', init_set)
    print('remove "{val}"'.format(val=val))
    expected = False
    if val in init_set:
        expected = True
        init_set.remove(val)  # expected set
    print('expected:', init_set)
    res = ps.remove(val)
    res_set = set(filter(lambda x: x is not None, ps.slots))
    print('result:', res_set)
    assert res == expected and res_set == init_set


# --------------------------- INTERSECTION --------------------------

@pytest.mark.parametrize(**SETS_PARAMS)
def test_inters(vals1, vals2):
    print()
    ps1 = PowerSet.create(vals1)
    ps2 = PowerSet.create(vals2)
    i_val_map1 = dict(filter(lambda x: x[1] is not None, enumerate(ps1.slots)))
    i_val_map2 = dict(filter(lambda x: x[1] is not None, enumerate(ps2.slots)))
    init_set1 = set(i_val_map1.values())
    init_set2 = set(i_val_map2.values())
    print('init A ind-val mapping:', i_val_map1)
    print('init B ind-val mapping:', i_val_map2)
    print('init sets:', init_set1, init_set2)
    expected = init_set1.intersection(init_set2)
    print('intersection expected', expected)
    res = ps1.intersection(ps2)
    i_val_res_map = dict(filter(lambda x: x[1] is not None, enumerate(res.slots)))
    init_res_set = set(i_val_res_map.values())
    print('result:', init_res_set)
    assert init_res_set == expected


# --------------------------- UNION ---------------------------------

@pytest.mark.parametrize(**SETS_PARAMS)
def test_union(vals1, vals2):
    print()
    ps1 = PowerSet.create(vals1)
    ps2 = PowerSet.create(vals2)
    i_val_map1 = dict(filter(lambda x: x[1] is not None, enumerate(ps1.slots)))
    i_val_map2 = dict(filter(lambda x: x[1] is not None, enumerate(ps2.slots)))
    init_set1 = set(i_val_map1.values())
    init_set2 = set(i_val_map2.values())
    print('init A ind-val mapping:', i_val_map1)
    print('init B ind-val mapping:', i_val_map2)
    print('init sets:', init_set1, init_set2)
    expected = init_set1.union(init_set2)
    print('union expected', expected)
    res = ps1.union(ps2)
    i_val_res_map = dict(filter(lambda x: x[1] is not None, enumerate(res.slots)))
    init_res_set = set(i_val_res_map.values())
    print('result:', init_res_set)
    assert init_res_set == expected


# --------------------------- DIFFERENCE ----------------------------


# --------------------------- ISSUBSET ------------------------------


