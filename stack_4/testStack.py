import pytest

from stack_4.stack import Stack


# --------------------------- pytest settings -----------------------

class BaseTest:
    @classmethod
    def setup_class(cls):
        print('============= {} STARTED ================='.format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        print('============= {} FINISHED ================'.format(cls.__name__))

    def teardown_method(self, method):
        print()


# --------------------------- SIZE ----------------------------------

def test_size():
    for vals, res in zip(
            (list('(()()(()'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ),
            (8, 10, )):
        print(vals, res)
        assert Stack.create(vals).size() == res


# --------------------------- PUSH ----------------------------------

def test_push():
    for (vals, adds), res in zip(
            (([1, 2], [3, 4]), ([], []), ([], [0]), ([], [None]),
             (list(range(5)), list(range(5, 0, -1)))),
            ([1, 2, 3, 4], [], [0], [None], [0,1,2,3,4,5,4,3,2,1])):
        stack = Stack.create(vals)
        for a in adds:
            stack.push(a)
        print(vals, '+', adds, res)
        assert stack.to_list() == res


# --------------------------- PEEK ----------------------------------

def test_peek():
    for vals, (cor_res, corr_p) in zip(
            ([1, 2, 3, 4], [], [0], [None, 0, 17]),
            (([1, 2, 3, 4], 4), ([], None), ([0], 0),
             ([None, 0, 17], 17))):
        stack = Stack.create(vals)
        p = stack.peek()
        print(vals, 'peek:', cor_res, corr_p)
        assert stack.to_list() == cor_res and p == corr_p


# --------------------------- POP -----------------------------------

def test_pop():
    for vals, (cor_res, popped) in zip(
            ([1, 2, 3, 4], [], [0], [None, 0, 17]),
            (([1, 2, 3], 4), ([], None), ([], 0),
             ([None, 0], 17))):
        stack = Stack.create(vals)
        p = stack.pop()
        print(vals, 'pop:', cor_res, popped)
        assert stack.to_list() == cor_res and p == popped


# --------------------------- BALANCE -------------------------------

def test_balance():
    for string, res in zip(
            ('(()()(()', '(()((())()))', '())(', '))((', '((())',
             '(hjy()(()', '(()(pdd()))', '(a)(', '))f(d)((', '(()t',
             ')))'),
            (False, True, False, False, False,
             False, True, False, False, False,
             False)):
        print(string, res)
        assert Stack.is_balanced(string) == res


