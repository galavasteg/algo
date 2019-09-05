from hash_tables_8.hashTable import HashTable


SIZES_ARGS = (1, 3, 11, 17)
STEPS_ARGS = (2,) + SIZES_ARGS
VALS_ARGS = ('', 'лещ', 'лещи', 'лщеи', 'dca', 'dac')
INIT_VALS = (tuple(),) + tuple((v,) for v in VALS_ARGS)
INIT_VALS = tuple(INIT_VALS + tuple(VALS_ARGS[:i] + VALS_ARGS[i+1:]
                                    for i in range(len(VALS_ARGS))))


# --------------------------- HASH ----------------------------------

def test_hash():
    for sz, value in zip(SIZES_ARGS, VALS_ARGS):
        ht = HashTable(sz, 1)
        assert ht.hash_fun(value) == HashTable.hash(value, sz)


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    test_hash()

