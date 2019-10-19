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


# inherit this class from HashTable or extend it with it's methods
class PowerSet:
    def __init__(self):
        """Your storage realization..."""
        self.sz = 20000
        self.__slots = tuple([] for _ in range(self.sz))
        self.__count = 0

    def hash_fun(self, value):
        """Always return correct slot index.
        **key** is always string"""
        bStr = value.encode()
        return int('0' + ''.join(str(b) for b in bStr)) % self.sz
        # # faster but much more collisions
        # return sum(value.encode()) % self.sz

    def size(self):
        """Count of the set's elements"""
        return self.__count

    def get(self, value):
        """Check if the **value** is in the set"""
        hash_i = self.hash_fun(value)
        return value in self.__slots[hash_i]

    def put(self, value):
        """Put **value** into the set if it is not full"""
        if self.__count < self.sz:
            hash_i = self.hash_fun(value)
            collisions = self.__slots[hash_i]
            if not collisions or value not in collisions:
                self.__slots[hash_i].append(value)
                self.__count += 1

    def remove(self, value):
        """Delete set's **value**. Return True if
        **value** has been deleted, False otherwise"""
        isRemoved = False
        hash_i = self.hash_fun(value)
        collisions = self.__slots[hash_i]
        if collisions and value in collisions:
            self.__slots[hash_i].remove(value)
            self.__count -= 1
            isRemoved = True
        return isRemoved

    def intersection(self, set2):
        """Return the intersection with **set2** as a new set.
        (i.e. all elements that are in both sets.)"""
        vals1, vals2 = self.get_vals(), set2.get_vals()
        intersection_vals = tuple(v1 for v1 in vals1
                                  if v1 in vals2)
        return self.create(intersection_vals)

    def union(self, set2):
        """Return the union of this and **set2** sets as
        a new set. (i.e. all elements that are in either set.)"""
        union_vals = self.get_vals() + set2.get_vals()
        return self.create(union_vals)

    def difference(self, set2):
        """Return the difference of this and **set2**
        sets as a new set. (i.e. all elements that are in
        this set but not the **set2**.)"""
        vals1, vals2 = self.get_vals(), set2.get_vals()
        diff_vals = tuple(v1 for v1 in vals1
                          if v1 not in vals2)
        return self.create(diff_vals)

    def issubset(self, set2):
        """Report whether **set2** contains this set"""
        vals2 = set2.get_vals()
        if vals2:
            intersection_vals = self.intersection(set2).get_vals()
            vals2 = set2.get_vals()
            equal_vals = tuple(v2 in intersection_vals for v2 in vals2)
        else:
            equal_vals = ()
        return all(equal_vals)

    def get_vals(self):
        return sum((collis for collis in self.__slots if collis), [])

    @classmethod
    def create(cls, vals):
        p_set = cls()
        for v in vals:
            p_set.put(v)
        return p_set

