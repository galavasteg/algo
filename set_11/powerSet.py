"""
TODO: На основе класса HashTable создайте реализующий множество
 класс PowerSet, который
 11.1. не должен допускать добавление уже существующего в множестве
 значения -- надо изменить оригинальный метод put().
 11.2. дополнительно реализуем следующие типичные для множества методы:
 - remove(значение) -- удаление элемента из множества;
 - intersection(), в качестве параметра выступает другое множество, а
   возвращается пересечение этих множеств (множество, в котором есть
   только те элементы, которые имеются в каждом из множеств);
 - union(), в качестве параметра выступает другое множество, а
   возвращается объединение этих множеств (множество, в котором есть
   все элементы из каждого множества);
 - difference(), в качестве параметра выступает другое множество, а
   возвращается подмножество текущего множества из таких элементов,
   которые не входят в множество-параметр;
 - issubset(), в качестве параметра выступает другое множество, и
   проверяется, входят ли все его элементы в текущее множество (будет
   ли множество-параметр подмножеством текущего множества).
 11.3. Добавьте тесты, которые проверяют:
 - возможность добавления отсутствующего элемента и невозможность
   добавления присутствующего в множестве элемента с помощью put();
 - удаление элемента с помощью remove();
 - пересечение множеств intersection(), чтобы в результате получались
   как пустое, так и непустое множества;
 - объединение union(), когда оба параметра непустые, и когда один из
   параметров -- пустое множество;
 - разница difference(), чтобы в результате получались как пустое, так
   и непустое множества;
 - подмножество issubset() -- рассмотрите три случая (все элементы
   параметра входят в текущее множество, все элементы текущего
   множества входят в параметр, не все элементы параметра входят в
   текущее множество).
 В реализации используйте вариант с фиксированным размером хэш-таблицы
   на 20,000 значений.
"""


# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:
    def __init__(self):
        # ваша реализация хранилища
        self.sz = 20000
        self.slots = [None] * self.sz

    def hash_fun(self, value):
        # TODO: doc
        return sum(value.encode()) % self.sz

    def size(self):
        # TODO: количество элементов в множестве
        return len(self.get_vals())

    def get(self, value):
        # TODO: возвращает True если value имеется в множестве, иначе False
        i = self.hash_fun(value)
        return self.slots[i] is not None

    def put(self, value):
        # всегда срабатывает
        pass

    def remove(self, value):
        # TODO: возвращает True если value удалено, иначе False
        i = self.hash_fun(value)
        is_rm = False
        if self.slots[i] is not None:
            self.slots[i] = None
            is_rm = True
        return is_rm

    def intersection(self, set2):
        # TODO: пересечение текущего множества и set2
        intersection_vals = tuple(v1 for v1, v2 in
                                  zip(self.slots, set2.slots)
                                  if v1 is not None and v1 == v2)
        return self.create(intersection_vals)

    def union(self, set2):
        # TODO: объединение текущего множества и set2
        union_vals = self.get_vals() + set2.get_vals()
        return self.create(union_vals)

    def difference(self, set2):
        # TODO: разница текущего множества и set2
        # TODO: test another approach
        diff_vals = tuple(v1 for v1, v2
                          in zip(self.slots, set2.slots)
                          if v1 is not None and v1 != v2)
        return self.create(diff_vals)

    def issubset(self, set2):
        # TODO: возвращает True, если set2 есть подмножество
        #  текущего множества, иначе False
        equal_vals = tuple(self.slots[i] == v2 for i, v2 in
                           enumerate(set2.slots)
                           if v2 is not None)
        return all(equal_vals)

    def get_vals(self):
        return tuple(filter(lambda x: x is not None, self.slots))

    @classmethod
    def create(cls, vals):
        p_set = cls()
        for v in vals:
            p_set.put(v)
        return p_set

