from itertools import product

import pytest

from native_dictionary_9.nativeDict import NativeDictionary as ND


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


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_is_key()

