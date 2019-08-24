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
4.5. TODO: in EN
4.6. TODO: in EN
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
        opened_s, bad_close = cls(), 0
        for ch in string:
            if ch == '(':
                opened_s.push(ch)
            elif ch == ')':
                if not opened_s.pop():
                    bad_close = bad_close + 1
        return not any([opened_s.peek(), bad_close])


