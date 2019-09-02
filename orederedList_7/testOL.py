from itertools import product

from orederedList_7.orderedList import OrderedList, OrderedStringList


def get_correct_nodes_vals(init_vals: list, val) -> tuple:
    return (get_node_vals_view(init_vals, init_vals.index(val))
            if val in init_vals else None)


def get_node_vals_view(l_vals: list, ind: int):
    prev_vals = l_vals[:ind]
    next_vals = l_vals[ind+1:]
    return prev_vals, l_vals[ind], next_vals


VALS_ARGS = (-9, -4, -1, 0, 1, 4, 9)
INIT_VALS = [[]] + [[v] for v in VALS_ARGS]
INIT_VALS = tuple(INIT_VALS + [list(VALS_ARGS[:i] + VALS_ARGS[i+1:])
                               for i in range(len(VALS_ARGS))])
ASC_ARGS = (True, False)


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




# --------------------------- FIND ----------------------------------

def test_find():
    pass


# --------------------------- DELETE --------------------------------

def test_delete():
    pass


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_add()
    test_find()
    # test_len()
    # test_get_all()
    # test_clean()
    test_compare()
    test_delete()

