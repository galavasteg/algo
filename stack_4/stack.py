"""
4.1. Find the appropriate dynamic data structure for
 storing the stack. Realize methods size(), pop(), push()
 and peek(). Write tests for all of them. Rate the
 complexity of pop() and push() methods.
4.2. Rebuild the stack implementation so that the top
 of the stack is the head and not the tail of the list.
4.3. Without starting the program, answer, how will this
code work?
            # while stack.size() > 0:
            #     print(stack.pop())
            #     print(stack.pop())
4.4. Rate the complexity of pop() and push() methods.
TODO: 4.5. Напишите функцию, которая получает на вход строку,
 состоящую из открывающих и закрывающих скобок (например, "(()((())()))"
 или "(()()(()") и, используя только стек и оператор цикла, определите,
 сбалансированы ли скобки в этой строке. Сбалансированной считается
 последовательность, в которой каждой открывающей обязательно
 соответствует закрывающая, а каждой закрывающей -- открывающая скобки,
 то есть последовательности "())(" , "))((" или "((())" будут
 несбалансированы.

TODO: 4.5. Постфиксная запись выражения -- это запись, в которой порядок
 вычислений определяется не скобками и приоритетами, а только позицией
 элемента в выражении. Например, в выражениях разрешено использовать
 целые числа и операции + и * . Тогда выражение
 (1 + 2) * 3    запишется как    1 2 + 3 * (верхушка стека слева)
 Такой стек обрабатывается следующим образом: берём с верхушки объект,
 если это число, сохраняем во втором стеке, а если операция, выполняем
 её над двумя верхними элементами второго стека и возвращаем её обратно
 во второй стек.
 В нашем случае:
 S1: 1 2 + 3 *    S2:
 S1: 2 + 3 *      S2: 1
 S1: + 3 *        S2: 2 1
 Берём операцию + и применяем её к содержимому S2:
 S1: 3 *          S2: 3
 S1: *            S2: 3 3
 S1:              S2: 9
 Можно ещё добавить операцию = , которая выдаёт содержимое второго стека
 как результат. Напишите функцию, которая с помощью двух стеков реализует
 вычисление подобных постфиксных выражений.
 Рассчитайте с её помощью например такое выражение:
 8 2 + 5 * 9 + =
"""


class Stack:
    def __init__(self):
        self.stack = []  # 4.1.

    def size(self):
        return len(self.stack)

    # 4.4. O(n)
    def pop(self):
        if self.stack:
            # 4.2.
            return self.stack.pop(0)
            # # 4.1. O(1)
            # return self.stack.pop(-1)

    # 4.4. O(n)
    def push(self, value):
        # 4.2.
        self.stack.insert(0, value)
        # # 4.1. O(1)
        # self.stack.insert(self.size(), value)

    def peek(self):
        if self.stack:
            # 4.2.
            return self.stack[0]
            # # 4.1.
            # return self.stack[-1]

    def to_list(self):
        # 4.2.
        return self.stack[::-1]
        # # 4.1.
        # return self.stack

    @classmethod
    def create(cls, vals: list):
        stack = cls()
        for v in vals:
            stack.push(v)
        return stack

    @classmethod
    def is_balanced(cls, string: str) -> bool:
        opened_s = cls()
        for ch in string:
            if ch == '(':
                opened_s.push(ch)
            elif ch == ')':
                if not opened_s.pop():
                    return False
        return not opened_s.peek()

    @classmethod
    def postfix_calc(cls, string: str) -> int:
        opers_mapping = dict(zip(('+', '*'), ('__add__', '__mul__', )))
        digits_s = cls()
        for ch in string.split(' '):
            if ch.isdigit():
                digits_s.push(int(ch))
            elif ch == '=':
                return digits_s.peek()
            else:
                a, b = digits_s.pop(), digits_s.pop()
                c = a.__getattribute__(opers_mapping[ch])(b)
                digits_s.push(c)

