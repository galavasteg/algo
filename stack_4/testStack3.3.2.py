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


