"""
TODO: EN doc
"""


class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

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
        """Удаление максимально приоритетного узла:

        - ликвидируем корневой узел с индексом 0;
        - выбираем самый последний существующий элемент массива
          (по сути, крайний правый на нижнем уровне);
        - перемещаем его в корень;
        - сдвигаем элемент вниз по дереву (моделируем этот
          процесс движения по дереву с помощью индексов узла в
          массиве): если ниже текущего узла "максимальный" узел
          больше текущего, меняем местами текущий элемент с этим
          максимальным, и продолжаем данное действие;
        - останавливаемся, когда у родителя будет больший ключ,
          а у двух наследников -- меньшие.
        """
        root = -1  # if heap is empty
        if self.HeapArray and self.is_slot_busy(0):
            root = self.HeapArray[0]
            self.__down_sift()

        return root

    def Add(self, key) -> bool:
        """Новый элемент помещаем в самый низ массива,
        в первый свободный слот, и затем поднимаем его вверх по
        дереву, останавливаясь в позиции, когда выше у родителя
        будет больший ключ, а ниже у обоих наследников -- меньшие.
        """
        slot_free = lambda x: x is None
        have_free_slot = any(map(slot_free, self.HeapArray))
        if have_free_slot:
            self.up_sift(key)
        added = have_free_slot
        return added


