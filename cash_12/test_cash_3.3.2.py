from cash_12.nativeCash import NativeCache as Cache


def test_put_is_key():
    cache = Cache.create(10,
            dict((str(v), v) for v in range(10)))

    assert cache.get('9') == 9
    assert cache.is_key('0') and cache.get('0') == 0
    assert not cache.is_key('10')


def test_put_replace_update():
    cache = Cache.create(10,
            dict((str(v), v) for v in range(10)))

    for v in range(9):
        cache.get(str(v))
    cache.put('100', 'opa')  # replace 9

    assert cache.get('9') is None and not cache.is_key('9')
    cache.put('100', 'newVal')  # update val of 100
    assert cache.get('100') == 'newVal'
    assert cache.is_key('0') and cache.get('0') == 0


def test_hits():
    cache = Cache.create(10,
            dict((str(v), v) for v in range(10)))

    for v in range(1, 10):
        for i in range(v):
            cache.get(str(v))  # increase hits for 1-9

    for v in range(10, 13):
        cache.put(str(v), 'new')  # replace 0-2
        for i in range(v):
            cache.get(str(v))  # increase hits for 10-12

    for v in range(24, 26):
        cache.put(str(v), 'new' + str(v))  # replace 3-4
        for i in range(v):
            cache.get(str(v))  # increase hits for 24-25

    for v in range(1, 5):
        assert cache.get(str(v)) is None and not cache.is_key(str(v))

    cache.get('5'), cache.get('5')  # increase hits for 5
    cache.put('99', 'opa')  # replace 6, hash('6') == hash('99')
    assert cache.get('6') is None and not cache.is_key('6')
    assert cache.get('99') == 'opa'

    for v in range(24, 26):
        assert cache.is_key(str(v)) and cache.get(str(v)) == 'new' + str(v)


def test_large_cache():
    cache = Cache(100)
    for v in range(1000):
        cache.put(str(v), v)
        if v % 10 == 0:
            cache.get(str(v))

    assert cache.get('999') == 999 and cache.is_key('999')
    cache.put('!!!', 'NEW')
    assert cache.get('!!!') == 'NEW'
    assert cache.is_key('!!!')
    assert cache.get('0') == 0


def test_random_strs():
    import random, string

    # random string generator, str length is argument
    rand_str = lambda n: ''.join(
            (random.choice(string.ascii_lowercase)
             for i in range(n)))
    items_num = 10000
    cache = Cache(100)
    strs = tuple(rand_str(v % 10 or 1) for v in range(items_num))
    last_key = strs[-1]

    for v, k in enumerate(strs):
        cache.put(k, v)
        if v != items_num - 1:  # increase hits for all except last
            cache.get(k)

    assert cache.is_key(last_key)
    cache.put('!!!', 'NEW')
    assert cache.get('!!!') == 'NEW'
    assert not cache.is_key(last_key)


def test_only_collis():
    import itertools

    chars = 'qwer'
    collisions = list(''.join(comb) for comb in itertools.permutations(chars))
    items_num = len(collisions)

    cache = Cache(items_num)

    miss_slot = items_num // 2

    for v, k in enumerate(collisions):
        cache.put(k, v)
        if v != miss_slot:  # increase hits for all except one
            cache.get(k)

    miss_key = collisions[miss_slot]
    assert cache.is_key(miss_key)
    cache.put('!!!', 'NEW')
    assert cache.get('!!!') == 'NEW'
    assert not cache.is_key(miss_key)
    for v, k in enumerate(collisions[:miss_slot]):
        assert cache.get(k) == v
    for v, k in enumerate(collisions[miss_slot+1:], miss_slot+1):
        assert cache.get(k) == v


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_put_is_key()
    test_put_replace_update()
    test_hits()
    test_large_cache()
    test_random_strs()
    test_only_collis()

