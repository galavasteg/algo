"""
1.7: Write tests for all previous tasks 1.1.-1.6.
 Pay attention to the correct field values:
 **head, tail** after all operations.
  - what if list is empty;
  - what if list has many elements;
  - what if list has only one element;
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list:
        """1.4.: Find all nodes by **val**
        (return a list of found nodes)."""
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        """1.1.: Delete only 1-st node with **val**
        1.2.: Delete **all** nodes with **val**"""
        nodes = self.find_all(val)
        for del_n in (nodes[::-1] if all else nodes[:1]):
            if del_n is self.head and del_n.next is None:
                self.clean()
            elif del_n is self.head:
                self.head = del_n.next
            else:
                prev_node = self.head
                while prev_node.next is not del_n:
                    prev_node = prev_node.next
                prev_node.next = del_n.next
                if prev_node.next is None:
                    self.tail = prev_node

            del_n.next = None

    def clean(self):
        """1.3.: delete all nodes in list (init. new list)"""
        self.__init__()

    def len(self) -> int:
        """1.5.: Compute list length"""
        _len = 0
        node = self.head
        while node:
            node = node.next
            _len += 1
        return _len

    def insert(self, afterNode, newNode: Node):
        """1.6.: Insert **newNode** after **afterNode**.
        If **afterNode** is None and list is empty add
        **newNode** in head."""
        if afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

    def to_list(self) -> list:
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    @classmethod
    def create_list(cls, vals: list):
        list_ = cls()
        for x in vals:
            list_.add_in_tail(Node(x))
        return list_

    @staticmethod
    def get_nodes_vals(nodes: list) -> list:
        nodes_vals = []
        for n in nodes:
            n_vals = []
            node_ = n
            while node_ is not None:
                n_vals.append(node_.value)
                node_ = node_.next
            nodes_vals.append(n_vals)
        return nodes_vals

    @classmethod
    def merge_lists(cls, list1, list2):
        """1.8: return LinkedList of  Sums corresponding
        elements of two LinkedLists, which consist of integers."""
        if list1.len() == list2.len():
            new_list = cls()
            n1, n2 = list1.head, list2.head
            while all((n1, n2)):
                new_list.add_in_tail(Node(n1.value + n2.value))
                n1, n2 = n1.next, n2.next
            return new_list

