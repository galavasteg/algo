from dynamic_list_3.dynArray import DynArray


d = dict((i, v)for i, v in enumerate([1, None, [], 'test']))


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


# --------------------------- DELETE --------------------------------

DELETE_PARAMS = dict(
    argnames='init_vals, del_indices',
    argvalues=[
        ([2], [0]), ([1, 2, 2, 3, 2, 5], [0]),
        ([None, d, None], [0]), ([0, 0, d], [0]),
        ([None, 1, 4, 5, 1], [1]), ([0, 1, 2, 3, 4], [1, 3]),
        ([5, d, 0, 3, 2], [1]), ([2, 1, 3, 2, 2], [3]),
        ([0, 1, 4, 3, 2], [2]), ([0, 1, 4, 3, 2], [4]),
        (list(range(17)), [16, 0]), ([0, 1, 4, 3, 0], [4]),
        (list(range(35)), list(range(15))),
        (list(range(32)), list(range(16, 0, -1))),
    ])
DELETE_NEGATIVE_PARAMS = dict(
    argnames='init_vals, del_indices',
    argvalues=[
        ([], [0]), ([], [-6]), ([], [1]), ([], [6]),
        (list(range(33)), [33]), ([2, 1, 3, 2, 2], [6]),
        ([None, None, None], [-1]), ([2, 1, 3, 2, 2], [5]),
        ([2, 2, 2, 2], [-10]), ([0, 0, ''], [15]),
        ([2, 2, 2, 2, 5], [0, 4]),
        (list(range(32)), list(range(17))),
    ])


class TestDelete(BaseTest):
    @staticmethod
    def get_correct_delete_res(da: DynArray, del_indices: list):
        array, count, capacity, fill_percent = da.meta
        for del_ind in del_indices:
            try:
                ind = del_ind if del_ind >= 0 else count + - del_ind
                array.pop(ind)
            except IndexError:
                break
            count = len(array)
            fill_percent = count / capacity * 100
            if capacity > 16 and fill_percent < 50:
                capacity = int(capacity / 1.5)
                fill_percent = count / capacity * 100
        return array, count, capacity, fill_percent

    def test_delete_negative(self, init_vals: list, del_indices: list):
        da = DynArray.create(init_vals)
        expected = self.get_correct_delete_res(da, del_indices)
        print('init state:', da.meta)
        print('delete items in indices:', del_indices)
        print('expected: IndexError("Index is out of bounds"),', expected)
        e_type, e_val = None, ''
        try:
            for del_ind in del_indices:
                da.delete(del_ind)
        except IndexError as e:
            e_val = str(e)
            e_type = 'IndexError'
        print('result: {et}("{ev}"),'.format(et=e_type, ev=e_val), da.meta)
        assert (e_val == 'Index is out of bounds' and
                da.meta == expected)

    def test_delete(self, init_vals: list, del_indices: list):
        da = DynArray.create(init_vals)
        expected = self.get_correct_delete_res(da, del_indices)
        print('init state:', da.meta)
        print('delete items in indices', del_indices)
        print('expected:', expected)
        for del_ind in del_indices:
            da.delete(del_ind)
        result = da.meta
        print('result:', result)
        assert result == expected


# --------------------------- INSERT --------------------------------

INSERT_PARAMS = dict(
    argnames='init_vals, ins_indices, ins_vals',
    argvalues=[
        ([], [0], [d]), ([], [0], [0]), ([], [0], [None]),
        ([2], [1], [0]), ([2], [0, 2], [d, 0]),
        (list(range(1, 16)), [0, 16], [0, 16]),
        (list(range(10)), [10, 11], [None, 0]),
        (list(range(15)), [5] * 5, ['!'] * 5),
        (list(range(16)), list(range(16, 50)), [None] * 34),
        (list(range(64)), list(range(64, 0, -1)), ['W'] * 64),
        (list(range(100)), list(range(100, 150)), [1] * 50),
    ])
INSERT_NEGATIVE_PARAMS = dict(
    argnames='init_vals, ins_indices, ins_vals',
    argvalues=[
        ([], [1], [15]), ([], [-1], [4]), ([], [1], [None]),
        ([], [-1], ['']), ([2], [-2], [None]), ([d], [15], [d]),
        (list(range(1, 16)), [0, 17], [0, 16]),
        (list(range(60)), [55] * 5 + [67], [None] * 5 + [70]),
    ])


class TestInsert(BaseTest):
    @staticmethod
    def get_correct_insert_res(da: DynArray, ins_indices: list,
                               ins_vals: list):
        array, count, capacity, fill_percent = da.meta
        for ins_ind, ins_val in zip(ins_indices, ins_vals):
            ind = ins_ind if ins_ind >= 0 else count + - ins_ind
            if count >= ind:
                array.insert(ind, ins_val)
            count = len(array)
            if count > capacity:
                capacity = 2 * capacity
            fill_percent = count / capacity * 100
        return array, count, capacity, fill_percent

    def test_insert_negative(self, init_vals: list, ins_indices: list,
                             ins_vals: list):
        da = DynArray.create(init_vals)
        expected = self.get_correct_insert_res(da, ins_indices, ins_vals)
        print('init state:', da.meta)
        print('insert', ins_vals, 'in indices', ins_indices)
        print('expected: IndexError("Index is out of bounds"),', expected)
        e_type, e_val = None, ''
        try:
            for ins_ind, ins_val in zip(ins_indices, ins_vals):
                da.insert(ins_ind, ins_val)
        except IndexError as e:
            e_val = str(e)
            e_type = 'IndexError'
        print('result: {et}("{ev}"),'.format(et=e_type, ev=e_val), da.meta)
        assert (e_val == 'Index is out of bounds' and
                da.meta == expected)

    def test_insert(self, init_vals: list, ins_indices: list,
                    ins_vals: list):
        da = DynArray.create(init_vals)
        expected = self.get_correct_insert_res(da, ins_indices, ins_vals)
        print('init state:', da.meta)
        print('insert', ins_vals, 'in indices', ins_indices)
        print('expected:', expected)
        for ins_ind, ins_val in zip(ins_indices, ins_vals):
            da.insert(ins_ind, ins_val)
        result = da.meta
        print('result:', result)
        assert result == expected


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':

    test = TestDelete()
    for init_vals, del_ind in DELETE_PARAMS['argvalues']:
        test.test_delete(init_vals, del_ind)
    for init_vals, del_ind in DELETE_NEGATIVE_PARAMS['argvalues']:
        test.test_delete_negative(init_vals, del_ind)

    test = TestInsert()
    for init_vals, ins_ind, ins_val in INSERT_PARAMS['argvalues']:
        test.test_insert(init_vals, ins_ind, ins_val)
    for init_vals, ins_ind, ins_val in INSERT_NEGATIVE_PARAMS['argvalues']:
        test.test_insert_negative(init_vals, ins_ind, ins_val)

