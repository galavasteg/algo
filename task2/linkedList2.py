"""
2.9.: Write tests for all previous tasks 2.1.-2.8.
Pay attention to the correct field values:
**head, prev, next, tail** after all operations.
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def next_vals(self):
        values = []
        node = self.next
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    def prev_vals(self):
        values = []
        node = self.prev
        while node is not None:
            values.append(node.value)
            node = node.prev
        values.reverse()
        return values


class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    @classmethod
    def create(cls, values):
        list_ = cls()
        [list_.add_in_tail(Node(v)) for v in values]
        return list_

    @property
    def vals(self) -> list:
        values = []
        if self.head is not None:
            values = [self.head.value]
            [values.append(v) for v in self.head.next_vals()]
        return values

    @property
    def nodes(self) -> list:
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node)
            node = node.next
        return nodes

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        """2.1.: Find 1-st node by **val*."""
        node = self.head
        while node is not None:
            if node.value == val:
                break
            node = node.next
        return node

    def find_all(self, val) -> list:
        """2.2.: Find all nodes by **val**
        (return a list of found nodes)."""
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        """2.3.: Delete only 1-st node with **val**.\n
        2.4.: Delete **all** nodes with **val**"""
        nodes = self.find_all(val)
        for del_n in (nodes[::-1] if all else nodes[:1]):
            if del_n is self.head and del_n.next is None:
                self.clean()
            elif del_n is self.tail:
                self.tail = del_n.prev
                del_n.prev.next = None
            elif del_n is self.head:
                self.head = del_n.next
                del_n.next.prev = None
            else:
                del_n.prev.next = del_n.next
                del_n.next.prev = del_n.prev
            # TODO: delete links or not delete?
            # del_n.prev = None
            # del_n.next = None

    def clean(self):
        """2.7.: delete all nodes in list (init. new list)"""
        self.__init__()

    def len(self) -> int:
        """2.8.: Compute list length"""
        return len(self.vals)

    def insert(self, afterNode, newNode: Node):
        """2.5.: Insert **newNode** after **afterNode**.\n
        If **afterNode** is None and list is empty add
        **newNode** in head. If **afterNode** and list
        not empty add **newNode** in tail."""
        if afterNode is self.tail or afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            afterNode.next.prev = newNode
            newNode.next = afterNode.next
            afterNode.next = newNode

    def add_in_head(self, newNode: Node):
        """2.6.: Insert **newNode** in head."""
        if self.head is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

