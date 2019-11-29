"""
TODO: EN doc
"""


class Heap:

    def __init__(self):
        self.HeapArray = []  # stores positive int-keys

    @staticmethod
    def _get_btree_size(depth: int):
        return 2 ** (depth + 1) - 1

    @staticmethod
    def _get_parent_i(child_i: int) -> int:
        return (child_i - 1) // 2

    @staticmethod
    def _get_left_child_i(parent_i: int) -> int:
        return 2 * parent_i + 1

    @staticmethod
    def _get_right_child_i(parent_i: int) -> int:
        return 2 * parent_i + 2

    def _array_init(self, depth: int):
        tree_size = self._get_btree_size(depth)  # slots count
        self.HeapArray = [None] * tree_size  # keys array

    def MakeHeap(self, a: list, depth: int):
        assert depth >= 0
        self._array_init(depth)
        add_success_flags = tuple(map(self.Add, a))

    def _parent_more_children(self, parent_i: int,
                              *children_inds: int) -> bool:
        # TODO: semantic refactoring
        parent_more_children = True

        if parent_i >= 0 and children_inds:
            p_key = self.HeapArray[parent_i]
            heap_size = len(self.HeapArray)

            def parent_more_then_child(c_i: int) -> bool:
                c_key = self.HeapArray[c_i] if c_i <= heap_size else None
                return c_key is None or p_key > c_key

            parent_more_children = all(map(parent_more_then_child,
                                           children_inds))

        return parent_more_children

    def is_slot_busy(self, i: int) -> bool:
        return self.HeapArray[i] is not None

    def _get_last_busy_slot(self):
        i = next(filter(self.is_slot_busy,
                        reversed(range(len(self.HeapArray)))))
        return i

    def __down_sift(self):
        last_busy_i = self._get_last_busy_slot()
        parent_i = 0
        self.HeapArray[parent_i], self.HeapArray[last_busy_i] = (
            self.HeapArray[last_busy_i], None)

        c1_i = self._get_left_child_i(parent_i)
        c2_i = self._get_right_child_i(parent_i)

        while not self._parent_more_children(parent_i,
                                             c1_i, c2_i):
            max_child = max(self.HeapArray[i] for i
                            in filter(self.is_slot_busy, (c1_i, c2_i)))
            is_max_child = lambda i: self.HeapArray[i] == max_child
            max_c_i = next(filter(is_max_child, (c1_i, c2_i)))

            self.HeapArray[parent_i], self.HeapArray[max_c_i] = (
                self.HeapArray[max_c_i], self.HeapArray[parent_i])
            parent_i = max_c_i
            c1_i = self._get_left_child_i(parent_i)
            c2_i = self._get_right_child_i(parent_i)

    def GetMax(self):
        """TODO: EN doc
        """
        root = -1  # if heap is empty
        if self.HeapArray and self.is_slot_busy(0):
            root = self.HeapArray[0]
            self.__down_sift()

        return root

    @staticmethod
    def _get_depth(tree_size: int) -> int:
        def logarithm(x_: int, base=2):
            count = -1
            while x_ != 0:
                x_ = x_ // base
                count = count + 1
            return count

        x = tree_size + 1
        log = logarithm(x)
        depth = int(log) - 1
        return depth

    def _get_level_slots(self, level: int) -> tuple:
        level_size = self._get_btree_size(level)
        slots = tuple(range(level_size))
        if level > 0:
            prev_level_size = self._get_btree_size(level - 1)
            prev_slots = tuple(range(prev_level_size))
            slots = tuple(sorted(
                set(slots).difference(set(prev_slots))
            ))

        return slots

    def _get_bottom_level_slots(self) -> tuple:
        depth = self._get_depth(len(self.HeapArray))
        level = depth
        slots = self._get_level_slots(level)
        while level > 0 and not any(map(self.is_slot_busy, slots)):
            level -= 1
            slots = self._get_level_slots(level)
        return slots

    def is_slot_free(self, i: int) -> bool:
        return self.HeapArray[i] is None

    def _get_bottom_left_free_slot(self) -> int:
        bottom_level_slots = self._get_bottom_level_slots()
        free_slots = tuple(filter(self.is_slot_free,
                                  bottom_level_slots))
        if free_slots:
            bottom_left_free_i = free_slots[0]
        else:
            parent_i = bottom_level_slots[0]
            bottom_left_free_i = self._get_left_child_i(parent_i)

        return bottom_left_free_i

    def __up_sift(self, key):
        bottom_left_free_i = self._get_bottom_left_free_slot()
        self.HeapArray[bottom_left_free_i] = key

        c_i = bottom_left_free_i
        parent_i = self._get_parent_i(c_i)
        while not self._parent_more_children(parent_i, c_i):
            self.HeapArray[parent_i], self.HeapArray[c_i] = (
                self.HeapArray[c_i], self.HeapArray[parent_i])
            c_i = parent_i
            parent_i = self._get_parent_i(c_i)

    def Add(self, key) -> bool:
        """TODO: EN doc
        """
        have_free_slot = any(map(self.is_slot_free,
                                 reversed(range(len(self.HeapArray)))))
        if have_free_slot:
            self.__up_sift(key)

        added = have_free_slot
        return added

