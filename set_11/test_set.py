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


# --------------------------- UNION ---------------------------------


# --------------------------- DIFFERENCE ----------------------------


# --------------------------- ISSUBSET ------------------------------


