from itertools import product
from math import gcd

import pytest

from hash_tables_8.hashTable import HashTable


SIZES_ARGS = (1, 3, 11, 17)
STEPS_ARGS = (2,) + SIZES_ARGS
VALS_ARGS = ('', 'лещ', 'лещи', 'лщеи', 'dca', 'dac')
INIT_VALS = (tuple(),) + tuple((v,) for v in VALS_ARGS)
INIT_VALS = tuple(INIT_VALS + tuple(VALS_ARGS[:i] + VALS_ARGS[i+1:]
                                    for i in range(len(VALS_ARGS))))
PARAMS = dict(
    argnames='sz, stp, vals, val',
    argvalues=tuple(product(SIZES_ARGS, STEPS_ARGS, INIT_VALS, VALS_ARGS)))


# --------------------------- HASH ----------------------------------

def test_hash():
    for sz, value in zip(SIZES_ARGS, VALS_ARGS):
        ht = HashTable(sz, 1)
        assert ht.hash_fun(value) == HashTable.hash(value, sz)


# --------------------------- SEEK ----------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_seek(sz, stp, vals, val):
    ht = HashTable.create(sz, stp, vals)
    corr_slots = tuple(i for i, v in enumerate(ht.slots) if v is None)
    if gcd(sz, stp) != 1:
        corr_slots = corr_slots + (None,)
    corr_slots = corr_slots or (None,)
    print('\ninit state,', sz, stp, ':', ht.slots)
    print('seek "{val}"'.format(val=val))
    print('expected seek in :', corr_slots)
    assert ht.seek_slot(val) in corr_slots


# --------------------------- PUT -----------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_put(sz, stp, vals, val):
    ht = HashTable.create(sz, stp, vals)
    corr_slots = tuple(i for i, v in enumerate(ht.slots) if v is None)
    if gcd(sz, stp) != 1:
        corr_slots = corr_slots + (None,)
    corr_slots = corr_slots or (None,)
    print('\ninit state,', sz, stp, ':', ht.slots)
    print('put "{val}"'.format(val=val))
    print('expected put ind in:', corr_slots)
    res = ht.put(val)
    print('result:', ht.slots)
    assert res in corr_slots


# --------------------------- FIND ----------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_find(sz, stp, vals, val):
    ht = HashTable.create(sz, stp, vals)
    corr_res = ht.slots.index(val) if val in ht.slots else None
    print('\ninit state,', sz, stp, ':', ht.slots)
    print('find "{val}"'.format(val=val))
    print('expected:', corr_res)
    assert ht.find(val) == corr_res


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_hash()
    test_seek()
    test_put()
    test_find()

