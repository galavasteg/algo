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
    def _get_parent_i(node_i: int) -> int:
        return (node_i - 1) // 2

    @staticmethod
    def _get_left_child_i(parent_i: int) -> int:
        return 2 * parent_i + 1

    @staticmethod
    def _get_right_child_i(parent_i: int) -> int:
        return 2 * parent_i + 2

    def MakeHeap(self, a: list, depth: int):
        assert depth >= 0
        tree_size = self._get_btree_size(depth)  # slots count
        self.HeapArray = [None] * tree_size  # keys array
        add_success_flags = tuple(map(self.Add, a))

    def _get_last_existing(self):
        i = len(self.HeapArray)
        key = self.HeapArray[i]
        while i >= 0 and key is not None:
            i -= 1
            key = self.HeapArray[i]

        return key

    def _down_sift(self):
        parent = self._get_last_existing()
        parent_i = 0
        self.HeapArray[parent_i] = parent
        while

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
        if self.HeapArray and self.HeapArray[0] is not None:
            root = self.HeapArray[0]
            self._down_sift()

        return root

    def Add(self, key) -> bool:
        """Новый элемент помещаем в самый низ массива,
        в первый свободный слот, и затем поднимаем его вверх по
        дереву, останавливаясь в позиции, когда выше у родителя
        будет больший ключ, а ниже у обоих наследников -- меньшие.
        """
        # добавляем новый элемент key в кучу и перестраиваем её
        return False  # если куча вся заполнена


