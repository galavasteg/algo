"""
TODO: В классе хэш-таблицы потребуются два параметра: размер хэш-таблицы
 (желательно простое число, для экспериментов можно например брать
 17 или 19), и длину шага (количество слотов) для поиска следующего
 свободного слота (например, 3).
 В этом классе требуется реализовать четыре метода:
  - хэш-функцию hash_fun(value), которая по входному значению вычисляет
    индекс слота;
  - функцию поиска слота seek_slot(value), которая по входному значению
    сперва рассчитывает индекс хэш-функцией, а затем отыскивает подходящий
    слот для него с учётом коллизий, или возвращает None, если это не
    удалось;
  - put(value), который помещает значение value в слот, вычисляемый с
    помощью функции поиска;
  - find(value), который проверяет, имеется ли в слотах указанное
    значение, и возвращает либо слот, либо None.
 Напишите тесты, которые проверяют работу этих четырёх методов.
"""


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    @staticmethod
    def hash(s: str, sz: int):
        return sum(s.encode()) % sz

    def hash_fun(self, value):
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        return self.hash(value, self.size)

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        hash_i = i = self.hash_fun(value)
        if self.slots[i] is not None:
            i = (hash_i + self.step) % self.size
            while (self.slots[i] is not None and hash_i != i):
                print(hash_i, i)
                i = (i + self.step) % self.size
        if self.slots[i] is None:
            return i

    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        i = self.seek_slot(value)
        if i is not None:
            self.slots[i] = value
        return i

    def find(self, value):
        # находит индекс слота со значением, или None
        if value in self.slots:
            return self.slots.index(value)

    @classmethod
    def create(cls, sz: int, stp: int, vals: tuple):
        ht = cls(sz, stp)
        for v in vals:
            ht.put(v)
        return ht

