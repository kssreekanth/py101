class node:
    def __init__(self):
        self.value = 0
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

    def set_head(self, node):
        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        self.length = self.length + 1

    # easy to find it since it's the middle of a sorted linked list.
    def median(self):
        mid = self.length / 2
        current = self.head
        while mid > 0:
            current = current.get_next()
            mid = mid - 1
        return current

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()

    def sort(self):
        current = self.head
        sorted_head = node()

        while current is not None:
            next = current.get_next()
            sorted_ptr = sorted_head
            prev = None
            while sorted_ptr is not None and sorted_ptr.get_value() > current.get_value():
                prev = sorted_ptr
                sorted_ptr = sorted_ptr.get_next()
            if prev is None:
                current.set_next(sorted_head.get_next())
                sorted_head.set_next(current)
            else:
                current.set_next(sorted_ptr)
                prev.set_next(current)

            current = next

        self.head = sorted_head


n1 = node()
n1.set_value(1)

n2 = node()
n2.set_value(2)

n3 = node()
n3.set_value(3)

n4 = node()
n4.set_value(4)

n = node()
n.set_value(2)

ll = linked_list()
ll.set_head(n1)
ll.set_head(n3)
ll.set_head(n2)
ll.set_head(n4)
ll.traverse()
ll.sort()
ll.traverse()
