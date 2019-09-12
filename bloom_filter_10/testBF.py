from itertools import product

import pytest

from bloom_filter_10.bloomFilter import BloomFilter as BF


init = "0123456789"
VALS = tuple(init[i:] + init[:i] for i in range(len(init)))
INIT_VALS = (((),) +
             tuple((VALS[i],) for i in range(len(VALS))) +
             tuple(tuple(VALS[i+1:] + VALS[:i])
                   for i in range(len(VALS))))

PARAMS = dict(
    argnames='string',
    argvalues=VALS)


# --------------------------- ADD -----------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_add(string):
    size = 32
    bf = BF(size)
    print('\ninit state', size)
    print(bf.storage)
    print('value to add "{0}"'.format(string))
    corr_res = [x for x in bf.storage]
    corr_res[BF.hash(string, size, 17)] = corr_res[BF.hash(string, size, 223)] = 1
    bf.add(string)
    assert bf.storage == corr_res


# --------------------------- IS VALUE ------------------------------

PUT_PARAMS = dict(
    argnames='init_vals, string',
    argvalues=tuple(product(INIT_VALS, VALS)))


@pytest.mark.parametrize(**PUT_PARAMS)
def test_is_value(init_vals, string):
    size = 32
    bf = BF.create(size, init_vals)
    print('\ninit state', size)
    print(init_vals)
    print(tuple(i for i in range(10)) * (size // 10) +
          tuple(i for i in range(size % 10)))
    print(bf.storage)
    print('value to check "{0}"'.format(string))
    h1, h2 = BF.hash(string, size, 17), BF.hash(string, size, 223)
    corr_res = all((bf.storage[h1], bf.storage[h2]))
    print('expected:', corr_res)
    assert bf.is_value(string) == corr_res


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_add()
    test_is_value()

