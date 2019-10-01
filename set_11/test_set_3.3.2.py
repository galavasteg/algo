from itertools import product

from set_11.powerSet import PowerSet


VALS_ARGS = ('', 'лещ', 'dca', 'cda', '0', '-115')
INIT_VALS = ((),) + tuple((v,) for v in VALS_ARGS)
INIT_VALS = (INIT_VALS +
             tuple(VALS_ARGS[:i] + VALS_ARGS[i+1:]
                   for i in range(len(VALS_ARGS))) +
             (VALS_ARGS,))
UNION_PARAMS = dict(
    argnames='vals1, vals2',
    argvalues=tuple(product(INIT_VALS, INIT_VALS)))

# put a lot of numbers
INIT_VALS = INIT_VALS + (tuple(map(str, range(10000))),)

PARAMS = dict(
    argnames='vals, val',
    argvalues=tuple(product(INIT_VALS, VALS_ARGS)))
SETS_PARAMS = dict(
    argnames='vals1, vals2',
    argvalues=tuple(product(INIT_VALS, INIT_VALS)))


# --------------------------- PUT -----------------------------------

def test_put(vals, val):
    print()
    ps = PowerSet.create(vals)
    init_set = set(vals)
    init_length = len(init_set)
    print('init set:', init_length, init_set)
    print('remove "{val}"'.format(val=val))
    if init_length < ps.sz:
        init_set.add(val)  # expected
    exp_size = len(init_set)
    print('expected:', exp_size, init_set)
    ps.put(val)
    res_set = set(ps.get_vals())
    print('result:', ps.size(), res_set)
    assert (res_set == init_set and ps.size() == exp_size)


# --------------------------- REMOVE --------------------------------

def test_remove(vals, val):
    print()
    ps = PowerSet.create(vals)
    init_set = set(vals)
    init_length = len(init_set)
    print('init set:', init_length, init_set)
    print('remove "{val}"'.format(val=val))
    expected = False
    if val in init_set:
        expected = True
        init_set.remove(val)  # expected set
    exp_size = len(init_set)
    print('expected:', exp_size, init_set)
    res = ps.remove(val)
    res_set = set(ps.get_vals())
    print('result:', ps.size(), res_set)
    assert (res == expected and res_set == init_set and
            ps.size() == exp_size)


# --------------------------- INTERSECTION --------------------------

def test_inters(vals1, vals2):
    print()
    ps1, ps2 = PowerSet.create(vals1), PowerSet.create(vals2)
    init_set1, init_set2 = set(vals1), set(vals2)
    print('init sets:', init_set1, init_set2)
    expected = init_set1.intersection(init_set2)
    exp_size = len(expected)
    print('intersection expected', exp_size, expected)
    res = ps1.intersection(ps2)
    res_set = set(res.get_vals())
    assert res_set == expected and res.size() == exp_size


# --------------------------- UNION ---------------------------------

def test_union(vals1, vals2):
    print()
    ps1, ps2 = PowerSet.create(vals1), PowerSet.create(vals2)
    init_set1, init_set2 = set(vals1), set(vals2)
    print('init sets:', init_set1, init_set2)
    expected = init_set1.union(init_set2)
    exp_size = len(expected)
    print('union expected', exp_size, expected)
    res = ps1.union(ps2)
    res_set = set(res.get_vals())
    assert res_set == expected and res.size() == exp_size


# --------------------------- DIFFERENCE ----------------------------

def test_diff(vals1, vals2):
    print()
    ps1, ps2 = PowerSet.create(vals1), PowerSet.create(vals2)
    init_set1, init_set2 = set(vals1), set(vals2)
    print('init sets:', init_set1, init_set2)
    expected = init_set1 - init_set2
    exp_size = len(expected)
    print('diff expected', exp_size, expected)
    res = ps1.difference(ps2)
    res_set = set(res.get_vals())
    assert res_set == expected and res.size() == exp_size


# --------------------------- ISSUBSET ------------------------------

def test_issubset(vals1, vals2):
    print()
    ps1, ps2 = PowerSet.create(vals1), PowerSet.create(vals2)
    init_set1, init_set2 = set(vals1), set(vals2)
    print('init sets:', init_set1, init_set2)
    expected = init_set2.issubset(init_set1)
    print('issubset expected', expected)
    res = ps1.issubset(ps2)
    assert res == expected


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    for vals, val in PARAMS['argvalues']:
        test_remove(vals, val)
        test_put(vals, val)
    for vals1, vals2 in SETS_PARAMS['argvalues']:
        test_inters(vals1, vals2)
        test_diff(vals1, vals2)
        test_issubset(vals1, vals2)
    for vals1, vals2 in UNION_PARAMS['argvalues']:
        test_union(vals1, vals2)

