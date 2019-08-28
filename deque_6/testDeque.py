from deque_6.deque import Deque


# --------------------------- SIZE ----------------------------------

def test_size():
    pass


# --------------------------- ADD FRONT -----------------------------

def test_add_front():
    pass


# --------------------------- ADD TAIL ------------------------------

def test_add_tail():
    pass  # TODO: Queue.enqueue


# --------------------------- REMOVE FRONT --------------------------

def test_remove_front():
    pass  # TODO: Queue.dequeue


# --------------------------- REMOVE TAIL ---------------------------

def test_remove_tail():
    pass


# --------------------------- IS PALINDROME -------------------------

def test_is_pali():
    for s, res in zip(
            ('((()))', '(((S(((', '((((((', '', '123321', '12321',
             'иди', 'Аргентинаманитнегра', 'sdcsd', '12sDsfds21', '!'),
            (False, True, True, True, True, True,
             True, True, False, False, True)):
        print(f'"{s}"', res)
        assert Deque.is_pali(s) == res


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_size()
    test_add_front()
    test_add_tail()
    test_remove_front()
    test_remove_tail()
    test_is_pali()

