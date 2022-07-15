# this problem is complex, because of its complex nature. We have to find next and random pointer for this.
# LL with data, next ptr and a random ptr.
# How do we clone, to clone all nodes should be cloned first, then only we can update ptrs.

class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_random(self):
        return self.random

    def set_random(self, node):
        self.random = node


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

    def clone(self):

        map = {}
        current = self.head
        while current is not None:
            map[current] = node(current.get_value())
            current = current.get_next()

        new_head = node(-1)
        new_ll = new_head

        current = self.head
        while current is not None:
            new_node = map[current]

            if current.get_next() is not None:
                new_node.set_next(map[current.get_next()])

            new_node.set_random(map[current.get_random()])
            new_ll.set_next(new_node)
            new_ll = new_node
            current = current.get_next()

        return new_head.get_next()

    def traverse(self):
        current = self.head
        while current is not None and current.get_next() is not None and current.get_random() is not None:
            print(current.get_value(), current.get_next().get_value(), current.get_random().get_value())
            current = current.get_next()


ll = linked_list()
n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)

n1.set_random(n5)
n2.set_random(n4)
n3.set_random(n1)
n4.set_random(n3)
n5.set_random(n2)

ll.set_head(n1)
ll.set_head(n2)
ll.set_head(n3)
ll.set_head(n4)
ll.set_head(n5)

ll.traverse()
cloned = ll.clone()
ll.head = cloned
ll.traverse()
