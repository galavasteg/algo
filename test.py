from linkedList import Node, LinkedList


class BaseTest:
    init_vals = ()

    @classmethod
    def setup_class(cls):
        print(f'============= {cls.__name__} STARTED =================')
        inst = cls()
        inst.set_init()
        print('initial state')
        inst.list.print_all_nodes()

    @classmethod
    def teardown_class(cls):
        print(f'============= {cls.__name__} FINISHED ================')

    def setup_method(self, method):
        self.set_init()
        print(method.__name__, 'start')

    def teardown_method(self, method):
        m_name = method.__name__
        print('output:')
        self.list.print_all_nodes()
        print(m_name, 'finish', '\n')

    def set_init(self):
        self.list = LinkedList()
        [self.list.add_in_tail(Node(x)) for x in self.init_vals]


