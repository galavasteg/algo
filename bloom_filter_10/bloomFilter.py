"""
TODO: EN doc
"""


class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.storage = [0] * self.filter_len
        # создаём битовый массив длиной f_len ...

    @staticmethod
    def hash(s: str, sz: int, mult: int) -> int:
        res = ord(s[0]) % sz
        for c in s[1:]:
            res = (res * mult + ord(c)) % sz
        return res

    def hash1(self, str1):
        """организуем цикл до длины строки, результат в этом цикле считаем
        как его версия с предыдущей итерации умноженная на случайное число
        к которой прибавляется код очередного символа,
        и берём результат тут же по модулю длины таблицы."""
        mult = 17
        return self.hash(str1, self.filter_len, mult)

    def hash2(self, str1):
        mult = 223
        return self.hash(str1, self.filter_len, mult)

    def add(self, str1):
        # добавляем строку str1 в фильтр
        h1, h2 = self.hash1(str1), self.hash2(str1)
        self.storage[h1] = self.storage[h2] = 1

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в
        h1, h2 = self.hash1(str1), self.hash2(str1)
        return all((self.storage[h1], self.storage[h2]))

    @classmethod
    def create(cls, sz: int, vals: tuple):
        instance = cls(sz)
        for v in vals:
            instance.add(v)
        return instance

