"""
7.6. Write tests on add, delete and find functions
 taking into **asc** attribute.
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def _next_vals(self):
        values = []
        node = self.next
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    def _prev_vals(self):
        values = []
        node = self.prev
        while node is not None:
            values.append(node.value)
            node = node.prev
        values.reverse()
        return values


class OrderedList:
    def __init__(self, asc):
        """7.1. Implement an additional private attribute
        in the class constructor - **__ascending**: elements
        should be stored in an array ascending (True) or
        descending (False). This attribute can be changed by
        **clean** method"""
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        """7.2. Compare two values: **v1** < **v2** -> -1;
        **v1** == **v2** -> 0; **v1** > **v2** -> 1"""
        return (-1 if v1 < v2 else
                0 if v1 == v2 else
                1)  # v2 > v2

    def add(self, value):
        """7.3. Automatically paste new Node with **value** into
        an array taking into __ascending private attribute (use
        compare method for it)"""
        newNode = Node(value)
        nodes = self.get_all()
        if not nodes:
            self.head = newNode
            self.tail = newNode
        else:
            # search afterNode element
            stop_search = 1 if self.__ascending else -1
            for next_n in nodes:
                comp_res = self.compare(next_n.value, value)
                if comp_res == stop_search:
                    afterNode = next_n.prev
                    break
                else:
                    afterNode = next_n
            # insert logic
            if afterNode is None:  # prev of head
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif afterNode is self.tail:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                newNode.prev = afterNode
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
                afterNode.next = newNode

    # O(n), the same as in LinkedList and LinkedList2
    def find(self, val):
        """7.5. Find 1-st node by **val** taking into account
        **__ascending** private attribute and the possibility
        of early termination of the search. Rate the complexity
        of this method."""
        node = self.head
        while node != None:
            if self.compare(node.value, val) == 0:
                break
            node = node.next
        return node

    def delete(self, val):
        """Delete 1-st node with **val**"""
        del_n = self.find(val)
        if del_n is not None and del_n.value == val:
            if del_n is self.head and del_n.next is None:
                self.clean(self.__ascending)
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
            del_n.prev = None
            del_n.next = None

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        return len(self.get_all())

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    @classmethod
    def create(cls, vals: list, asc: bool):
        list_ = cls(asc)
        for v in vals:
            list_.add(v)
        return list_


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        """7.4. Compare two strings cleared of
        leading and trailing spaces."""
        return super(OrderedStringList, self).compare(
            v1.strip(), v2.strip())

