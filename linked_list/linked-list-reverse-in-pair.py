# this is interesting, because we do swap.
class node:
    def __init__(self):
        self.value = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next


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

    # 1 2 3 4 5 6 --> # 2 1 4 3 6 5 : basically swap the values.
    def reverse_pair(self):
        current = self.head
        while current is not None and current.get_next() is not None:
            current_value = current.get_value()
            next = current.get_next()
            next_value = next.get_value()
            current.set_value(next_value)
            next.set_value(current_value)
            current = next.get_next()

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_value())
            current = current.get_next()


n1 = node()
n1.set_value(1)

n2 = node()
n2.set_value(2)

n3 = node()
n3.set_value(3)

n4 = node()
n4.set_value(4)

n5 = node()
n5.set_value(5)

ll = linked_list()
ll.set_head(n5)
ll.set_head(n4)
ll.set_head(n3)
ll.set_head(n2)
ll.set_head(n1)

ll.traverse()
ll.reverse_pair()
print("Reversed")
ll.traverse()
