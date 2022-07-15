class node:
    def __init__(self):
        self.value = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head(self):
        return self.head

    def set_head(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    def arrange_odd_even(self):
        if self.length == 0:
            return None

        if self.length == 1:
            return self.head

        odd = node()
        even = node()
        event_ptr = even
        odd_ptr = odd

        current = self.head
        while current is not None:
            if current.get_value() % 2 == 0:
                event_ptr.set_next(current)
                event_ptr = event_ptr.get_next()
            else:
                odd_ptr.set_next(current)
                odd_ptr = odd_ptr.get_next()
            current = current.get_next()

        odd_ptr.set_next(None)
        event_ptr.set_next(None)
        odd_ptr.set_next(even.get_next())
        self.head = odd.get_next()

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()


ll = linked_list()
n1 = node()
n1.set_value(1)
ll.set_head(n1)

n2 = node()
n2.set_value(2)
ll.set_head(n2)

n3 = node()
n3.set_value(3)
ll.set_head(n3)

n4 = node()
n4.set_value(4)
ll.set_head(n4)

n5 = node()
n5.set_value(5)
ll.set_head(n5)

ll.traverse()
ll.arrange_odd_even()
ll.traverse()
