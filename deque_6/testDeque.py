from deque_6.deque import Deque


# --------------------------- SIZE ----------------------------------

def test_size():
    for vals in (list('(()()(()'), [0, 1, 2, 3, 4, 5, 6], []):
        print(vals, len(vals))
        assert Deque.create(vals).size() == len(vals)


# --------------------------- ADD FRONT -----------------------------

def test_add_front():
    for (vals, add), cor_res in zip(
            (([1, 2, 3], 0), ([], None), ([], 0), ([None, 0], 17)),
            ([0, 1, 2, 3], [None], [0], [17, None, 0]),):
        d = Deque.create(vals)
        d.addFront(add)
        print(vals, add, 'add tail:', cor_res)
        assert d.to_list() == cor_res and d.size() == len(vals) + 1


# --------------------------- ADD TAIL ------------------------------

def test_add_tail():
    for (vals, add), cor_res in zip(
            (([1, 2, 3], 4), ([], None), ([], 0), ([None, 0], 17)),
            ([1, 2, 3, 4], [None], [0], [None, 0, 17]),):
        d = Deque.create(vals)
        d.addTail(add)
        print(vals, add, 'add tail:', cor_res)
        assert d.to_list() == cor_res and d.size() == len(vals) + 1


# --------------------------- REMOVE FRONT --------------------------

def test_remove_front():
    for vals, (cor_res, popped) in zip(
            ([1, 2, 3, 4], [], [0], [None, 0, 17]),
            (([2, 3, 4], 1), ([], None), ([], 0), ([0, 17], None)),):
        deque = Deque.create(vals)
        p = deque.removeFront()
        print(vals, 'rm front:', popped, cor_res)
        assert deque.to_list() == cor_res and p == popped


# --------------------------- REMOVE TAIL ---------------------------

def test_remove_tail():
    for vals, (cor_res, popped) in zip(
            ([1, 2, 3, 4], [], [0], [None, 0, 17]),
            (([1, 2, 3], 4), ([], None), ([], 0), ([None, 0], 17)),):
        deque = Deque.create(vals)
        p = deque.removeTail()
        print(vals, 'rm tail:', cor_res, popped)
        assert deque.to_list() == cor_res and p == popped


# --------------------------- IS PALINDROME -------------------------

def test_is_pali():
    for s, res in zip(
            ('((()))', '(((S(((', '((((((', '', '123321', '12321',
             'иди', 'Аргентинаманитнегра', 'sdcsd', '12sDsfds21', '!'),
            (False, True, True, True, True, True,
             True, True, False, False, True),):
        print('"%s"' % s, res)
        assert Deque.is_pali(s) == res


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_size()
    test_add_front()
    test_add_tail()
    test_remove_front()
    test_remove_tail()
    test_is_pali()

