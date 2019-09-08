from itertools import product

import pytest

from native_dictionary_9.nativeDict import NativeDictionary as ND


SIZES = (1, 3, 8, 11, 17)
KEYS = ('', 'лещ', 'лещи', 'лщеи', 'dca', 'dac')
VALS = ([None], 'что-то', (1, 3), 0, 831, '')

INIT_VALS = tuple(({},) + tuple(
    dict((k, v) for k, v
         in zip(KEYS[i+1:] + KEYS[:i-1],
                VALS[i+1:] + VALS[:i-1]))
    for i in range(len(KEYS)))
)
PARAMS = dict(
    argnames='sz, vals, key',
    argvalues=tuple(product(SIZES, INIT_VALS, KEYS)))


# --------------------------- IS KEY --------------------------------

IS_KEY_PARAMS = dict(
    argnames='sz, vals, key',
    argvalues=tuple(product(SIZES, INIT_VALS, KEYS)))


@pytest.mark.parametrize(**IS_KEY_PARAMS)
def test_is_key(sz, vals, key):
    nd = ND.create(sz, vals)
    print('\ninit state', sz, ':', vals)
    print('keys:', '\t'.join(map(lambda s: '"%s"' % s, nd.slots)))
    print('vals:', '\t'.join(map(str, nd.values)))
    print('is key "{0}"'.format(key), nd.is_key(key))
    assert nd.is_key(key) == (key in nd.slots)


# --------------------------- GET -----------------------------------

@pytest.mark.parametrize(**PARAMS)
def test_get(sz, vals, key):
    nd = ND.create(sz, vals)
    corr_val = vals[key] if key in nd.slots else None
    print('\ninit state,', sz, ':', vals)
    print('keys:', '\t'.join(map(lambda s: '"%s"' % s, nd.slots)))
    print('vals:', '\t'.join(map(str, nd.values)))
    print('get "{key}"'.format(key=key))
    print('expected value:', corr_val)
    assert nd.get(key) == corr_val


# --------------------------- PUT -----------------------------------

PUT_PARAMS = dict(
    argnames='sz, vals, key, val',
    argvalues=tuple(product(SIZES, INIT_VALS, KEYS, VALS)))


@pytest.mark.parametrize(**PUT_PARAMS)
def test_put(sz, vals, key, val):
    nd = ND.create(sz, vals)
    corr_view = list(zip(nd.slots, nd.values))
    if key in nd.slots:
        corr_view[nd.slots.index(key)] = (key, val)
    else:
        corr_view[nd.hash_fun(key)] = (key, val)
    print('\ninit state,', sz, ':', vals)
    print('keys:', '\t'.join(map(lambda s: '"%s"' % s, nd.slots)))
    print('vals:', '\t'.join(map(str, nd.values)))
    print('put "{key}": "{val}"'.format(key=key, val=val))
    print('expected dict:', corr_view)
    nd.put(key, val)
    res = list(zip(nd.slots, nd.values))
    print('result:', res)
    assert res == corr_view


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_is_key()
    test_put()
    test_get()

