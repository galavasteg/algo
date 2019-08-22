"""
TODO: 4.4. Напишите тесты, проверяющие работу методов
 insert() и delete():
 -- вставка элемента, когда в итоге размер буфера не превышен
    (проверьте также размер буфера);
 -- вставка элемента, когда в результате превышен размер буфера
    (проверьте также корректное изменение размера буфера);
 -- попытка вставки элемента в недопустимую позицию;
 -- удаление элемента, когда в результате размер буфера остаётся
    прежним (проверьте также размер буфера);
 -- удаление элемента, когда в результате понижается размер буфера
    (проверьте также корректное изменение размера буфера);
 -- попытка удаления элемента в недопустимой позиции.

TODO: В тестах используется схема, когда
 1) увеличение буфера происходит в два раза,
 При этом сохраняем минимальную ёмкость 16 элементов.
 Придерживайтесь этой схемы в своём коде для успешного тестирования.
"""

import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    @classmethod
    def create(cls, values: list):
        array = cls()
        for v in values:
            array.append(v)
        return array

    @property
    def fill_percent(self):
        return self.count/self.capacity * 100

    def to_list(self):
        array, end = [], False
        try:
            for v in self.array:
                array.append(v)
        except ValueError:
            pass
        except IndexError:
            pass
        return array

    @property
    def meta(self):
        return (self.to_list(), self.count,
                self.capacity, self.fill_percent)

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """
        TODO: 3.1. Добавьте метод insert(i, itm), который вставляет
         в i-ю позицию объект itm, сдвигая вперёд все последующие
         элементы. Учтите, что новая длина массива может превысить
         размер буфера. Увеличение буфера выполняем, когда он весь
         полностью заполнен, и выполняется попытка добавления.
        """
        # TODO: Если индекс i лежит вне допустимых
        #  границ, генерируйте исключение.
        # TODO: Кроме:
        #  параметр i может принимать значение, равное длине
        #  рабочего массива count, в таком случае добавление
        #  происходит в его хвост.
        if self.count == i:
            self.append(itm)
        else:
            self[i]  # check IndexError
            count = self.count + 1
            if count > self.capacity:
                self.resize(2 * self.capacity)
            move_forward_indices = list(range(i, self.count))
            for ind in move_forward_indices[::-1]:
                self.array[ind + 1] = self.array[ind]
            self.count = self.count + 1
            self.array[i] = itm

    def delete(self, i):
        """3.2. Delete object in **i**-th position. Reduce capacity
        if the array is less than 50% full after deletion. The logic
        of power reduction is as follows: the result of dividing the
        current power by 1.5 is converted to int (without rounding)"""
        self[i]  # check IndexError
        move_back_indices = list(range(i + 1, self.count))
        for ind in move_back_indices:
            self.array[ind - 1] = self.array[ind]
        self.count = self.count - 1
        capacity = (int(self.capacity / 1.5)
                    if self.capacity > 16 and self.fill_percent < 50 else
                    self.capacity)
        self.resize(capacity if capacity > 16 else 16)

